import json
from .dtos.kms_key_dto import KMSKeyDto
from .https.http_caller import HttpCaller
from .constants.constants import CREATE_KEY_API
from .handler_response_http import HandlerResponseHttp

class CreateKMSKeyRepository(HandlerResponseHttp):
    def __init__(self, http_caller:HttpCaller):
        self.http_caller = http_caller

    def create_kms_key(self, kms_key_dto: KMSKeyDto):
        input = json.dumps(kms_key_dto.__dict__)
        result = self.http_caller.post(CREATE_KEY_API, input)
        response_body = json.loads(result)
        return self.handler_response(response_body)


    def handler_response_success(self, result):
        return None if result['data'] is None else result['data'][0]




