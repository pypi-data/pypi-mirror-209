import os
import random
import aiohttp
import asyncio
import json


class Bard:
    HEADERS = {
        "Host": "bard.google.com",
        "X-Same-Domain": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Origin": "https://bard.google.com",
        "Referer": "https://bard.google.com/",
    }

    session = None

    def __init__(self, token=None, timeout=20, proxies=None):
        self.token = token or os.getenv("_BARD_API_KEY")
        self.timeout = timeout
        self.proxies = proxies
        self._reqid = random.randint(10000, 99999)
        self.conversation_id = ""
        self.response_id = ""
        self.choice_id = ""
        self.SNlM0e = None

    async def create_session(self):
        return aiohttp.ClientSession()

    async def initialize(self):
        if not self.token or self.token[-1] != ".":
            raise ValueError("__Secure-1PSID value must end with a single dot. Enter the correct __Secure-1PSID value.")
        if Bard.session is None:
            Bard.session = await self.create_session()

        resp = await Bard.session.get(
            "https://bard.google.com/",
            timeout=self.timeout,
            proxy=self.proxies,
            headers=self.HEADERS,
            cookies={"__Secure-1PSID": self.token},
        )
        resp.raise_for_status()
        resp_text = await resp.text()
        snim0e_start = resp_text.find('SNlM0e":"')
        if snim0e_start == -1:
            raise ValueError("SNlM0e value not found in the response. Check the __Secure-1PSID value.")
        snim0e_start += 9
        snim0e_end = resp_text.find('"', snim0e_start)
        if snim0e_end == -1:
            raise ValueError("SNlM0e value not found in the response. Check the __Secure-1PSID value.")
        self.SNlM0e = resp_text[snim0e_start:snim0e_end]

    def get_session(self):
        if Bard.session is None:
            loop = asyncio.get_event_loop()
            Bard.session = loop.run_until_complete(self.create_session())
        return Bard.session

    async def get_answer(self, input_text):
        session = self.get_session()
        params = {
            "bl": "boq_assistant-bard-web-server_20230419.00_p1",
            "_reqid": str(self._reqid),
            "rt": "c",
        }
        input_text_struct = [
            [input_text],
            None,
            [self.conversation_id, self.response_id, self.choice_id],
        ]
        data = {
            "f.req": [None, json.dumps(input_text_struct)],
            "at": self.SNlM0e,
        }

        async with session.post(
            "https://bard.google.com/_/BardChatUi/data/assistant.lamda.BardFrontendService/StreamGenerate",
            params=params,
            json=data,
            timeout=self.timeout,
            proxy=self.proxies,
            headers=self.HEADERS,
        ) as resp:
            resp.raise_for_status()
            resp_json = await resp.json()
            resp_dict = resp_json[0][2]

            if not resp_dict:
                return {"content": f"Response Error: {resp.content}."}
            parsed_answer = json.loads(resp_dict)
            bard_answer = {
                "content": parsed_answer[0][0],
                "conversation_id": parsed_answer[1][0],
                "response_id": parsed_answer[1][1],
                "factualityQueries": parsed_answer[3],
                "textQuery": parsed_answer[2][0] if parsed_answer[2] else "",
                "choices": [{"id": i[0], "content": i[1]} for i in parsed_answer[4]],
            }
            self.conversation_id, self.response_id, self.choice_id = (
                bard_answer["conversation_id"],
                bard_answer["response_id"],
                bard_answer["choices"][0]["id"],
            )
            self._reqid += 100000

            return bard_answer
