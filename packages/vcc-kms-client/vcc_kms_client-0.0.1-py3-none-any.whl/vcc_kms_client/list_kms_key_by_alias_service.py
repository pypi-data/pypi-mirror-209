from .models.kms_key import KMSKey
from .models.list_kms_key_by_alias_request import ListKMSKeyByAliasRequest
from .models.list_kms_key_by_alias_result import ListKMSKeyByAliasResult
from .list_kms_key_repository import ListKMSKeyRepository
from .https.http_caller import HttpCaller

class ListKMSKeyByAliasService:
    def __init__(self, http_caller: HttpCaller):
        self.http_caller = http_caller

    def list_kms_key_by_alias(self, request: ListKMSKeyByAliasRequest):
        list_kms_key_repository = ListKMSKeyRepository(self.http_caller)
        kms_key_dtos = list_kms_key_repository.get_by_alias(request.alias, request.limit, request.offset)
        keys = []
        for kms_key_dto in kms_key_dtos:
            keys.append(KMSKey(kms_key_dto['id'], kms_key_dto['description'], kms_key_dto['alias'],
                               kms_key_dto['state'], kms_key_dto['algorithm']))

        return ListKMSKeyByAliasResult(keys, request.alias)
