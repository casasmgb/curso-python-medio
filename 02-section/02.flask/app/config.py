class Config:
    DEBUG = False
    TESTING = False
    PORT = 5000
    HOST = '0.0.0.0'
    DB = 'sistema.db'

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True

class ProductionConfig(Config):
    pass

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': ProductionConfig
}
