# © Cyril C Thomas
# https://t.me/cyril_c_10

import os

class Config(object):
    BOT_TOKEN = os.environ.get("7919283586:AAFIq7A0LuVG5nCdxBnWheNHf_cglXh8GQU", "")
    API_ID = int(os.environ.get("APP_ID", ))
    API_HASH = os.environ.get("API_HASH", "")
    LOG_CHANNEL = int(os.environ.get("t.me/tcronebhackx", -100))
    MONGODB_URI = os.environ.get("MONGODB_URI", "")
    SESSION_NAME = os.environ.get("SESSION_NAME", "")
    BOT_OWNER = int(os.environ.get("TcronebNet", ))
