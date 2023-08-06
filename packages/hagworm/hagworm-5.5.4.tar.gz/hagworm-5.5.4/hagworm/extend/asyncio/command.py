# -*- coding: utf-8 -*-

__author__ = r'wsb310@gmail.com'

from typing import Callable

from ... import hagworm_slogan
from ... import __version__ as hagworm_version

from .base import install_uvloop, Utils
from .socket import UnixSocketServer, UnixSocketClient, DEFAULT_LIMIT

from ..interface import RunnableInterface
from ..process import Daemon


class MainProcessAbstract(Daemon):

    def __init__(
            self, target: Callable, sub_process_num: int, *,
            keep_live: bool = False, set_affinity=None,
            unix_socket_path=r'/tmp/unix_socket_endpoint', unix_socket_limit=DEFAULT_LIMIT,
            **kwargs
    ):

        self._socket_server = UnixSocketServer(self._client_connected_cb, unix_socket_path, unix_socket_limit)

        super().__init__(
            target, sub_process_num, keep_live=keep_live, set_affinity=set_affinity,
            unix_socket_path=unix_socket_path,
            **kwargs
        )

    async def _client_connected_cb(self, reader, writer):
        raise NotImplementedError()

    async def _run(self):

        self._fill_process()

        while self.is_active():
            self._check_process()
            await Utils.sleep(1)

    def run(self):

        environment = Utils.environment()

        Utils.log.info(
            f'{hagworm_slogan}'
            f'hagworm {hagworm_version}\n'
            f'python {environment["python"]}\n'
            f'system {" ".join(environment["system"])}'
        )

        install_uvloop()

        Utils.run_until_complete(self._socket_server.open())
        Utils.run_until_complete(self._run())
        Utils.run_until_complete(self._socket_server.close())


class SubProcessAbstract(RunnableInterface):

    @classmethod
    def create(cls, unix_socket_path):

        cls(unix_socket_path).run()

    def __init__(self, unix_socket_path: str):

        self._socket_client = UnixSocketClient(unix_socket_path)

        self._process_id = Utils.getpid()

    async def _run(self):
        raise NotImplementedError()

    def run(self):

        Utils.log.success(f'Started worker process [{self._process_id}]')

        install_uvloop()

        Utils.run_until_complete(self._socket_client.open())
        Utils.run_until_complete(self._run())
        Utils.run_until_complete(self._socket_client.close())

        Utils.log.success(f'Stopped worker process [{self._process_id}]')
