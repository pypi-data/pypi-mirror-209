from src.vcc_kms_client.auth.kms_credentials import KMSCredentials
from src.vcc_kms_client.models.list_kms_key_by_alias_request import ListKMSKeyByAliasRequest
from src.vcc_kms_client.kms_client import KMSClient

f = open("file/security_file.json", "r")
credentals = KMSCredentials(f)
kms = KMSClient(credentals)
request = ListKMSKeyByAliasRequest(1, 0, 'cuong dep zai')
print(kms.list_key_by_alias(request).keys[0])