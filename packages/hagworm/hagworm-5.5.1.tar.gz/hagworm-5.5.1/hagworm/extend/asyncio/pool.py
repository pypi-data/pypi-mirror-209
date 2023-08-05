# -*- coding: utf-8 -*-

__author__ = r'wsb310@gmail.com'

from asyncio import Queue
from contextlib import contextmanager, asynccontextmanager

from hagworm.extend.base import Utils


class ObjectPool:
    """对象池实现
    """

    def __init__(self, maxsize, key_prefix=None):

        self._key_prefix = key_prefix

        self._queue = Queue(maxsize=maxsize)

    async def _create_obj(self):

        raise NotImplementedError()

    async def _delete_obj(self, obj):

        raise NotImplementedError()

    async def open(self):

        while not self._queue.full():
            self._queue.put_nowait(
                await self._create_obj()
            )

        Utils.log.info(f'ObjectPool {type(self)} initialized: {self._queue.qsize()}')

    async def close(self):

        while not self._queue.empty():
            await self._delete_obj(
                self._queue.get_nowait()
            )

    @property
    def size(self):

        return self._queue.qsize()

    def key(self, _key):

        if self._key_prefix:
            return f'{self._key_prefix}/{_key}'
        else:
            return _key

    @asynccontextmanager
    async def get(self):

        Utils.log.debug(f'ObjectPool {type(self)} size: {self._queue.qsize()}')

        obj = await self._queue.get()

        try:
            yield obj
        except Exception as err:
            raise err
        finally:
            self._queue.put_nowait(obj)

    @contextmanager
    def get_nowait(self):

        Utils.log.debug(f'ObjectPool {type(self)} size: {self._queue.qsize()}')

        obj = self._queue.get_nowait()

        try:
            yield obj
        except Exception as err:
            raise err
        finally:
            self._queue.put_nowait(obj)
