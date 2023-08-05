from src.vcc_kms_client.auth.kms_credentials import KMSCredentials
from src.vcc_kms_client.models.delete_alias_key_request import DeleteAliasKeyRequest
from src.vcc_kms_client.kms_client import KMSClient

f = open("file/security_file.json", "r")
credentals = KMSCredentials(f)
kms = KMSClient(credentals)
request = DeleteAliasKeyRequest('01GZZWTJYTNRGEQ8YMQQ7H6KMS')
print(kms.delete_alias_key(request))