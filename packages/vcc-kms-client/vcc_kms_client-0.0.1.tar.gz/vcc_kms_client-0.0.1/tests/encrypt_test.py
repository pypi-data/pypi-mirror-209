import json

from src.vcc_kms_client.auth.kms_credentials import KMSCredentials
from src.vcc_kms_client.models import content_type
from src.vcc_kms_client.models.encrypt_request import EncryptRequest
from src.vcc_kms_client.kms_client import KMSClient

f = open("file/security_file.json", "r")
credentals = KMSCredentials(f)
kms = KMSClient(credentals)
# request = EncryptRequest('01GZZWTJYTNRGEQ8YMQQ7H6KMS', 'cuong dep zai', content_type.SINGLE_STRING)
# request = EncryptRequest('01GZZWTJYTNRGEQ8YMQQ7H6KMS', ['cuong dep zai', 'asdasdasd'], content_type.LIST_STRING)
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y = json.dumps(x)
request = EncryptRequest('01GZZWTJYTNRGEQ8YMQQ7H6KMS', [y], content_type.LIST_JSON_OBJECT)
print(kms.encrypt(request))