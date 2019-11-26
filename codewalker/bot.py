"""
codewalker main file

(c) 2019 tilda, under the Apache 2 License
"""
import lifesaver
import time
import aiohttp
import discord
from discord.ext.commands import DefaultHelpCommand
class CodeWalker(lifesaver.bot.AutoShardedBot):
    def __init__(self, cfg, **kwargs):
        # i'm gonna be honest i have no idea what this does
        # but it looks important
        super().__init__(cfg, **kwargs)
        
        # http is important
        self.session = aiohttp.ClientSession(loop=self.loop)

        # for uptime purposes
        self.init_time = time.time()
