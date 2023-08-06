from flask import Flask
from tenable.sc import TenableSC as _TenableSC

__all__ = ['TenableSC']


class TenableSC(_TenableSC):
    _env_base = 'TENABLE_SC'

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
