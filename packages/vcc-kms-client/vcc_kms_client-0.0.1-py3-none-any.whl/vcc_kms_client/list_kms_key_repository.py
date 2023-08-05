import json
import urllib.parse
from .constants.constants import GET_KEY_BY_ALIAS_API, LIST_KEY_API
from .https.http_caller import HttpCaller
from .handler_response_http import HandlerResponseHttp

class ListKMSKeyRepository(HandlerResponseHttp):

    def __init__(self, http_caller: HttpCaller):
        self.http_caller = http_caller

    def get_by_alias(self, alias, limit, offset):
        alias = urllib.parse.quote(alias.encode('utf8'))
        params = {}
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset

        result = self.http_caller.get(api=GET_KEY_BY_ALIAS_API + '/' + alias, params=params)
        response_body = json.loads(result)
        return self.handler_response(response_body)

    def list(self, limit, offset):

        params = {}
        if limit is not None:
            params['limit'] = limit
        if offset is not None:
            params['offset'] = offset

        result = self.http_caller.get(api=LIST_KEY_API, params=params)
        response_body = json.loads(result)
        return self.handler_response(response_body)

    def handler_response_success(self, result):
        return result['data']
