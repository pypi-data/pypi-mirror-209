from .models.update_description_key_request import UpdateDescriptionKeyRequest
from .models.update_description_key_result import UpdateDescriptionKeyResult
from .models import action
from .dtos.description_key_dto import DescriptionKeyDto
from .update_description_key_repository import UpdateDescriptionKeyRepository
from .https.http_caller import HttpCaller

class UpdateDescriptionKeyService:
    def __init__(self, http_caller: HttpCaller):
        self.http_caller = http_caller

    def update_description_key(self, request: UpdateDescriptionKeyRequest):
        description_key_dto = DescriptionKeyDto(request.key_id, request.description, action.UPDATE_DESCRIPTION_KEY)

        update_description_key_repository = UpdateDescriptionKeyRepository(self.http_caller)
        description_key_dto = update_description_key_repository.update_description(description_key_dto)
        return UpdateDescriptionKeyResult(description_key_dto['keyId'], description_key_dto['description'])