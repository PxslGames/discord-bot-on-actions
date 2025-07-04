import discord
from discord.ext import commands
import os
import threading
import time

# Auto-exit after 59 minutes to let GitHub Actions restart the bot cleanly
def auto_exit():
    time.sleep(60 * 59)
    print("Restarting bot...")
    os._exit(0)

threading.Thread(target=auto_exit).start()

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user.name}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(os.getenv("TOKEN"))
