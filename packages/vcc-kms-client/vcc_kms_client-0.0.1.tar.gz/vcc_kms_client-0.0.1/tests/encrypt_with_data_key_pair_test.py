import json

from src.vcc_kms_client.auth.kms_credentials import KMSCredentials
from src.vcc_kms_client.models import content_type
from src.vcc_kms_client.models import algorithm
from src.vcc_kms_client.models.encrypt_with_data_key_pair_request import EncryptWithDataKeyPairRequest
from src.vcc_kms_client.kms_client import KMSClient

f = open("file/security_file.json", "r")
credentals = KMSCredentials(f)
kms = KMSClient(credentals)
# request = EncryptWithDataKeyPairRequest('01GZZWTJYTNRGEQ8YMQQ7H6KMS', 'cuong dep zai', algorithm.RSA_2048,
#                                         content_type.SINGLE_STRING)
# request = EncryptWithDataKeyPairRequest('01GZZWTJYTNRGEQ8YMQQ7H6KMS', ['cuong dep zai'], algorithm.RSA_2048, content_type.LIST_STRING)
x = {
  "name": "John"
}
y = json.dumps(x)
request = EncryptWithDataKeyPairRequest('01GZZWTJYTNRGEQ8YMQQ7H6KMS', [y], algorithm.RSA_2048, content_type.LIST_JSON_OBJECT)
print(kms.encrypt_with_data_key_pair(request))
