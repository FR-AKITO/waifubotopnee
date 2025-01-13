import logging  

from pyrogram import Client 

from telegram.ext import Application
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("apscheduler").setLevel(logging.ERROR)
logging.getLogger('httpx').setLevel(logging.WARNING)
logging.getLogger("pyrate_limiter").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

OWNER_ID = "6632519077"
sudo_users = ["6632519077"]
GROUP_ID = "-1002055176072"
TOKEN = "7256217879:AAEM3lP4dTxN-3LJDvpXuik-PeFcY8n4oyE"
mongo_url = "mongodb+srv://tiwarireeta004:peqxLEd36RAg7ors@cluster0.furypd3.mongodb.net/?retryWrites=true&w=majority"
PHOTO_URL = ["https://telegra.ph/file/a17bbdf36197b0f0eb2c1.jpg", "https://telegra.ph/file/4754711cd88be32baf5b4.jpg", "https://telegra.ph/file/46b1151c6088fabc62250.jpg", "https://telegra.ph/file/4ed692d4e678216f87083.jpg"]
SUPPORT_CHAT = "BeybladeVerse"
UPDATE_CHAT = "BeybladeXD"
BOT_USERNAME = "YxH_Game_Bot"
CHARA_CHANNEL_ID = "-1002055176072"
api_id = "20457610"
api_hash = "b7de0dfecd19375d3f84dbedaeb92537"

application = Application.builder().token(TOKEN).build()
Grabberu = Client("Grabber", api_id, api_hash, bot_token=TOKEN)
client = AsyncIOMotorClient(mongo_url)
db = client['Character_catcher']
collection = db['anime_characters']
user_totals_collection = db['user_totals']
user_collection = db["user_collection"]
group_user_totals_collection = db['group_user_total']
top_global_groups_collection = db['top_global_groups']
