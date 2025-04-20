# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

INST_COOKIES = """"""

YTUB_COOKIES = """"""

API_ID = os.getenv("API_ID", "25316666")
API_HASH = os.getenv("API_HASH", "804e92d43aa2d7a2a0a552b46f38646a")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8054346385:AAFTYzkfhDQ3y2C6Vs2EdakJj4TCkUL7EMI")
MONGO_DB = os.getenv("MONGO_DB", "mongodb+srv://creativexanas:Axbxcxdx1900@cluster0.w870qby.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "7314813409").split()))
DB_NAME = os.getenv("DB_NAME", "telegram_downloader")
STRING = os.getenv("STRING", '')
LOG_GROUP = int(os.getenv("LOG_GROUP", "-1002338464600"))
FORCE_SUB = int(os.getenv("FORCE_SUB", "-1002586263929"))
MASTER_KEY = os.getenv("MASTER_KEY", "gK8HzLfT9QpViJcYeB5wRa3DmN7P2xUq")
IV_KEY = os.getenv("IV_KEY", "s7Yx5CpVmE3F")
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "500"))
