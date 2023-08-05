from .models import key_state
from .models.create_kms_key_request import CreateKMSKeyRequest
from .models.create_kms_key_result import CreateKMSKeyResult
from .dtos.kms_key_dto import KMSKeyDto
from .create_kms_key_repository import CreateKMSKeyRepository
from .https.http_caller import HttpCaller

class CreateKMSKeyService:
    def __init__(self, http_caller:HttpCaller):
        self.http_caller = http_caller

    def create_kms_key(self, request:CreateKMSKeyRequest):
        kms_key_dto = KMSKeyDto(None, request.description, request.alias, key_state.ENABLED, request.algorithm)
        create_kms_key_repository = CreateKMSKeyRepository(self.http_caller)
        kms_key_dto = create_kms_key_repository.create_kms_key(kms_key_dto)
        return CreateKMSKeyResult(kms_key_dto['id'], kms_key_dto['description'], kms_key_dto['alias'], kms_key_dto['state'], kms_key_dto['algorithm'])

