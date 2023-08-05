import json
from .dtos.encrypt_dto import EncryptDto
from .constants.constants import ENCRYPT_WITH_DATA_KEY_API, ENCRYPT_API, ENCRYPT_WITH_DATA_KEY_PAIR_API
from .https.http_caller import HttpCaller
from .handler_response_http import HandlerResponseHttp

class EncryptRepository(HandlerResponseHttp):
    def __init__(self, http_caller:HttpCaller):
        self.http_caller=http_caller

    def encrypt(self, encrypt_dto: EncryptDto):
        input = json.dumps(encrypt_dto.__dict__)
        result = self.http_caller.post(ENCRYPT_API, input)
        response_body = json.loads(result)
        return self.handler_response(response_body)

    def encrypt_with_data_key(self, encrypt_dto: EncryptDto):
        input = json.dumps(encrypt_dto.__dict__)
        result = self.http_caller.post(ENCRYPT_WITH_DATA_KEY_API, input)
        response_body = json.loads(result)
        return self.handler_response(response_body)

    def encrypt_with_data_key_pair(self, encrypt_dto: EncryptDto):
        input = json.dumps(encrypt_dto.__dict__)
        result = self.http_caller.post(ENCRYPT_WITH_DATA_KEY_PAIR_API, input)
        response_body = json.loads(result)
        return self.handler_response(response_body)

    def handler_response_success(self, result):
        return None if result['data'] is None else result['data'][0]
