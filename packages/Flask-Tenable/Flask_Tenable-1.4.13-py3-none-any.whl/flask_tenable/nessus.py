from flask import Flask
from tenable.nessus import Nessus as _Nessus

__all__ = ['Nessus']


class Nessus(_Nessus):
    _env_base = 'TENABLE_NESSUS'

    def __init__(self, app: Flask = None, **kwargs):  # noqa
        # hold back super.__init__ until the needed values are present
        self.__kwargs = kwargs
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        self.__kwargs.update({
            'url': f"https://{app.config[f'{self._env_base}_HOST']}",
            'access_key': app.config[f'{self._env_base}_ACCESS_KEY'],
            'secret_key': app.config[f'{self._env_base}_SECRET_KEY'],
        })
        super().__init__(**self.__kwargs)
