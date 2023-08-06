import sys

import pyrogram
from naya.config import CMD_HNDLR as cmd
from pyrogram import *
from pyrogram import Client, filters
from pytgcalls import GroupCallFactory


class Ubot(Client):
    __module__ = "pyrogram.client"
    _bots = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.group_call = GroupCallFactory(self).get_group_call()

    def on_message(self, filters=filters.Filter, group=-1):
        def decorator(func):
            for bot in self._bots:
                bot.add_handler(MessageHandler(func, filters), group)
            return func

        return decorator

    async def start(self):
        await super().start()
        if self not in self._bots:
            self._bots.append(self)


def naya(command: str, prefixes: cmd):
    def wrapper(func):
        @Client.on_message(filters.command(command, prefixes) & filters.me)
        async def wrapped_func(client, message):
            await func(client, message)

        return wrapped_func

    return wrapper


def devs(command: str):
    def wrapper(func):
        @Client.on_message(
            filters.command(command, ".") & filters.user(DEVS) & ~filters.me
        )
        def wrapped_func(client, message):
            return func(client, message)

        return wrapped_func

    return wrapper
