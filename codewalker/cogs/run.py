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
        """
        Run code using the Judge0 API.

        NOTE: This command makes assumptions about which language version you want to use.
        If the version the bot chose for you does not work (e.g. you want Java 9), 
        look at https://api.judge0.com/languages and see if they have what you want.
        """
        submission = await self.judgeapi.add_submission(self.bot.session, languagedetect.detect(lang), code)
        result = await submission.json()
        return await ctx.send('wip')

def setup(bot):
    bot.add_cog(RunCode(bot))