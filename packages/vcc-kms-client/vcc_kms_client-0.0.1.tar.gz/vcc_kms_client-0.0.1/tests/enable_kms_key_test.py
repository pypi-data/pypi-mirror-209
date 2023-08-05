from src.vcc_kms_client.auth.kms_credentials import KMSCredentials
from src.vcc_kms_client.models.enable_kms_key_request import EnableKMSKeyRequest
from src.vcc_kms_client.kms_client import KMSClient

f = open("file/security_file.json", "r")
credentals = KMSCredentials(f)
kms = KMSClient(credentals)
request = EnableKMSKeyRequest('01GZZWTJYTNRGEQ8YMQQ7H6KMS')
print(kms.enable_kms_key(request))