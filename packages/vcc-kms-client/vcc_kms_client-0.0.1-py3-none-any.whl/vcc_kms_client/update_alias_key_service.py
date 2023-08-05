from .models.update_alias_key_request import UpdateAliasKeyRequest
from .models.update_alias_key_result import UpdateAliasKeyResult
from .models import action
from .dtos.alias_key_dto import AliasKeyDto
from .manage_alias_key_repository import ManageAliasKeyRepository
from .https.http_caller import HttpCaller

class UpdateAliasKeyService:
    def __init__(self, http_caller: HttpCaller):
        self.http_caller = http_caller

    def update_alias_key(self, request: UpdateAliasKeyRequest):
        alias_key_dto = AliasKeyDto(request.key_id, request.alias, action.UPDATE_ALIAS)

        manage_alias_key_repository = ManageAliasKeyRepository(self.http_caller)
        alias_key_dto = manage_alias_key_repository.update_alias(alias_key_dto)
        return UpdateAliasKeyResult(alias_key_dto['keyId'], alias_key_dto['alias'])
