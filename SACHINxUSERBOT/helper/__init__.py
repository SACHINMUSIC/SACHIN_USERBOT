import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "SACHINxUSERBOT"])

async def join(client):
    try:
        await client.join_chat("All_SANATANI_BOT")
    except BaseException:
        pass
