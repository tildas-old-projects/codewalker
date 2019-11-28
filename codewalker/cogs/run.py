import lifesaver
from codewalker.adapters.judge0 import Judge0
from codewalker.converters import languagedetect

class RunCode(lifesaver.Cog):
    def __init__(self, bot):
        super().__init__(bot)
        self.bot = bot
        self.judgeapi = Judge0()
    
    @lifesaver.command()
    async def run(self, ctx, lang, code: str):
        submission = self.judgeapi.add_submission(self.bot.session, languagedetect.detect(lang), code)
        return await ctx.send('wip')

def setup(bot):
    bot.add_cog(RunCode(bot))