from discord.ext import commands
from utils import FactionUpgrades, NaWSearch

import datetime
import discord

alias = {
    "upgrade": ["upg", "up", "u"],
    "challenge": ["ch", "c"],
    "research": ["res", "r"],
    "lineage": ["line", "l"],
    "artifact": ["art", "a"],
    "bloodline": ["bl", "b"]
}


class Notawiki(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = discord.Colour.magenta()

    @commands.command(aliases=alias["upgrade"])
    async def upgrade(self, ctx: commands.Context, faction=None, number=None):
        """Retrieves information of a Faction Upgrade from Not-a-Wiki"""
        if faction in ['help', 'Help'] or (faction == None and number == None):
            emoji = discord.utils.get(ctx.guild.emojis, name="SuggestionMaster")
            description = "**.upgrade <faction>**\n**Aliases: **" + ', '.join(alias["upgrade"]) + \
                          "\n\nRetrieves a Faction upgrade information " \
                          "directly from Not-a-Wiki. <faction> inputs can be using two-letter Mercenary Template with " \
                          "upgrade number, or full Faction name with an upgrade number.\n\nExamples: Fairy 7, MK10 "
            embed = discord.Embed(title=f"{emoji}  Upgrade", description=description, colour=self.color)
            return await ctx.send(embed=embed)

        # Checking if input returns an abbreviation faction i.e. FR7 or MK11, also accepts lowercase inputs
        if faction[2].isdigit() and number is None:
            faction = faction.upper()
            color = FactionUpgrades.getFactionColour(faction[0:2])

        # if number is added as an input, we automatically assume the full term, i.e. "Fairy 7"
        elif number is not None:
            # Some people just like to watch the world burn
            if int(number) < 1 or int(number) > 12:
                raise Exception('Invalid Input')

            faction = faction.lower()
            faction = faction.capitalize()
            checks, fac, color = FactionUpgrades.getFactionAbbr(faction)

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
            upgradeEmbed = NaWSearch.factionUpgrade(faction)
            author: discord.Member = ctx.message.author

            # Embed things, using the list retrieved from factionUpgradeSearch
            title = f'**{upgradeEmbed[1]}**'
            embed = discord.Embed(title=title, colour=discord.Colour(color), timestamp=datetime.datetime.utcnow())
            embed.set_footer(text="http://musicfamily.org/realm/FactionUpgrades/",
                             icon_url="http://musicfamily.org/realm/Factions/picks/RealmGrinderGameRL.png") \
                 .set_thumbnail(url=upgradeEmbed[0]) \
                 .set_author(name=author, icon_url=author.avatar_url)

            # Since the first two lines always are guaranteed to be an url and name of Faction upgrade, we ignore
            # them, and then start processing adding new fields for each line
            try:
                for line in upgradeEmbed[2:]:
                    line = line.split(": ")
                    embed.add_field(name=f'**{line[0]}**', value=line[1], inline=False)
            except IndexError:
                return await ctx.send('There is something wrong with this upgrade. Notify Alright#2304')

        await ctx.send(embed=embed)

    @commands.command(aliases=alias["challenge"])
    async def challenge(self, ctx: commands.Context, faction=None, number=None):
        """Retrieves information of a Faction Challenge from Not-a-Wiki"""

        # Help command
        if faction in ['help', 'Help'] or (faction == None and number == None):
            emoji = discord.utils.get(ctx.guild.emojis, name="SuggestionMaster")
            description = "**.challenge <faction>**\n**Aliases: **" + ', '.join(alias["challenge"]) + "\n\nRetrieves " \
                          "challenge info from Not-a-Wiki displaying name, requirements, effects, and formulas. Valid " \
                          "inputs include using faction name and the challenge number, or r for spell challenge " \
                          "reward. Mercenary templates in place of full name can be used, adding C# or \"R\".\n\nExample: " \
                          "Fairy 2, Makers r, DGC5, DJR"
            embed = discord.Embed(title=f"{emoji}  Challenge", description=description,
                                  colour=self.color)
            return await ctx.send(embed=embed)

        # Too many people call Mercenary "merc" so this is to make it easier
        if faction in ["merc", "Merc"]:
            faction = "Mercenary"

        # Checking if input returns an abbreviation faction i.e. FR2 or MK5, also accepts lowercase inputs
        if faction[2].isdigit() or faction[2] in ["R", "r", "C", "c"] and number is None:
            if faction[2] in ["C", "c"]:
                faction = faction[:2] + faction[3:]
            faction = faction.upper()
            factionColor = faction[0:2]
            color = FactionUpgrades.getFactionColour(factionColor)
            # No huge dictionary this time around
            faction2 = FactionUpgrades.getFactionNameFull(factionColor)
            faction = faction2 + faction[0] + "C" + faction[2:]

        # if number is added as an input, we automatically assume the full term, i.e. "Fairy 7"
        elif number is not None:
            # Number checker has been moved to factionChallengeSearch()
            faction = faction.lower()
            faction = faction.capitalize()
            checks, fac, color = FactionUpgrades.getFactionAbbr(faction)

            # checks is retrieved from FactionUpgrades, if the term is not in dictionary it returns False and we
            # raise Exception error
            if checks is False:
                raise Exception('Invalid Input')
            else:
                faction = faction + faction[0] + "C" + str(number).upper()

        # if inputs match neither above, raise Exception
        else:
            raise Exception('Invalid Input')

        async with ctx.channel.typing():
            challengeEmbed = NaWSearch.challenge(faction)
            author: discord.Member = ctx.message.author
            ignore = 4  # Default ignore for challenge embed

            # Spell rewards need special formatting
            if faction[-1:] == "R":
                title = f'**{challengeEmbed[1]}**'
                ignore = 3  # Changes to 3 if challenge is specifically a reward
            else:
                title = f'**{challengeEmbed[2]} : {challengeEmbed[1]}**'

            embed = discord.Embed(title=title, colour=discord.Colour(color), timestamp=datetime.datetime.utcnow()) \
                .set_footer(text="http://musicfamily.org/realm/Challenges/",
                            icon_url="http://musicfamily.org/realm/Factions/picks/RealmGrinderGameRL.png") \
                .set_thumbnail(url=challengeEmbed[0]) \
                .set_author(name=author, icon_url=author.avatar_url)

            if faction == "MercenaryMCR":
                return await ctx.send(
                    'This challenge reward is disabled for a bit due to the embed being too large. See: http://musicfamily.org/realm/Challenges/')

            # Ignore the first 4 fields and create the rest
            for line in challengeEmbed[ignore:]:
                newline = line.split(": ")
                embed.add_field(name=f'**{newline[0]}**', value=newline[1], inline=False)

        await ctx.send(embed=embed)

    @commands.command(aliases=alias["research"])
    async def research(self, ctx, researchName=None):
        """Retrieves Research upgrade from Not-a-Wiki"""
        if researchName in ['help', 'Help'] or researchName == None:
            description = "**.research <research>**\n**Aliases: **" + ', '.join(
                alias["research"]) + "\n\nRetrieves the " \
                                     "Research info from Not-a-Wiki in an embed displaying name, cost, formula, and effect." \
                                     "\n\nAcceptable inputs are only using research branch + number (i.e. S10, C340, E400)."
            emoji = discord.utils.get(ctx.guild.emojis, name="SuggestionMaster")
            embed = discord.Embed(title=f"{emoji}  Research", description=description, colour=self.color)
            return await ctx.send(embed=embed)
        image = ''

        # Capitalizing researchName, adding check and importing the research dict
        researchName = researchName.upper()
        check = False

        # Checks if first letter is an alphabet and the input after 0th index are digits
        if researchName[0].isalpha() and researchName[1:].isdigit():
            for key, value in FactionUpgrades.researchBranchesdict.items():
                if key[0] == researchName[0]:
                    image = value
                    check = True

        if not check:
            raise Exception("Invalid Input")

        async with ctx.channel.typing():
            researchEmbed = NaWSearch.research(researchName)

            # data[0] and data[2] returns the shorthand research and the name of research
            title = f'{researchEmbed[0]} - {researchEmbed[2]}'
            author: discord.Member = ctx.message.author

            embed = discord.Embed(title=title, description=researchEmbed[1], colour=discord.Colour.dark_gold())
            embed.set_footer(text="http://musicfamily.org/realm/Researchtree/",
                             icon_url="http://musicfamily.org/realm/Factions/picks/RealmGrinderGameRL.png")
            embed.set_thumbnail(url=image)
            embed.set_author(name=author, icon_url=author.avatar_url)

            # Cleaning the list
            for line in researchEmbed[3:]:
                line = line.strip()
                line = line.split(": ")
                embed.add_field(name=f'**{line[0]}**', value=line[1], inline=False)

        await ctx.send(embed=embed)

    @commands.command(aliases=alias['lineage'])
    async def lineage(self, ctx: commands.Context, faction=None, number=None):
        if (faction is None and number is None) or faction == "help":
            description = "**.lineage <faction> <perk>**\n**Aliases: **" + ', '.join(
                alias["lineage"]) + "\n\nRetrieves the " \
                                    "Lineage info from Not-a-Wiki in an embed displaying name, cost, formula, and effect. Also includes challenges." \
                                    "\n\nAcceptable inputs include full or shortened faction names, plus the number of perk (can be left empty to get base effect)." \
                                    "\n\nExample: .lineage Fairy, .line Dwarf 4"
            emoji = discord.utils.get(ctx.guild.emojis, name="SuggestionMaster")
            embed = discord.Embed(title=f"{emoji}  Research", description=description, colour=self.color)
            return await ctx.send(embed=embed)

        if len(faction) == 2:
            faction = faction.upper()
            colour = FactionUpgrades.getFactionColour(faction)
            faction = FactionUpgrades.getFactionNameFull(faction)
            if not faction:
                raise Exception('Invalid Input')
        else:
            faction = faction.lower()
            faction = faction.capitalize()
            colour = FactionUpgrades.getFactionColour(faction)

        # TODO: Add "p" as part of 1st parameter

        # nobody calls elf/dwarf "Elven/Dwarven", it's not hip
        if faction == 'Elf':
            faction = 'Elven'
        elif faction == 'Dwarf':
            faction = 'Dwarven'

        async with ctx.channel.typing():
            lineageEmbed = NaWSearch.lineage(faction, number)

            title = f'{lineageEmbed[1]}'
            author: discord.Member = ctx.message.author

            embed = discord.Embed(title=title, colour=discord.Colour(colour))
            embed.set_footer(text="http://musicfamily.org/realm/Lineages/",
                             icon_url="http://musicfamily.org/realm/Factions/picks/RealmGrinderGameRL.png") \
                 .set_thumbnail(url=lineageEmbed[0]) \
                 .set_author(name=author, icon_url=author.avatar_url)

            for line in lineageEmbed[2:]:
                line = line.split(": ")
                embed.add_field(name=f'**{line[0]}**', value=line[1], inline=False)

        await ctx.send(embed=embed)

    @commands.command(aliases=alias["artifact"])
    async def artifact(self, ctx: commands.Context, *, artifact=None):
        if (artifact is None) or artifact == "help":
            description = "**.artifact <keyword>**\n**Aliases: **" + ', '.join(alias["artifact"]) + "\n\nRetrieves the " \
                          "Artifact info from Not-a-Wiki in an embed displaying name, cost, formula, and effect(s) given a keyword. " \
                          "If there are multiple artifacts, they will be listed instead and you'll be asked to refine the search a bit more. " \
                          "Acronyms for certain artifacts are also accepted, i.e. KYE 1 for Know Your Enemy, Part 1, but not all artifacts have them. Feel free to suggest more!" \
                          "\n\nExample: .artifact Silk Cloth, .art core, .a statue"
            emoji = discord.utils.get(ctx.guild.emojis, name="SuggestionMaster")
            embed = discord.Embed(title=f"{emoji}  Artifact", description=description, colour=self.color)
            return await ctx.send(embed=embed)

        # Mostly because letters are really easy to figure, and could arise problems. Best to do this way
        if len(artifact) == 1:
            raise Exception("Invalid Input")

        async with ctx.channel.typing():
            artifactEmbed, check = NaWSearch.artifactSearch(artifact)

            if len(artifactEmbed) == 0:
                raise Exception("Invalid Input")

            if not check:
                title = "Searching for: " + artifact
                description = 'Your search found multiple results. Try refining your search a bit more further.'
                colour = discord.Colour.teal()
                author: discord.Member = ctx.message.author

                embed = discord.Embed(title=title, description=description, colour=colour) \
                    .set_footer(text="http://musicfamily.org/realm/Artifacts/",
                                icon_url="http://musicfamily.org/realm/Factions/picks/RealmGrinderGameRL.png") \
                    .set_author(name=author, icon_url=author.avatar_url)

                str = ""
                for line in artifactEmbed:
                    str += f'`{line}`\n'

                embed.add_field(name="Possible Artifacts", value=str)

            else:
                title = artifactEmbed[1]
                image = artifactEmbed[0]
                colour = discord.Colour.teal()
                author: discord.Member = ctx.message.author
                for line in artifactEmbed:
                    if line.startswith("Desc"):
                        description = line.split(": ")[1]
                        break

                embed = discord.Embed(title=title, description=description, colour=colour) \
                    .set_thumbnail(url=image) \
                    .set_author(name=author, icon_url=author.avatar_url)

                for line in artifactEmbed[2:]:
                    try:
                        line = line.split(": ")
                        if line[1] == description:
                            continue
                        else:
                            embed.add_field(name=f'**{line[0]}**', value=line[1], inline=False)

                    except Exception as e:
                        print(e)
                        print("Something went error with this artifact: " + artifact)
                        print(line)

        await ctx.send(embed=embed)

    @commands.command(aliases=alias["bloodline"])
    async def bloodline(self, ctx: commands.Context, faction=None):
        if faction in ['help', 'Help'] or faction == None:
            emoji = discord.utils.get(ctx.guild.emojis, name="SuggestionMaster")
            description = "**.bloodline <faction>**\n**Aliases: **" + ', '.join(alias["bloodline"]) + \
                          "\n\nRetrieves the Bloodline info from the wiki. " \
                          "<faction> inputs can be using two-letter Mercenary Template, or the full Faction name. " \
                          "\n\nExamples: .bloodline Fairy, .bl AR "
            embed = discord.Embed(title=f"{emoji}  Bloodline", description=description, colour=self.color)
            return await ctx.send(embed=embed)

        if len(faction) == 2:
            faction = faction.upper()
            faction = FactionUpgrades.getFactionNameFull(faction)
            if faction is None:
                raise Exception("Invalid Input")
            color = FactionUpgrades.getFactionColour(faction)
        else:
            faction = faction.lower()
            faction = faction.capitalize()
            if faction == "Dwarven":
                color = FactionUpgrades.getFactionColour("Dwarf")
            elif faction == "Elven":
                color = FactionUpgrades.getFactionColour("Elf")
            else:
                color = FactionUpgrades.getFactionColour(faction)

        if faction in ["EL", "Elf"]:
            faction = "Elven"
        if faction == "Dwarven":
            faction = "Dwarf"

        async with ctx.channel.typing():
            bloodlineEmbed = NaWSearch.bloodline(faction)
            author: discord.Member = ctx.message.author

            embed = discord.Embed(title=bloodlineEmbed[1] + " Bloodline", colour=discord.Colour(color)) \
                .set_footer(text="http://musicfamily.org/realm/Bloodline/",
                            icon_url="http://musicfamily.org/realm/Factions/picks/RealmGrinderGameRL.png") \
                .set_author(name=author, icon_url=author.avatar_url) \
                .set_thumbnail(url=bloodlineEmbed[0])

            for line in bloodlineEmbed[2:]:
                try:
                    line = line.split(": ")
                    embed.add_field(name=f'**{line[0]}**', value=line[1], inline=False)
                except Exception as e:
                    print(e)

        await ctx.send(embed=embed)

    @challenge.error
    @research.error
    @lineage.error
    @artifact.error
    @bloodline.error
    async def universal_error(self, ctx, error):
        if isinstance(error, Exception):
            title = " :exclamation:  Command Error!"
            description = "The parameters you used are not found in the list. Please try again."
            print(error)
            print("Sent by: " + str(ctx.message.author) + "\nMessage: " + str(ctx.message.content) + "\nDate: " + str(
                datetime.datetime.utcnow()))
            print("-----------")
            embed = discord.Embed(title=title, description=description, colour=discord.Colour.red())
            return await ctx.send(embed=embed)


####
def setup(bot):
    bot.add_cog(Notawiki(bot))
