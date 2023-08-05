from src.vcc_kms_client.auth.kms_credentials import KMSCredentials
from src.vcc_kms_client.models import algorithm
from src.vcc_kms_client.models.generate_data_key_pair_request import GenerateDataKeyPairRequest

from src.vcc_kms_client.kms_client import KMSClient

f = open("file/security_file.json", "r")
credentals = KMSCredentials(f)
kms = KMSClient(credentals)
request = GenerateDataKeyPairRequest('01GZZWTJYTNRGEQ8YMQQ7H6KMS', algorithm.RSA_2048)
print(kms.generate_data_key_pair(request))