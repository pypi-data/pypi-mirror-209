from .models.internal_server_exception import InternalServerException
from .models.unauthorized_exception import UnauthorizedException
from .models.invalid_request_exception import InvalidRequestException
from .models.invalid_data_exception import InvalidDataException
from .models.not_found_exception import NotFoundException
from .models.code import *

class HandlerResponseHttp:
    def handler_response(self, response_body):
        if response_body['code']==UNAUTHORIZED_REQUEST:
            raise UnauthorizedException(response_body['message'])
        elif response_body['code']==BAD_REQUEST:
            raise InvalidRequestException(response_body['message'])
        elif response_body['code']==DATA_ERROR:
            raise InvalidDataException(response_body['message'])
        elif response_body['code']==INTERNAL_ERROR:
            raise InternalServerException(response_body['message'])
        elif response_body['code']==NOT_FOUND:
            raise NotFoundException(response_body['message'])
        elif response_body['code']==SUCCESS:
            return self.handler_response_success(response_body['result'])
        else:
            raise Exception(response_body['message'])

    def handler_response_success(self, result):
        pass