from .auth.kms_credentials import KMSCredentials
from .models.create_kms_key_request import CreateKMSKeyRequest
from .models.decrypt_request import DecryptRequest
from .models.decrypt_with_data_key_pair_request import DecryptWithDataKeyPairRequest
from .models.decrypt_with_data_key_request import DecryptWithDataKeyRequest
from .models.delete_alias_key_request import DeleteAliasKeyRequest
from .models.delete_kms_key_request import DeleteKMSKeyRequest
from .models.describe_kms_key_request import DescribeKMSKeyRequest
from .models.disable_kms_key_request import DisableKMSKeyRequest
from .models.enable_kms_key_request import EnableKMSKeyRequest
from .models.encrypt_request import EncryptRequest
from .models.encrypt_with_data_key_pair_request import EncryptWithDataKeyPairRequest
from .models.encrypt_with_data_key_request import EncryptWithDataKeyRequest
from .models.generate_data_key_pair_request import GenerateDataKeyPairRequest
from .models.generate_data_key_request import GenerateDataKeyRequest
from .models.list_kms_key_by_alias_request import ListKMSKeyByAliasRequest
from .models.list_kms_key_request import ListKMSKeyRequest
from .models.sign_request import SignRequest
from .models.update_alias_key_request import UpdateAliasKeyRequest
from .models.update_description_key_request import UpdateDescriptionKeyRequest
from .models.verify_request import VerifyRequest
from .create_kms_key_service import CreateKMSKeyService
from .decrypt_service import DecryptService
from .decrypt_with_data_key_pair_service import DecryptWithDataKeyPairService
from .decrypt_with_data_key_service import DecryptWithDataKeyService
from .delete_alias_key_service import DeleteAliasKeyService
from .delete_kms_key_service import DeleteKMSKeyService
from .describe_kms_key_service import DescribeKMSKeyService
from .disable_kms_key_service import DisableKMSKeyService
from .enable_kms_key_service import EnableKMSKeyService
from .encrypt_service import EncryptService
from .encrypt_with_data_key_pair_service import EncryptWithDataKeyPairService
from .encrypt_with_data_key_service import EncryptWithDataKeyService
from .generate_data_key_pair_service import GenerateDataKeyPairService
from .generate_data_key_service import GenerateDataKeyService
from .list_kms_key_by_alias_service import ListKMSKeyByAliasService
from .list_kms_key_service import ListKMSKeyService
from .sign_service import SignService
from .update_alias_key_service import UpdateAliasKeyService
from .update_description_key_service import UpdateDescriptionKeyService
from .verify_service import VerifyService
from .https.http_caller import HttpCaller

class KMSClient:
    def __init__(self, credentals: KMSCredentials):
        self.http_caller=HttpCaller(credentals)

    def create_key(self, request: CreateKMSKeyRequest):
        create_kms_key_service = CreateKMSKeyService(self.http_caller)
        return create_kms_key_service.create_kms_key(request)

    def encrypt(self, request: EncryptRequest):
        encrypt_service = EncryptService(self.http_caller)
        return encrypt_service.encrypt(request)

    def decrypt(self, request: DecryptRequest):
        decrypt_service = DecryptService(self.http_caller)
        return decrypt_service.decrypt(request)

    def encrypt_with_data_key(self, request: EncryptWithDataKeyRequest):
        encrypt_with_data_key_service = EncryptWithDataKeyService(self.http_caller)
        return encrypt_with_data_key_service.encrypt_with_data_key(request)

    def encrypt_with_data_key_pair(self, request: EncryptWithDataKeyPairRequest):
        encrypt_with_data_key_pair_service = EncryptWithDataKeyPairService(self.http_caller)
        return encrypt_with_data_key_pair_service.encrypt_with_data_key_pair(request)

    def decrypt_with_data_key(self, request: DecryptWithDataKeyRequest):
        decrypt_with_data_key_service = DecryptWithDataKeyService(self.http_caller)
        return decrypt_with_data_key_service.decrypt_with_data_key(request)

    def decrypt_with_data_key_pair(self, request: DecryptWithDataKeyPairRequest):
        decrypt_with_data_key_pair_service = DecryptWithDataKeyPairService(self.http_caller)
        return decrypt_with_data_key_pair_service.decrypt_with_data_key_pair(request)

    def delete_kms_key(self, request: DeleteKMSKeyRequest):
        delete_kms_key_service = DeleteKMSKeyService(self.http_caller)
        return delete_kms_key_service.delete_kms_key(request)

    def disable_kms_key(self, request: DisableKMSKeyRequest):
        disable_kms_key_service = DisableKMSKeyService(self.http_caller)
        return disable_kms_key_service.disable_kms_key(request)

    def enable_kms_key(self, request: EnableKMSKeyRequest):
        enable_kms_key_service = EnableKMSKeyService(self.http_caller)
        return enable_kms_key_service.enable_kms_key(request)

    def update_alias_key(self, request: UpdateAliasKeyRequest):
        update_alias_key_service = UpdateAliasKeyService(self.http_caller)
        return update_alias_key_service.update_alias_key(request)

    def delete_alias_key(self, request: DeleteAliasKeyRequest):
        delete_alias_key_service = DeleteAliasKeyService(self.http_caller)
        return delete_alias_key_service.delete_alias_key(request)

    def generate_data_key(self, request: GenerateDataKeyRequest):
        generate_data_key_service = GenerateDataKeyService(self.http_caller)
        return generate_data_key_service.generate_data_key(request)

    def generate_data_key_pair(self, request: GenerateDataKeyPairRequest):
        generate_data_key_pair_service = GenerateDataKeyPairService(self.http_caller)
        return generate_data_key_pair_service.generate_data_key_pair(request)

    def update_description_key(self, request: UpdateDescriptionKeyRequest):
        update_description_key_service = UpdateDescriptionKeyService(self.http_caller)
        return update_description_key_service.update_description_key(request)

    def describe_kms_key(self, request: DescribeKMSKeyRequest):
        describe_kms_key_service = DescribeKMSKeyService(self.http_caller)
        return describe_kms_key_service.describe_kms_key(request)

    def list_key(self, request: ListKMSKeyRequest):
        list_kms_key_service = ListKMSKeyService(self.http_caller)
        return list_kms_key_service.list_kms_key(request)

    def list_key_by_alias(self, request: ListKMSKeyByAliasRequest):
        list_kms_key_by_alias_service = ListKMSKeyByAliasService(self.http_caller)
        return list_kms_key_by_alias_service.list_kms_key_by_alias(request)

    def sign(self, request: SignRequest):
        sign_service = SignService(self.http_caller)
        return sign_service.sign(request)

    def verify(self, request: VerifyRequest):
        verify_service = VerifyService(self.http_caller)
        return verify_service.verify(request)