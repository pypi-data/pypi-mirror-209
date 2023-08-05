import json
from .dtos.alias_key_dto import AliasKeyDto
from .constants.constants import UPDATE_ALIAS_API, DELETE_ALIAS_API
from .https.http_caller import HttpCaller
from .handler_response_http import HandlerResponseHttp

class ManageAliasKeyRepository(HandlerResponseHttp):
    def __init__(self, http_caller:HttpCaller):
        self.http_caller=http_caller

    def update_alias(self, alias_key_dto: AliasKeyDto):
        input = json.dumps(alias_key_dto.__dict__)
        result = self.http_caller.post(UPDATE_ALIAS_API, input)
        response_body = json.loads(result)
        return self.handler_response(response_body)

    def delete_alias(self, alias_key_dto: AliasKeyDto):
        input = json.dumps(alias_key_dto.__dict__)
        result = self.http_caller.post(DELETE_ALIAS_API, input)
        response_body = json.loads(result)
        return self.handler_response(response_body)

    def handler_response_success(self, result):
        return None if result['data'] is None else result['data'][0]