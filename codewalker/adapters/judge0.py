import aiohttp
import string
import base64

class Judge0:
    def __init__(self, *args, **kwargs):
        self.base_url_submit = 'https://api.judge0.com/submissions?wait=true'
        super().__init__(*args, **kwargs)
    
    async def add_submission(self, session: aiohttp.ClientSession(), lang: int, code: str, stdin: str="", expected_output: str="") -> aiohttp.ClientResponse:
        """
        add_submission - Submits code to Judge0 for a run.

        Returns an instance of `aiohttp.ClientResponse`.

        Arguments:

        session (aiohttp.ClientSession) - A aiohttp ClientSession to make the submission.

        lang (int) - A language ID (full chart available at api.judge0.com)

        code (str) - The code that Judge0 should run.

        stdin (str) - Optional argument that allows you to provide input to your program.

        expected_output (str) - Optional argument that allows you to require a specific output otherwise the run will fail.
        """
        # judge0 requires that if any unprintable characters are used
        # that the code be submitted in base64 for some ungodly reason
        # you have to encode 3 things if base64 is required btw
        # code, stdin, and expected_output
        filtered_code = filter(lambda x: x in string.printable, code)
        if code != filtered_code:
            submit_url = self.base_url_submit + '&base64_encoded=true'
            base64 = True
        else:
            submit_url = self.base_url_submit
            base64 = False
        body = {
            "source_code": base64.b64encode(b'{}'.format(code)) if base64 is True else code,
            "language_id": lang,
            "stdin": base64.b64encode(b'{}'.format(stdin)) if base64 is True else stdin,
            "expected_output": base64.b64encode(b'{}'.format(expected_output)) if base64 is True else expected_output
        }
        request = await session.post(submit_url, json=body)
        return request