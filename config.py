import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID","17221046"))
API_HASH = getenv("API_HASH", "233ef51a2c05a3979f95d7c7730cf320")

BOT_TOKEN = getenv("BOT_TOKEN", "5667013817:AAEp9ZEBF6C2bfN9D4Om2xLrOv0dwyNMTW8")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Belly:belly55@atlascluster.ends7zl.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001573996982"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "sᴜᴍɪᴛ ダ ᴍᴜsɪᴄ")

OWNER_ID = list(map(int, getenv("OWNER_ID", "2139088940").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AnonymousX1025/AnonXMusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ab_sumit")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/bellysupportchat")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQAKUD-GMHipdtsv8dlkeDoMLWtgnrfdzNiQcQI3eRXoBoEIbxWEzJzWgxTQmaw_dpJp3WARM-WuorAI-G0n1P8Hdo7MapjC6mCpo6-j0rSagCqfgFIBxmB5XtDXb4Wp60OZUm64hNido6drMeqRbVQQrQ3BLtwAgSnkN6XY3yZGqbipun4O1NtsPAbf5ckINZVyc8F-lT1eVk3PjSerCfGkmedJpEk0KmDcoWj0YkanMnzao5JO_bMZH4xtuPgtE-zogHeoFRZyBGDOE8_pufeFEV23xOlM7pna4fTkCLJ1J-IHYE-MpKyMQPFNTejsGJDN9ty7QUkvj02auoJ5D35XAAAAAUqDigcA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://te.legra.ph/file/8eb3466b2e2fc39263665.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/56d1760224589ee370186.jpg",
)

PLAYLIST_IMG_URL = "https://te.legra.ph/file/1296994c1a55dde6323b2.jpg"

GLOBAL_IMG_URL = "https://te.legra.ph/file/88e0c7be525de0d93854e.jpg"

STATS_IMG_URL = "https://te.legra.ph/file/88e0c7be525de0d93854e.jpg"

TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/d4e79e1719a07e53da4fe.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/d4e79e1719a07e53da4fe.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/5f9ae00cde0806a969197.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/5f9ae00cde0806a969197.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://te.legra.ph/file/1296994c1a55dde6323b2.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://te.legra.ph/file/8eb3466b2e2fc39263665.jpg"
