import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

import pyrogram



if __name__ == "__main__" :
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "All In One Bot",
        bot_token=Config.TG_BOT_TOKEN,(2139262171:AAEfhaKTgAXTOMQsZW-NyNzx57yip2_l9dk)
        api_id=Config.APP_ID,(5350175)
        api_hash=Config.API_HASH,(9fe77c9c85e1b8569fb5e82e534ba7af)
        plugins=plugins
    )
    Config.AUTH_USERS.add(1633617583)
    app.run()
