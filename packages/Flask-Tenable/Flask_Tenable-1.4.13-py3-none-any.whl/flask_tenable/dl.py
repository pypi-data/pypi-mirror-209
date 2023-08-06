from flask import Flask
from tenable.dl import Downloads as _Downloads

__all__ = ['Downloads']


class Downloads(_Downloads):
    _env_base = 'TENABLE_DOWNLOADS'

    def __init__(self, app: Flask = None, **kwargs):  # noqa
        # hold back super.__init__ until the needed values are present
        self.__kwargs = kwargs
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        self.__kwargs.update({
            'api_token': app.config[f'{self._env_base}_API_TOKEN'],
        })
        super().__init__(**self.__kwargs)
