import json
from .dtos.verify_dto import VerifyDto
from .constants.constants import VERIFY_API
from .https.http_caller import HttpCaller
from .handler_response_http import HandlerResponseHttp

class VerifyRepository(HandlerResponseHttp):
    def __init__(self, http_caller: HttpCaller):
        self.http_caller = http_caller

    def verify(self, verify_dto: VerifyDto):
        input = json.dumps(verify_dto.__dict__)
        result = self.http_caller.post(VERIFY_API, input)
        response_body = json.loads(result)
        return self.handler_response(response_body)

    def handler_response_success(self, result):
        return None if result['data'] is None else result['data'][0]