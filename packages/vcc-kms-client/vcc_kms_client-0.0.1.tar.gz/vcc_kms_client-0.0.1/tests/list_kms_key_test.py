from src.vcc_kms_client.auth.kms_credentials import KMSCredentials
from src.vcc_kms_client.models.list_kms_key_request import ListKMSKeyRequest
from src.vcc_kms_client.kms_client import KMSClient

f = open("file/security_file.json", "r")
credentals = KMSCredentials(f)
kms = KMSClient(credentals)
request = ListKMSKeyRequest(3, 0)
for key in kms.list_key(request).keys:
    print(key)