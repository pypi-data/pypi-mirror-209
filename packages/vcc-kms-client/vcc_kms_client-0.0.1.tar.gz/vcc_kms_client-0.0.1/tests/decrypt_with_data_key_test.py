import json

from src.vcc_kms_client.auth.kms_credentials import KMSCredentials
from src.vcc_kms_client.models import content_type
from src.vcc_kms_client.models.decrypt_with_data_key_request import DecryptWithDataKeyRequest
from src.vcc_kms_client.kms_client import KMSClient

f = open("file/security_file.json", "r")
credentals = KMSCredentials(f)
kms = KMSClient(credentals)
# request = DecryptWithDataKeyRequest('01GZZWTJYTNRGEQ8YMQQ7H6KMS', '7CqNRImiu2/DdnNoosdYnsBE5OG9536Cm3i1ulWm8f4ZcBUt4w4C9v3CI+lk2q/d8QJHJWzf9j0ljhvsH4L+/6uYa6pItvBwNNmCzhoV6m/ZyRMsheVwtZNxILVTs9qMx0ma4bivTvvF+DjJj2X2q6AZOVKJ0v2QsD78Tk/yOUc=', content_type.SINGLE_STRING)
# request = DecryptWithDataKeyRequest('01GZZWTJYTNRGEQ8YMQQ7H6KMS', ['7CqNRImiu2/DdnNoosdYnmtjitw05f0yj+ZaVggwGZbtxYKlG1dpnEylu+yL+nJFlJceXbptMvLtoX2iauXUfUGna7kY1JtJHoJbMIKYRBY7lBXMUimVH60de4I6gcaLl3T1pBZcs+kXOkpggIwSaDG880ExuSv9CFcRFUUEAvc='], content_type.LIST_STRING)
x = {
  "name": "7CqNRImiu2/DdnNoosdYnpe87Xr+x7AOLNni46fKzsKVuG2YKgz6lD5pbdkgO94dmNLB9O1/MDaMhoXvJvqE/8JdmKCicHEygizphFWleP4JSM8sdxYmI0B2fVZhT3lqlfUs60Lfkw1ldGeCbx1w85W335RrpjBI7O2kJXaWIdI=",
  "age": "7CqNRImiu2/DdnNoosdYnnxYyyMhVU9FGFfC5pEJm6VW2SeLpYoHzVtGUF87NXwj/k2MslgSZKYVGZ3EhrisIBC1tFR5AeL97WsUClSP989Es3HlTIPJODCFRZngjdjHpVIFbXrfzZGU2yqlxLtJfe44h7BWckg3HFRVzq1Hpw4=",
  "city": "7CqNRImiu2/DdnNoosdYnkcWN01M9TuSTp1iBKr4tkvfma27HtX84d4BZSdXzXx4o550Dd/iW6yqVB+NMJ0HE5r439gaqxcmojf5zF8OAszJzqniNRDJZn7t1DtnRp3Yzbebj3/ErW7t2EDicjae5O4NNgrTZc3Dap9bB2vMSSU="
}
y = json.dumps(x)
request = DecryptWithDataKeyRequest('01GZZWTJYTNRGEQ8YMQQ7H6KMS', [y], content_type.LIST_JSON_OBJECT)
print(kms.decrypt_with_data_key(request))