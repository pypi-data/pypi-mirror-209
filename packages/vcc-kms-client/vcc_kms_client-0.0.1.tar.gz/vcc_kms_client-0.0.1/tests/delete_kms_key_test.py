from src.vcc_kms_client.auth.kms_credentials import KMSCredentials
from src.vcc_kms_client.models.delete_kms_key_request import DeleteKMSKeyRequest
from src.vcc_kms_client.kms_client import KMSClient

f = open("file/security_file.json", "r")
credentals = KMSCredentials(f)
kms = KMSClient(credentals)
request = DeleteKMSKeyRequest('01H0PYX8VZXE6A56DQVWHVXZXJ')
print(kms.delete_kms_key(request))