import json
from .dtos.generate_data_key_dto import GenerateDataKeyDto
from .https.http_caller import HttpCaller
from .constants.constants import GENERATE_DATA_KEY_API, GENERATE_DATA_KEY_PAIR_API
from .handler_response_http import HandlerResponseHttp

class GenerateDataKeyRepository(HandlerResponseHttp):
    def __init__(self, http_caller:HttpCaller):
        self.http_caller = http_caller

    def generate_data_key(self, generate_data_key_dto: GenerateDataKeyDto):
        input = json.dumps(generate_data_key_dto.__dict__)
        result = self.http_caller.post(GENERATE_DATA_KEY_API, input)
        response_body = json.loads(result)
        return self.handler_response(response_body)

    def generate_data_key_pair(self, generate_data_key_dto: GenerateDataKeyDto):
        input = json.dumps(generate_data_key_dto.__dict__)
        result = self.http_caller.post(GENERATE_DATA_KEY_PAIR_API, input)
        response_body = json.loads(result)
        return self.handler_response(response_body)


    def handler_response_success(self, result):
        return None if result['data'] is None else result['data'][0]




