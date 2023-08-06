from flask import Flask
from tenable.ad import TenableAD as _TenableAD

__all__ = ['TenableAD']


class TenableAD(_TenableAD):
    _env_base = 'TENABLE_AD'

    def __init__(self, app: Flask = None, **kwargs):  # noqa
        # hold back super.__init__ until the needed values are present
        self.__kwargs = kwargs
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        self.__kwargs.update({
            'api_key': app.config[f'{self._env_base}_API_KEY'],
        })
        super().__init__(**self.__kwargs)
