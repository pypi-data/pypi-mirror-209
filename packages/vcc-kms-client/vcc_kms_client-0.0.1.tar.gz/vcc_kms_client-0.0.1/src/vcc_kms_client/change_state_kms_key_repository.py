import json
from .dtos.change_state_dto import ChangeStateDto
from .https.http_caller import HttpCaller
from .constants.constants import CHANGE_STATE_KEY_API
from .handler_response_http import HandlerResponseHttp

class ChangeStateKMSKeyRepository(HandlerResponseHttp):
    def __init__(self, http_caller:HttpCaller):
        self.http_caller = http_caller

    def change_state_kms_key(self, change_state_dto: ChangeStateDto):
        input = json.dumps(change_state_dto.__dict__)
        result = self.http_caller.post(CHANGE_STATE_KEY_API, input)
        response_body = json.loads(result)
        return self.handler_response(response_body)


    def handler_response_success(self, result):
        return None if result['data'] is None else result['data'][0]




