from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "28188113"
# -------------------------------------------------------------
API_HASH = "81719734c6a0af15e5d35006655c1f84"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", None)
MONGO_URL = getenv("MONGO_URL", None)
OWNER_ID = int(getenv("OWNER_ID", "6955568347"))
SUPPORT_GRP = "DNS_NETWORK"
UPDATE_CHNL = "Dns_Official_Channel"
OWNER_USERNAME = "II_RAJPUT_SHIV_OP_II"
