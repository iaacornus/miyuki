from os import getenv
from os.path import dirname

import discord
from dotenv import load_dotenv
from discord.ext import commands

from src.utils.logger import Logger


load_dotenv()

log: object = Logger()

client = commands.Bot(command_prefix="~!")
TOKEN = getenv("TOKEN")


if __name__ != "__main__":
    log.logger("error", "Not inteded for use as library!")
    raise SystemExit


@client.event
async def on_read():
    log.logger("passed", "Successfully started the discord bot.")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    BASE_DIR: str = "/".join(dirname(__file__).split("/")[:-2])
    PATH: str = f"{BASE_DIR}/training_data"

    try:
        with open(
                f"{PATH}/discord_conversations.txt", "a", encoding="utf-8"
            ) as live_data:
            live_data.write(f"{message}\n")
    except (IOError, PermissionError) as exception:
        log.logger("error", f"Exception: {exception} was raised, aborting ...")
        raise SystemExit

    msg: str = message.content.lower()
