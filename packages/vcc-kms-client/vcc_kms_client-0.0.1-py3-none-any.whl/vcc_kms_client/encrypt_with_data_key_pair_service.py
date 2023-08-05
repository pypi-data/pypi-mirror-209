from .models import content_type
from .models.encrypt_with_data_key_pair_request import EncryptWithDataKeyPairRequest
from .models.encrypt_with_data_key_pair_result import EncryptWithDataKeyPairResult
from .dtos.encrypt_dto import EncryptDto
from .encrypt_repository import EncryptRepository
from .https.http_caller import HttpCaller
from .models import action

class EncryptWithDataKeyPairService:
    def __init__(self, http_caller: HttpCaller):
        self.http_caller = http_caller

    def encrypt_with_data_key_pair(self, request: EncryptWithDataKeyPairRequest):
        encrypt_dto = EncryptDto(request.key_id,
                                 request.input if request.content_type == content_type.SINGLE_STRING else None,
                                 request.input if request.content_type == content_type.LIST_STRING else None,
                                 request.input if request.content_type == content_type.LIST_JSON_OBJECT else None,
                                 request.algorithm,
                                 action.ENCRYPT_WITH_DATA_KEY_PAIR,
                                 request.content_type)
        encrypt_repository = EncryptRepository(self.http_caller)
        encrypt_dto = encrypt_repository.encrypt_with_data_key_pair(encrypt_dto)

        output = None
        if request.content_type == content_type.SINGLE_STRING:
            output = encrypt_dto['text']
        elif request.content_type == content_type.LIST_STRING:
            output = encrypt_dto['texts']
        elif request.content_type == content_type.LIST_JSON_OBJECT:
            output = encrypt_dto['jsons']

        return EncryptWithDataKeyPairResult(encrypt_dto['keyId'], output, encrypt_dto['algorithm'])

