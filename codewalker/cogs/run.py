import lifesaver

class RunCode(lifesaver.Cog):
    def __init__(self, bot):
        super().__init__(bot)
    
    @lifesaver.command()
    async def run(self, ctx, lang, code: str):
        return await ctx.send('wip')

def setup(bot):
    bot.add_cog(RunCode(bot))