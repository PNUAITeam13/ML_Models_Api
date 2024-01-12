from os import environ


class Config(object):
    FLASK_DEBUG = False
    DEVELOPMENT = False

    @staticmethod
    def get_config():
        return config[environ.get('CONFIG') or "DEFAULT"]


class DevConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class ProdConfig(Config):
    DEVELOPMENT = False
    DEBUG = False


config = {
    'DEV': DevConfig,
    'PROD': ProdConfig,
    'DEFAULT': DevConfig,
}
