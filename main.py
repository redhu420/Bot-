from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from config import *
from plugins import play, pause, skip

app = Client("music_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
pytgcalls = PyTgCalls(app)

@app.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_text("🎵 Music Bot is up and running!")

# Load plugin commands
play.init(app, pytgcalls)
pause.init(app, pytgcalls)
skip.init(app, pytgcalls)

app.start()
pytgcalls.start()
print("Music bot is running...")
app.idle()
