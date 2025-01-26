# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/YouTube-Video-Download-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/YouTube-Video-Download-Bot



from pyrogram import Client, filters
from Youtube.config import Config

# Create a Pyrogram client
app = Client(
    "my_bot",
    api_id=Config.API_ID, 20968912
    api_hash=Config.API_HASH, d4d83a5da95269c7f4c91eecb84cf999
    bot_token=Config.BOT_TOKEN,7941335078:AAFtmzNiVGLU3Odr7nZI-zOmyHmkCGtsx8E
    plugins=dict(root="Youtube")
)



# Start the bot
print("🎊 I AM ALIVE 🎊")
app.run()
