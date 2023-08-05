import json
import base64
from OpenSSL import crypto
from pathlib import Path
import os

class KMSCredentials:
    def __init__(self, security_file):
        self.security_file = security_file

        credential_json = json.loads(self.security_file.read())
        keystore_bytes = base64.b64decode(credential_json['keystore_base64'])
        truststore_bytes = base64.b64decode(credential_json['truststore_base64'])

        keystore_pkcs12 = crypto.load_pkcs12(keystore_bytes, credential_json['password_file'])
        truststore_pkcs12 = crypto.load_pkcs12(truststore_bytes, credential_json['password_file'])

        cer_file_path = 'private/cer.pem'
        ca_file_path = 'private/ca.pem'
        key_file_path = 'private/key.pem'

        os.makedirs('private', exist_ok=True)

        if not Path(cer_file_path).is_file():
            cer_file = open(cer_file_path, 'wb')
            cer_file.write(crypto.dump_certificate(crypto.FILETYPE_PEM, keystore_pkcs12.get_certificate()))
            cer_file.close()

        if not Path(ca_file_path).is_file():
            ca_file = open(ca_file_path, 'wb')
            ca_file.write(crypto.dump_certificate(crypto.FILETYPE_PEM, truststore_pkcs12.get_ca_certificates()[0]))
            ca_file.close()

        if not Path(key_file_path).is_file():
            key_file = open(key_file_path, 'wb')
            key_file.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, keystore_pkcs12.get_privatekey()))
            key_file.close()

        self.cer_file_path = cer_file_path
        self.key_file_path = key_file_path
        self.ca_file_path = ca_file_path
        self.domain = credential_json['domain'][8:]

    def get_ca_file_path(self):
        return self.ca_file_path

    def get_cert_file_path(self):
        return self.cer_file_path

    def get_key_file_path(self):
        return self.key_file_path

    def get_domain(self):
        return self.domain