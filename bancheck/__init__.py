"""Package for BanCheck cog."""
from .bancheck import BanCheck

__red_end_user_data_statement__ = (
    "This cog does not persistently store data or metadata about users."
)


async def setup(bot):
    """Load BanCheck cog."""
    cog = BanCheck(bot)
    await cog.initialize()
    bot.add_cog(cog)
