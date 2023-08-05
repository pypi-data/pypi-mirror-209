from .models.generate_data_key_pair_request import GenerateDataKeyPairRequest
from .models.generate_data_key_pair_result import GenerateDataKeyPairResult
from .models import action
from .dtos.generate_data_key_dto import GenerateDataKeyDto
from .generate_data_key_repository import GenerateDataKeyRepository
from .https.http_caller import HttpCaller

class GenerateDataKeyPairService:
    def __init__(self, http_caller: HttpCaller):
        self.http_caller = http_caller

    def generate_data_key_pair(self, request:GenerateDataKeyPairRequest):
        generate_data_key_dto = GenerateDataKeyDto(request.key_id, request.algorithm, None, None, None, None, None, action.GENERATE_DATA_KEY_PAIR)
        generate_data_key_repository = GenerateDataKeyRepository(self.http_caller)
        generate_data_key_dto = generate_data_key_repository.generate_data_key_pair(generate_data_key_dto)
        return GenerateDataKeyPairResult(generate_data_key_dto['keyId'], generate_data_key_dto['algorithm'], generate_data_key_dto['encryptPrivateDataKey'], generate_data_key_dto['plaintextPrivateDataKey'], generate_data_key_dto['plaintextPublicDataKey'])