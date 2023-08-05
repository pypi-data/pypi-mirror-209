from src.vcc_kms_client.auth.kms_credentials import KMSCredentials
from src.vcc_kms_client.models.update_alias_key_request import UpdateAliasKeyRequest
from src.vcc_kms_client.kms_client import KMSClient

f = open("file/security_file.json", "r")
credentals = KMSCredentials(f)
kms = KMSClient(credentals)
request = UpdateAliasKeyRequest('01GZZWTJYTNRGEQ8YMQQ7H6KMS', 'ssss dep zai')
print(kms.update_alias_key(request))