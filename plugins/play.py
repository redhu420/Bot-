from pyrogram import Client, filters
from pytgcalls import PyTgCalls

def init(app: Client, pytgcalls: PyTgCalls):
    @app.on_message(filters.command("play") & filters.group)
    async def play_command(_, message):
        await message.reply_text("🎶 Playing song... (dummy response)")
