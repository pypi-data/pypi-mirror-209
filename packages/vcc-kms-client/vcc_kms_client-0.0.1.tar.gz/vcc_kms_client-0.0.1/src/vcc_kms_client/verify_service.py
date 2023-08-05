from .models.verify_request import VerifyRequest
from .models.verify_result import VerifyResult
from .dtos.verify_dto import VerifyDto
from .verify_repository import VerifyRepository
from .https.http_caller import HttpCaller
from .models import action

class VerifyService:
    def __init__(self, http_caller: HttpCaller):
        self.http_caller = http_caller

    def verify(self, request: VerifyRequest):
        verify_dto = VerifyDto(request.key_id, request.message, request.signature, action.VERIFY,
                               request.sign_algorithm, None)
        verify_repository = VerifyRepository(self.http_caller)
        verify_dto = verify_repository.verify(verify_dto)
        return VerifyResult(verify_dto['keyId'], verify_dto['signatureValid'], verify_dto['signAlgorithm'])
