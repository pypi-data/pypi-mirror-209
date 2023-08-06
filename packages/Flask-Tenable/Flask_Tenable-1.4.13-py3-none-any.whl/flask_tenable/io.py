from flask import Flask
from tenable.io import TenableIO as _TenableIO

__all__ = ['TenableIO']


class TenableIO(_TenableIO):
    _env_base = 'TENABLE_IO'

    def __init__(self, app: Flask = None, **kwargs):  # noqa
        # hold back super.__init__ until the needed values are present
        self.__kwargs = kwargs
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        self.__kwargs.update({
            'access_key': app.config[f'{self._env_base}_ACCESS_KEY'],
            'secret_key': app.config[f'{self._env_base}_SECRET_KEY'],
        })
        super().__init__(**self.__kwargs)
