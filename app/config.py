from decouple import config


DB_HOST = config("DB_HOST", cast=str)
DB_PORT = config("DB_PORT", cast=int)
DB_USER = config("DB_USER", cast=str)
DB_PASS = config("DB_PASS", cast=str)
DB_NAME = config("DB_NAME", cast=str)
