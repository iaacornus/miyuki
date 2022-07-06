from os import getenv

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

    msg: str = message.content.lower()
