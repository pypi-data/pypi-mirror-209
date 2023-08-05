from src.vcc_kms_client.auth.kms_credentials import KMSCredentials
from src.vcc_kms_client.models.update_description_key_request import UpdateDescriptionKeyRequest
from src.vcc_kms_client.kms_client import KMSClient

f = open("file/security_file.json", "r")
credentals = KMSCredentials(f)
kms = KMSClient(credentals)
request = UpdateDescriptionKeyRequest('01GZZWTJYTNRGEQ8YMQQ7H6KMS', 'dsafasfasfasasfasf')
print(kms.update_description_key(request))