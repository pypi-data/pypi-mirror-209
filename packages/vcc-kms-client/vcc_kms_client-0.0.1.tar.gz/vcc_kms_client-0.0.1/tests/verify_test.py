from src.vcc_kms_client.auth.kms_credentials import KMSCredentials
from src.vcc_kms_client.models import sign_algorithm
from src.vcc_kms_client.models.verify_request import VerifyRequest
from src.vcc_kms_client.kms_client import KMSClient

f = open("file/security_file.json", "r")
credentals = KMSCredentials(f)
kms = KMSClient(credentals)
request = VerifyRequest('01GZX850ZW3W4HC40T1ZX6V8NA', 'cuong dep zai', sign_algorithm.SHA512_RSA,
                        'C/PDWwJ2NpsqbwJTVDKqosFue+rs3dl+vKPbdVqh9zIc6Lnm33/WadCA2X+tMs87UOxaeuIn+NtgL6Jnh3ZgkkWB086ltp/YbccG+H9mxCc/OXKSP2hOZdO7bE5HXi4RyoXG3Mcv/ckXlgP02v9U2gehvQCOA9mcP3XDTZvHxCvU+WQpIt/QiNW3Ov150X7HrHt9vRFlX8cY1ciLH4esDcqshLY0Cw/SinB4hUJ8eX5DanQ/5VMZY12SLMQL+y9sifrmJNIe9WP0Gysp8yGPCwcO+zP49TrEs/zmMvkUscf3+0tJTFYetF4a4+zhI7QoaV/4FWPVaBVoh7kkb0HolQ==')
print(kms.verify(request))