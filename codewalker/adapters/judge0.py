import aiohttp
class Judge0:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_submission(self, session: aiohttp.ClientSession(), lang: int, code: str, base64: bool=False, stdin: str=None, expected_output: str=None):
        return 0