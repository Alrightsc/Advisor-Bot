from discord.ext import commands
from utils import config

import discord
import datetime
import sys
import traceback

initial_exts = ["cogs.notawiki",
                "cogs.help",
                "cogs.owner"]

def getPrefix(bot, msg):
    prefixes = ["."]
    return commands.when_mentioned_or(*prefixes)(bot, msg)

class AdvisorBot(commands.AutoShardedBot):
    def __init__(self):
        super().__init__(command_prefix=getPrefix, help_command=None)

        for extension in initial_exts:
            try:
                self.load_extension(extension)
            except Exception:
                print(f'Failed to load extension {extension}.', file=sys.stderr)
                traceback.print_exc()

    async def on_ready(self):
        if not hasattr(self, 'uptime'):
            self.uptime = datetime.datetime.utcnow()
        await self.change_presence(activity=discord.Game('Excavating more Rubies for your Majesty. .help for info'), status=discord.Status.online)

        print(f'Online and running. {self.user} (ID: {self.user.id}) at {datetime.datetime.utcnow()}.')

    def run(self):
        super().run(config.get_token(), reconnect=True)


if __name__ == '__main__':
    bot = AdvisorBot()
    bot.run()