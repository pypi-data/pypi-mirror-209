from .models.sign_request import SignRequest
from .models.sign_result import SignResult
from .dtos.sign_dto import SignDto
from .sign_repository import SignRepository
from .https.http_caller import HttpCaller
from .models import action

class SignService:
    def __init__(self, http_caller: HttpCaller):
        self.http_caller = http_caller

    def sign(self, request: SignRequest):
        sign_dto = SignDto(request.key_id, request.message, action.SIGN, request.sign_algorithm)
        sign_repository = SignRepository(self.http_caller)
        sign_dto = sign_repository.sign(sign_dto)

        return SignResult(sign_dto['keyId'], sign_dto['message'], sign_dto['signAlgorithm'])

