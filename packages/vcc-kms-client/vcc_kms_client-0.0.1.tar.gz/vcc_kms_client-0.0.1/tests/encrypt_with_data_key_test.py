import json

from src.vcc_kms_client.auth.kms_credentials import KMSCredentials
from src.vcc_kms_client.models import content_type
from src.vcc_kms_client.models import algorithm
from src.vcc_kms_client.models.encrypt_with_data_key_request import EncryptWithDataKeyRequest
from src.vcc_kms_client.kms_client import KMSClient

f = open("file/security_file.json", "r")
credentals = KMSCredentials(f)
kms = KMSClient(credentals)
# request = EncryptWithDataKeyRequest('01GZZWTJYTNRGEQ8YMQQ7H6KMS', 'cuong dep zai', algorithm.AES_256,
#                                     content_type.SINGLE_STRING)
# request = EncryptWithDataKeyRequest('01GZZWTJYTNRGEQ8YMQQ7H6KMS', ['cuong dep zai'], algorithm.AES_256, content_type.LIST_STRING)
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)
request = EncryptWithDataKeyRequest('01GZZWTJYTNRGEQ8YMQQ7H6KMS', [y], algorithm.AES_256, content_type.LIST_JSON_OBJECT)
print(kms.encrypt_with_data_key(request))
