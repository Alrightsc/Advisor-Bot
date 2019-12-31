from discord.ext import commands
from utils import FactionUpgrades, NaWSearch

import datetime
import discord

alias = {
    "upgrade": ["upg", "up", "u"],
    "challenge": ["ch", "c"],
    "research": ["r", "res"],
    "lineage": ["l", "line"]
}

class Notawiki(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=alias["upgrade"])
    async def upgrade(self, ctx, arg=None, number=None):
        """Retrieves information of a Faction Upgrade from Not-a-Wiki"""

        # Checking if input returns an abbreviation faction i.e. FR7 or MK11, also accepts lowercase inputs
        if arg[2].isdigit() and number is None:
            faction = arg.upper()
            argColor = faction[0:2]
            color = FactionUpgrades.getFactionColour(argColor)

        # if number is added as an input, we automatically assume the full term, i.e. "Fairy 7"
        elif number is not None:
            # Some people just like to watch the world burn
            if int(number) < 1 or int(number) > 12:
                raise Exception('Invalid Input')

            arg2 = arg.lower()
            arg2 = arg2.capitalize()
            checks, fac, color = FactionUpgrades.getFactionAbbr(arg2)

            # checks is retrieved from FactionUpgrades, if the term is not in dictionary it returns False and we
            # raise Exception error
            if checks is False:
                raise Exception('Invalid Input')
            else:
                faction = fac + number

        # if inputs match neither above, raise Exception
        else:
            raise Exception('Invalid Input')

        async with ctx.channel.typing():
            # We get our list through Not-a-Wiki Beautiful Soup search
            data = NaWSearch.factionUpgrade(faction)

            # Embed things, using the list retrieved from factionUpgradeSearch
            thumbnail = data[0]
            title = f'**{data[1]}**'
            embed = discord.Embed(title=title, colour=discord.Colour(color), timestamp=datetime.datetime.utcnow())
            embed.set_footer(text="http://musicfamily.org/realm/FactionUpgrades/",
                             icon_url="http://musicfamily.org/realm/Factions/picks/RealmGrinderGameRL.png")
            embed.set_thumbnail(url=thumbnail)

            # Since the first two lines always are guaranteed to be an url and name of Faction upgrade, we ignore
            # them, and then start processing adding new fields for each line
            try:
                for line in data[2:]:
                    newline = line.split(": ")
                    first = f'**{newline[0]}**'
                    embed.add_field(name=first, value=newline[1], inline=False)
            except IndexError:
                return await ctx.send('There is something wrong with this upgrade. Notify Alright#2304')

        await ctx.send(embed=embed)

    @commands.command(aliases=alias["challenge"])
    async def challenge(self, ctx, arg=None, number=None):
        """Retrieves information of a Faction Challenge from Not-a-Wiki"""

        # Checking if input returns an abbreviation faction i.e. FR2 or MK5, also accepts lowercase inputs
        if arg[2].isdigit() or arg[2] in ["R", "r", "C", "c"] and number is None:
            if arg[2] in ["C", "c"]:
                arg = arg[:2] + arg[3:]
            faction = arg.upper()
            argColor = faction[0:2]
            color = FactionUpgrades.getFactionColour(argColor)
            # No huge dictionary this time around
            faction2 = FactionUpgrades.getFactionNameFull(argColor)
            faction = faction2 + faction[0] + "C" + faction[2:]

        # if number is added as an input, we automatically assume the full term, i.e. "Fairy 7"
        elif number is not None:
            # Number checker has been moved to factionChallengeSearch()
            arg2 = arg.lower()
            arg2 = arg2.capitalize()
            checks, fac, color = FactionUpgrades.getFactionAbbr(arg2)

            # checks is retrieved from FactionUpgrades, if the term is not in dictionary it returns False and we
            # raise Exception error
            if checks is False:
                raise Exception('Invalid Input')
            else:
                faction = arg2 + arg2[0] + "C" + str(number).upper()

        # if inputs match neither above, raise Exception
        else:
            raise Exception('Invalid Input')

        async with ctx.channel.typing():
            data = NaWSearch.challenge(faction)

            ignore = 4

            # Embed things, using the list retrieved from factionChallengeSearch
            thumbnail = data[0]
            # Spell rewards need special formatting
            if faction[-1:] == "R":
                title = f'**{data[1]}**'
                ignore = 3
            else:
                title = f'**{data[2]} : {data[1]}**'
            embed = discord.Embed(title=title, colour=discord.Colour(color), timestamp=datetime.datetime.utcnow())
            embed.set_footer(text="http://musicfamily.org/realm/Challenges/",
                             icon_url="http://musicfamily.org/realm/Factions/picks/RealmGrinderGameRL.png")
            embed.set_thumbnail(url=thumbnail)

            # Ignore the first 4 fields and create the rest
            for line in data[ignore:]:
                newline = line.split(": ")
                first = f'**{newline[0]}**'
                embed.add_field(name=first, value=newline[1], inline=False)

        await ctx.send(embed=embed)

    @commands.command(aliases=alias["research"])
    async def research(self, ctx, researchName=None):
        """Retrieves Research upgrade from Not-a-Wiki"""
        image = ''

        # Capitalizing researchName, adding check and importing the research dict
        researchName = researchName.upper()
        check = False
        rbranch = FactionUpgrades.getResearchBranch()

        # Checks if first letter is an alphabet and the input after 0th index are digits
        if researchName[0].isalpha() and researchName[1:].isdigit():
            for key, value in rbranch.items():
                if key[0] == researchName[0]:
                    image = value
                    check = True

        if not check:
            raise Exception("Invalid Input")

        async with ctx.channel.typing():
            data = NaWSearch.research(researchName)

            # data[0] and data[2] returns the shorthand research and the name of research
            title = f'{data[0]} - {data[2]}'

            # mostly "For x factions"
            description = data[1]

            embed = discord.Embed(title=title, description=description, colour=discord.Colour.dark_green())
            embed.set_footer(text="http://musicfamily.org/realm/Researchtree/",
                             icon_url="http://musicfamily.org/realm/Factions/picks/RealmGrinderGameRL.png")
            embed.set_thumbnail(url=image)

            # Cleaning the list
            for line in data[3:]:
                line = line.strip()
                newLine = line.split(": ")
                embed.add_field(name=f'**{newLine[0]}**', value=newLine[1], inline=False)

        await ctx.send(embed=embed)

    @commands.command(aliases=alias['lineage'])
    async def lineage(self, ctx, faction, number):
        pass

    @upgrade.error
    @challenge.error
    @research.error
    @lineage.error
    async def universal_error(self, ctx, error):
        if isinstance(error, Exception):
            title = " :exclamation:  Command Error!"
            description = "The parameters you used are not found in the list. Please try again."
            embed = discord.Embed(title=title, description=description, colour=discord.Colour.red())
            return await ctx.send(embed=embed)


####
def setup(bot):
    bot.add_cog(Notawiki(bot))