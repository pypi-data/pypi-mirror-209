import json
from .constants.constants import GET_KEY_BY_ID_API
from .https.http_caller import HttpCaller
from .handler_response_http import HandlerResponseHttp

class GetKMSKeyRepository(HandlerResponseHttp):

    def __init__(self, http_caller: HttpCaller):
        self.http_caller = http_caller

    def get_by_id(self, key_id, action):
        headers = {'action': action}
        result = self.http_caller.get(GET_KEY_BY_ID_API + '/' + key_id, headers)
        response_body = json.loads(result)
        return self.handler_response(response_body)

    def handler_response_success(self, result):
        return None if result['data'] is None else result['data'][0]
