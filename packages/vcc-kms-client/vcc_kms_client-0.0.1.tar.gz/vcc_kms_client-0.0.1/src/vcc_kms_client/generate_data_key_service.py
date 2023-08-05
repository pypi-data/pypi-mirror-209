from .models.generate_data_key_request import GenerateDataKeyRequest
from .models.generate_data_key_result import GenerateDataKeyResult
from .models import action
from .dtos.generate_data_key_dto import GenerateDataKeyDto
from .generate_data_key_repository import GenerateDataKeyRepository
from .https.http_caller import HttpCaller

class GenerateDataKeyService:
    def __init__(self, http_caller: HttpCaller):
        self.http_caller = http_caller

    def generate_data_key(self, request:GenerateDataKeyRequest):
        generate_data_key_dto = GenerateDataKeyDto(request.key_id, request.algorithm, None, None, None, None, None, action.GENERATE_DATA_KEY)
        generate_data_key_repository = GenerateDataKeyRepository(self.http_caller)
        generate_data_key_dto = generate_data_key_repository.generate_data_key(generate_data_key_dto)
        return GenerateDataKeyResult(generate_data_key_dto['keyId'], generate_data_key_dto['algorithm'], generate_data_key_dto['plaintextSecretDataKey'], generate_data_key_dto['encryptSecretDataKey'])