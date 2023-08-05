import json

from src.vcc_kms_client.auth.kms_credentials import KMSCredentials
from src.vcc_kms_client.models import content_type
from src.vcc_kms_client.models.decrypt_request import DecryptRequest
from src.vcc_kms_client.kms_client import KMSClient

f = open("file/security_file.json", "r")
credentals = KMSCredentials(f)
kms = KMSClient(credentals)
# request = DecryptRequest('01GZZWTJYTNRGEQ8YMQQ7H6KMS', 'LoujTFUY5aELdmBB6b2N0g==', content_type.SINGLE_STRING)
# request = DecryptRequest('01GZZWTJYTNRGEQ8YMQQ7H6KMS', ['LoujTFUY5aELdmBB6b2N0g==', 's11DGSnLf6hUNHYNB6rwFQ=='], content_type.LIST_STRING)
x = {
  "name": "IYMUmLTiP5rZFYA9zKIWTA==",
  "age": "vBzZWDM9u3Fkt0yVQCl7Ow==",
  "city": "PFdV2PVgBbcQp+mQyd4usQ=="
}
y = json.dumps(x)
request = DecryptRequest('01GZZWTJYTNRGEQ8YMQQ7H6KMS', [y], content_type.LIST_JSON_OBJECT)
print(kms.decrypt(request))