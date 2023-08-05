from .models import key_state
from .models.disable_kms_key_request import DisableKMSKeyRequest
from .models.disable_kms_key_result import DisableKMSKeyResult
from .models import action
from .dtos.change_state_dto import ChangeStateDto
from .change_state_kms_key_repository import ChangeStateKMSKeyRepository
from .https.http_caller import HttpCaller

class DisableKMSKeyService:
    def __init__(self, http_caller: HttpCaller):
        self.http_caller = http_caller

    def disable_kms_key(self, request: DisableKMSKeyRequest):
        change_state_dto = ChangeStateDto(
            request.key_id,
            key_state.DISABLED,
            action.DISABLE_KEY
        )

        change_state_kms_key_repository = ChangeStateKMSKeyRepository(self.http_caller)
        change_state_dto = change_state_kms_key_repository.change_state_kms_key(change_state_dto)

        return DisableKMSKeyResult(change_state_dto['keyId'], change_state_dto['state'])