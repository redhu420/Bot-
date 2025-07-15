from pyrogram import Client, filters
from pytgcalls import PyTgCalls

def init(app: Client, pytgcalls: PyTgCalls):
    @app.on_message(filters.command("pause") & filters.group)
    async def pause_command(_, message):
        await message.reply_text("⏸️ Paused playback.")
