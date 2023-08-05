import json
from .dtos.decrypt_dto import DecryptDto
from .constants.constants import DECRYPT_API, DECRYPT_WITH_DATA_KEY_API, DECRYPT_WITH_DATA_KEY_PAIR_API
from .https.http_caller import HttpCaller
from .handler_response_http import HandlerResponseHttp

class DecryptRepository(HandlerResponseHttp):
    def __init__(self, http_caller:HttpCaller):
        self.http_caller=http_caller

    def decrypt(self, decrypt_dto: DecryptDto):
        input = json.dumps(decrypt_dto.__dict__)
        result = self.http_caller.post(DECRYPT_API, input)
        response_body = json.loads(result)
        return self.handler_response(response_body)

    def decrypt_with_data_key(self, decrypt_dto: DecryptDto):
        input = json.dumps(decrypt_dto.__dict__)
        result = self.http_caller.post(DECRYPT_WITH_DATA_KEY_API, input)
        response_body = json.loads(result)
        return self.handler_response(response_body)

    def decrypt_with_data_key_pair(self, decrypt_dto: DecryptDto):
        input = json.dumps(decrypt_dto.__dict__)
        result = self.http_caller.post(DECRYPT_WITH_DATA_KEY_PAIR_API, input)
        response_body = json.loads(result)
        return self.handler_response(response_body)

    def handler_response_success(self, result):
        return None if result['data'] is None else result['data'][0]
