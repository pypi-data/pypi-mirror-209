from .models.describe_kms_key_request import DescribeKMSKeyRequest
from .models.describe_kms_key_result import DescribeKMSKeyResult
from .models import action
from .get_kms_key_repository import GetKMSKeyRepository
from .https.http_caller import HttpCaller

class DescribeKMSKeyService:
    def __init__(self, http_caller:HttpCaller):
        self.http_caller = http_caller

    def describe_kms_key(self, request: DescribeKMSKeyRequest):
        get_kms_key_http_repository = GetKMSKeyRepository(self.http_caller)
        kms_key_dto = get_kms_key_http_repository.get_by_id(request.key_id, action.DESCRIBE_KEY)
        return DescribeKMSKeyResult(kms_key_dto['id'], kms_key_dto['description'], kms_key_dto['alias'],
                                  kms_key_dto['state'], kms_key_dto['algorithm'])
