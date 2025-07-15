from pyrogram import Client, filters
from pytgcalls import PyTgCalls

def init(app: Client, pytgcalls: PyTgCalls):
    @app.on_message(filters.command("skip") & filters.group)
    async def skip_command(_, message):
        await message.reply_text("⏭️ Skipped to next.")
