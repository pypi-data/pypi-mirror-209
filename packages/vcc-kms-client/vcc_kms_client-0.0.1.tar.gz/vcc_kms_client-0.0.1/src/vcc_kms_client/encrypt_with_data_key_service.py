from .models import content_type
from .models.encrypt_with_data_key_request import EncryptWithDataKeyRequest
from .models.encrypt_with_data_key_result import EncryptWithDataKeyResult
from .dtos.encrypt_dto import EncryptDto
from .encrypt_repository import EncryptRepository
from .https.http_caller import HttpCaller
from .models import action

class EncryptWithDataKeyService:
    def __init__(self, http_caller: HttpCaller):
        self.http_caller = http_caller

    def encrypt_with_data_key(self, request: EncryptWithDataKeyRequest):
        encrypt_dto = EncryptDto(request.key_id,
                                 request.input if request.content_type == content_type.SINGLE_STRING else None,
                                 request.input if request.content_type == content_type.LIST_STRING else None,
                                 request.input if request.content_type == content_type.LIST_JSON_OBJECT else None,
                                 request.algorithm,
                                 action.ENCRYPT_WITH_DATA_KEY,
                                 request.content_type)
        encrypt_repository = EncryptRepository(self.http_caller)
        encrypt_dto = encrypt_repository.encrypt_with_data_key(encrypt_dto)

        output = None
        if request.content_type == content_type.SINGLE_STRING:
            output = encrypt_dto['text']
        elif request.content_type == content_type.LIST_STRING:
            output = encrypt_dto['texts']
        elif request.content_type == content_type.LIST_JSON_OBJECT:
            output = encrypt_dto['jsons']

        return EncryptWithDataKeyResult(encrypt_dto['keyId'], output, encrypt_dto['algorithm'])

