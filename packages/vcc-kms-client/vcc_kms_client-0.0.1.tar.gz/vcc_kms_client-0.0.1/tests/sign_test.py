from src.vcc_kms_client.auth.kms_credentials import KMSCredentials
from src.vcc_kms_client.models import sign_algorithm
from src.vcc_kms_client.models.sign_request import SignRequest

from src.vcc_kms_client.kms_client import KMSClient

f = open("file/security_file.json", "r")
credentals = KMSCredentials(f)
kms = KMSClient(credentals)
request = SignRequest('01GZX850ZW3W4HC40T1ZX6V8NA','cuong dep zai', sign_algorithm.SHA512_RSA)
print(kms.sign(request))