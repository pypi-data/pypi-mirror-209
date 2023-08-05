from .models import content_type
from .models.decrypt_request import DecryptRequest
from .models.decrypt_result import DecryptResult
from .dtos.decrypt_dto import DecryptDto
from .decrypt_repository import DecryptRepository
from .https.http_caller import HttpCaller
from .models import action

class DecryptService:
    def __init__(self, http_caller: HttpCaller):
        self.http_caller = http_caller

    def decrypt(self, request: DecryptRequest):
        decrypt_dto = DecryptDto(request.key_id,
                                 request.input if request.content_type == content_type.SINGLE_STRING else None,
                                 request.input if request.content_type == content_type.LIST_STRING else None,
                                 request.input if request.content_type == content_type.LIST_JSON_OBJECT else None,
                                 action.DECRYPT,
                                 request.content_type)
        decrypt_repository = DecryptRepository(self.http_caller)
        decrypt_dto = decrypt_repository.decrypt(decrypt_dto)

        output = None
        if request.content_type == content_type.SINGLE_STRING:
            output = decrypt_dto['text']
        elif request.content_type == content_type.LIST_STRING:
            output = decrypt_dto['texts']
        elif request.content_type == content_type.LIST_JSON_OBJECT:
            output = decrypt_dto['jsons']

        return DecryptResult(decrypt_dto['keyId'], output)

