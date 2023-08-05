# -*- coding: utf-8 -*-

__author__ = r'wsb310@gmail.com'

from contextlib import asynccontextmanager
from async_etcd3gw import AsyncEtcd3Client, AsyncLock
from async_etcd3gw.async_client import DEFAULT_PORT, DEFAULT_PROTOCOL, DEFAULT_API_PATH

from .pool import ObjectPool


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

        super().__init__(maxsize, key_prefix)

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

    async def _create_obj(self) -> AsyncEtcd3Client:

        return AsyncEtcd3Client(**self._config)

    async def _delete_obj(self, obj: AsyncEtcd3Client):

        await obj.close()

    @asynccontextmanager
    async def lock(self, name, ttl=60) -> AsyncLock:

        async with self.get() as client, await client.lock(self.key(name), ttl) as lock:
            yield lock
