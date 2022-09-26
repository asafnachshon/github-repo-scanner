import tornado.web

from abc import ABCMeta
from http import HTTPStatus


class Main(tornado.web.RequestHandler, metaclass=ABCMeta):
    http_status = HTTPStatus

    @classmethod
    def initialize(cls, **kwargs):
        return

    async def prepare(self):
        pass

    def write_error(self, **kwargs):
        pass

    def log_exception(self, typ, value, tb):
        pass


__all__ = ["Main"]
