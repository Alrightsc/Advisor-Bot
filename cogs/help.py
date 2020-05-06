from discord.ext import commands

import discord

alias = {
    "upgrade": ["upg", "up", "u", "upgrade"],
    "challenge": ["ch", "c", "challenge"],
    "research": ["r", "res", "research"]
}

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = discord.Colour.magenta()

    @commands.command()
    async def help(self, ctx, cmd=None):
        if cmd is None:
            title = "Advisor - Realm Grinder Bot"
            description = "Hello! I am the Royal Advisor here to help you on the path to becoming the richest king/queen" \
                          " in the realm! Use the commands below and I can help query information from Not A Wiki." \
                          "\n\nBot written by Alright#2304. Any issue or feedback can be PM'd to me directly." \
                          "\n\nNot-a-Wiki Link: http://musicfamily.org/realm/" \
                          "\nGithub link: https://github.com/Alrightsc/Advisor-Bot" \
                          "\n\n" \
                          "**help** - Default help; help <command> below also gets more info about that command" \
                          "\n**upgrade** (upg, up, u) - Retrieves info for a Faction-only upgrade" \
                          "\n**challenge** (ch, c) - Retrieves info for a faction Challenge" \
                          "\n**research** (res, r) - Retrieves info for a Research upgrade" \
                          "\n**lineage** (line, l) - Retrieves info for a specific Lineage"
            embed = discord.Embed(title=title, description=description, colour=self.color)
            return await ctx.send(embed=embed)

        if cmd in alias["research"]:
            description = "**.research <research>**\n**Aliases: **" + ', '.join(alias["research"]) + "\n\nRetrieves the " \
                    "Research info from Not-a-Wiki in an embed displaying name, cost, formula, and effect." \
                    "\n\nAcceptable inputs are only using research branch + number (i.e. S10, C340, E400)."
            emoji = discord.utils.get(ctx.guild.emojis, name="SuggestionMaster")
            embed = discord.Embed(title=f"{emoji}  Research", description=description, colour=self.color)
            return await ctx.send(embed=embed)

        if cmd in alias["challenge"]:
            emoji = discord.utils.get(ctx.guild.emojis, name="SuggestionMaster")
            description = "**.challenge <faction>**\n**Aliases: **" + ', '.join(alias["challenge"]) + "\n\nRetrieves " \
                          "challenge info from Not-a-Wiki displaying name, requirements, effects, and formulas. Valid " \
                          "inputs include using faction name and the challenge number, or r for spell challenge " \
                          "reward. Mercenary templates in place of full name can be used, adding C# or \"R\".\n\nExample: " \
                          "Fairy 2, Makers r, DGC5, DJR"
            embed = discord.Embed(title=f"{emoji}  Challenge", description=description,
                                  colour=self.color)
            return await ctx.send(embed=embed)

        if cmd in alias["upgrade"]:
            emoji = discord.utils.get(ctx.guild.emojis, name="SuggestionMaster")
            description = "**.upgrade <faction>**\n**Aliases: **" + ', '.join(alias["upgrade"]) + \
                          '\n\nRetrieves a Faction upgrade information ' \
                          'directly from Not-a-Wiki. <faction> inputs can be using two-letter Mercenary Template with ' \
                          'upgrade number, or full Faction name with an upgrade number.' \
                          '\n\n**Note:** Non-faction upgrades such as Secret Trophy upgrades are not supported!' \
                          '\n\nExamples: Fairy 7, MK10'
            embed = discord.Embed(title=f"{emoji}  Upgrade", description=description,
                                  colour=self.color)
            return await ctx.send(embed=embed)

        if cmd in alias["lineage"]:
            description = "**.lineage <faction> <perk>**\n**Aliases: **" + ', '.join(alias["lineage"]) + "\n\nRetrieves the " \
                    "Lineage info from Not-a-Wiki in an embed displaying name, cost, formula, and effect. Also includes challenges." \
                    "\n\nAcceptable inputs include full or shortened faction names, plus the number of perk (can be left empty to get base effect)." \
                    "\n\nExample: .lineage Fairy, .line Dwarf 4"
            emoji = discord.utils.get(ctx.guild.emojis, name="SuggestionMaster")
            embed = discord.Embed(title=f"{emoji}  Research", description=description, colour=self.color)
            return await ctx.send(embed=embed)

####
def setup(bot):
    bot.add_cog(Help(bot))
