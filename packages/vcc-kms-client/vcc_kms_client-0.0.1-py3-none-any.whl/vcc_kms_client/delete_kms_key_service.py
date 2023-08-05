from .models import key_state
from .models.delete_kms_key_request import DeleteKMSKeyRequest
from .models.delete_kms_key_result import DeleteKMSKeyResult
from .models import action
from .dtos.change_state_dto import ChangeStateDto
from .change_state_kms_key_repository import ChangeStateKMSKeyRepository
from .https.http_caller import HttpCaller

class DeleteKMSKeyService:
    def __init__(self, http_caller: HttpCaller):
        self.http_caller = http_caller

    def delete_kms_key(self, request: DeleteKMSKeyRequest):
        change_state_dto = ChangeStateDto(
            request.key_id,
            key_state.SCHEDULED_DELETION,
            action.DELETE_KEY
        )

        change_state_kms_key_repository = ChangeStateKMSKeyRepository(self.http_caller)
        change_state_dto = change_state_kms_key_repository.change_state_kms_key(change_state_dto)

        return DeleteKMSKeyResult(change_state_dto['keyId'], change_state_dto['state'])