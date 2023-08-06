# -*- coding: utf-8 -*-

__author__ = r'wsb310@gmail.com'

import asyncio

from contextlib import asynccontextmanager
from async_etcd3gw import AsyncEtcd3Client as _AsyncEtcd3Client, AsyncLock as _AsyncLock
from async_etcd3gw.async_client import DEFAULT_PORT, DEFAULT_PROTOCOL, DEFAULT_API_PATH

from .pool import ObjectPool


DEFAULT_TIMEOUT = 60


class AsyncEtcd3Client(_AsyncEtcd3Client):

    async def lock(self, name, ttl=DEFAULT_TIMEOUT):
        return AsyncLock(name, ttl=ttl, async_client=self)


class AsyncLock(_AsyncLock):

    async def acquire(self, timeout=None):

        if timeout is None:
            return await super().acquire()
        else:
            return await asyncio.wait_for(self._acquire(), timeout)

    async def _acquire(self):

        while not (result := await super().acquire()):

            events, cancel = await self.async_client.watch(self.key)

            async for event in events:

                if event.get(r'type') == r'DELETE':
                    await cancel()
                    break

        return result

    async def __aenter__(self):
        return self


class Etcd3ClientPool(ObjectPool):

    def __init__(
        self, maxsize, host, *,
        port=DEFAULT_PORT,
        protocol=DEFAULT_PROTOCOL,
        ca_cert=None,
        cert_key=None,
        cert_cert=None,
        timeout=None,
        api_path=DEFAULT_API_PATH,
        key_prefix=None
    ):

        super().__init__(maxsize)

        self._config = {
            r'host': host,
            r'port': port,
            r'protocol': protocol,
            r'ca_cert': ca_cert,
            r'cert_key': cert_key,
            r'cert_cert': cert_cert,
            r'timeout': timeout,
            r'api_path': api_path,
        }

        self._key_prefix = key_prefix

    async def _create_obj(self) -> AsyncEtcd3Client:

        return AsyncEtcd3Client(**self._config)

    async def _delete_obj(self, obj: AsyncEtcd3Client):

        await obj.close()

    def key(self, _key):

        if self._key_prefix:
            return f'{self._key_prefix}{_key}'
        else:
            return _key

    @asynccontextmanager
    async def lock(self, name, ttl=DEFAULT_TIMEOUT) -> AsyncLock:

        async with self.get() as client, await client.lock(self.key(name), ttl) as lock:
            yield lock
