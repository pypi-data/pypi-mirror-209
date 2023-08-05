import json
from .dtos.sign_dto import SignDto
from .constants.constants import SIGN_API
from .https.http_caller import HttpCaller
from .handler_response_http import HandlerResponseHttp

class SignRepository(HandlerResponseHttp):
    def __init__(self, http_caller: HttpCaller):
        self.http_caller = http_caller

    def sign(self, sign_dto: SignDto):
        input = json.dumps(sign_dto.__dict__)
        result = self.http_caller.post(SIGN_API, input)
        response_body = json.loads(result)
        return self.handler_response(response_body)

    def handler_response_success(self, result):
        return None if result['data'] is None else result['data'][0]
