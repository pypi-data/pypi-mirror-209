from .models.delete_alias_key_request import DeleteAliasKeyRequest
from .models.delete_alias_key_result import DeleteAliasKeyResult
from .models import action
from .dtos.alias_key_dto import AliasKeyDto
from .manage_alias_key_repository import ManageAliasKeyRepository
from .https.http_caller import HttpCaller

class DeleteAliasKeyService:
    def __init__(self, http_caller: HttpCaller):
        self.http_caller = http_caller

    def delete_alias_key(self, request: DeleteAliasKeyRequest):
        alias_key_dto = AliasKeyDto(request.key_id, None, action.DELETE_ALIAS)

        manage_alias_key_repository = ManageAliasKeyRepository(self.http_caller)
        alias_key_dto = manage_alias_key_repository.delete_alias(alias_key_dto)
        return DeleteAliasKeyResult(alias_key_dto['keyId'])
