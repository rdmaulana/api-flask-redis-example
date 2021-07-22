import os

class BaseConfig(object):
    CACHE_TYPE="redis"
    CACHE_REDIS_HOST="redis"
    CACHE_REDIS_PORT=6379
    CACHE_REDIS_DB=0
    CACHE_REDIS_URL="redis://127.0.0.1:6379/0"
    CACHE_DEFAULT_TIMEOUT=500