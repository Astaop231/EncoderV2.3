# Fuck yea 👍
import logging
from logging.handlers import RotatingFileHandler
import os
import time
from pyrogram import Client


# TODO: is there a better way?




from bot.config import Config



# dont think ne dumb (c) @Animes_Encoded
AUTH_USERS = [1666551439] # add another id with , like [26272, 172727] , dont remove my id
# again lol (c) @Animes_Encoded 

SESSION_NAME = "WtfMan"
TG_BOT_TOKEN = " "  
APP_ID = 
API_HASH = " " 

LOG_CHANNEL = " "   # make sure to us this 
DOWNLOAD_LOCATION = "/app/downloads"
FREE_USER_MAX_FILE_SIZE = 2097152000
MAX_MESSAGE_LENGTH = 4096
FINISHED_PROGRESS_STR = "▓"
UN_FINISHED_PROGRESS_STR = "░"
BOT_START_TIME = time.time()
LOG_FILE_ZZGEVC = "Log.txt"
BOT_USERNAME = " "
UPDATES_CHANNEL = "botlogas"
data = []
crf = []
watermark = []
resolution = []
codec = []
preset = []
audio_b = []
font_one = []
font_two = []
# senpai I am changing app string WHY???????
pid_list = []
app = Client(
        SESSION_NAME,
        bot_token=TG_BOT_TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        workers=2
    )
if os.path.exists(LOG_FILE_ZZGEVC):
    with open(LOG_FILE_ZZGEVC, "r+") as f_d:
        f_d.truncate(0)

# the logging things
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            LOG_FILE_ZZGEVC,
            maxBytes=FREE_USER_MAX_FILE_SIZE,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)
