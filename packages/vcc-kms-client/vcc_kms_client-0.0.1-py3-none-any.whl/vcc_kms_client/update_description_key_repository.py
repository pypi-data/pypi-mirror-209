import json
from .dtos.description_key_dto import DescriptionKeyDto
from .constants.constants import UPDATE_DESCRIPTION_KEY_API
from .https.http_caller import HttpCaller
from .handler_response_http import HandlerResponseHttp

class UpdateDescriptionKeyRepository(HandlerResponseHttp):

    def __init__(self, http_caller:HttpCaller):
        self.http_caller=http_caller

    def update_description(self, description_key_dto: DescriptionKeyDto):
        input = json.dumps(description_key_dto.__dict__)
        result = self.http_caller.post(UPDATE_DESCRIPTION_KEY_API, input)
        response_body = json.loads(result)
        return self.handler_response(response_body)

    def handler_response_success(self, result):
        return None if result['data'] is None else result['data'][0]