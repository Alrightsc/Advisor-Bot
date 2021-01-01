from discord.ext import commands

import discord

alias = {
    "upgrade": ["upg", "up", "u", "upgrade"],
    "challenge": ["ch", "c", "challenge"],
    "research": ["r", "res", "research"],
    "lineage": ["lineage", "line", "l"],
    "artifact": ["artifact", "art", "a"],
    "bloodline": ["bloodline", "bl", "b"],
    "set": ["set", "s"]
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
                          "**help** - help <command> below also gets more info about that command" \
                          "\n**artifact** (art, a) - Searches and retrieves info for an Artifact" \
                          "\n**bloodline** (bl, b) - Retrieves info for a faction Bloodline" \
                          "\n**challenge** (ch, c) - Retrieves info for a faction Challenge" \
                          "\n**lineage** (line, l) - Retrieves info for a specific Lineage" \
                          "\n**research** (res, r) - Retrieves info for a Research upgrade" \
                          "\n**set** (s) - Retrieves info for an Artifact Set" \
                          "\n**upgrade** (upg, up, u) - Retrieves info for a Faction-only upgrade"
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

        if cmd in alias["artifact"]:
            description = "**.artifact <keyword>**\n**Aliases: **" + ', '.join(alias["artifact"]) + "\n\nRetrieves the " \
                          "Artifact info from Not-a-Wiki in an embed displaying name, cost, formula, and effect(s) given a keyword. " \
                          "If there are multiple artifacts, they will be listed instead and you'll be asked to refine the search a bit more." \
                          "\n\nExample: .artifact Silk Cloth, .art core, .a statue"
            emoji = discord.utils.get(ctx.guild.emojis, name="SuggestionMaster")
            embed = discord.Embed(title=f"{emoji}  Artifact", description=description, colour=self.color)
            return await ctx.send(embed=embed)

        if cmd in alias["bloodline"]:
            description = "**.bloodline <faction>**\n**Aliases: **" + ', '.join(alias["bloodline"]) + \
                          "\n\nRetrieves the Bloodline info from the wiki. " \
                          "<faction> inputs can be using two-letter Mercenary Template, or the full Faction name. " \
                          "\n\nExamples: .bloodline Fairy, .bl AR "
            emoji = discord.utils.get(ctx.guild.emojis, name="SuggestionMaster")
            embed = discord.Embed(title=f"{emoji}  Bloodline", description=description, colour=self.color)
            return await ctx.send(embed=embed)

        if cmd in alias["set"]:
            emoji = discord.utils.get(ctx.guild.emojis, name="SuggestionMaster")
            description = "**.set <faction>**\n**Aliases: **" + ', '.join(alias["set"]) + \
                          "\n\nRetrieves the Artifact Set info from the wiki. " \
                          "<faction> inputs can be using two-letter Mercenary Template, or the full Faction name. " \
                          "\n\nExamples: .set Merc, .s UD "
            embed = discord.Embed(title=f"{emoji} Artifact Set", description=description, colour=self.color)
            return await ctx.send(embed=embed)

####
def setup(bot):
    bot.add_cog(Help(bot))
