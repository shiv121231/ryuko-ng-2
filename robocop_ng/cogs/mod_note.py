import discord
from discord.ext import commands
from discord.ext.commands import Cog

from robocop_ng.helpers.checks import check_if_staff
from robocop_ng.helpers.userlogs import userlog


class ModNote(Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.check(check_if_staff)
    @commands.command(aliases=["addnote"])
    async def note(self, ctx, target: discord.Member, *, note: str = ""):
        """Adds a note to a user, staff only."""
        userlog(self.bot, target.id, ctx.author, note, "notes", target.name)
        await ctx.send(f"{ctx.author.mention}: noted!")

    @commands.guild_only()
    @commands.check(check_if_staff)
    @commands.command(aliases=["addnoteid"])
    async def noteid(self, ctx, target: int, *, note: str = ""):
        """Adds a note to a user by userid, staff only."""
        userlog(self.bot, target, ctx.author, note, "notes")
        await ctx.send(f"{ctx.author.mention}: noted!")


async def setup(bot):
    await bot.add_cog(ModNote(bot))
