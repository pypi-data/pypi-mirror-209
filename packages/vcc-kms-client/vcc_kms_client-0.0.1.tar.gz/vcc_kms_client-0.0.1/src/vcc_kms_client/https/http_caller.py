import os
import shutil
import ssl
import http.client
import urllib.parse

class HttpCaller:
    def __init__(self, kms_credentials):
        context = ssl.SSLContext(ssl.PROTOCOL_TLS)
        context.load_cert_chain(certfile=kms_credentials.get_cert_file_path(),
                                keyfile=kms_credentials.get_key_file_path())
        context.load_verify_locations(cafile=kms_credentials.get_ca_file_path())

        self.delete_security_file()

        self.connection = http.client.HTTPSConnection(host=kms_credentials.get_domain(), context=context)

    def get(self, api, headers={}, params=None):
        if params != None:
            api += '?' + urllib.parse.urlencode(params)

        self.connection.request(method='GET', url=api, headers=headers)
        response = self.connection.getresponse()
        result = response.read().decode('utf-8')
        return result

    def post(self, api, body, headers={'Content-type': 'application/json'}, params=None):
        if params != None:
            api += '?' + urllib.parse.urlencode(params)

        self.connection.request(method='POST', body=body, url=api, headers=headers)
        response = self.connection.getresponse()
        result = response.read().decode('utf-8')
        return result

    def delete_security_file(self):
        folder_path = 'private'
        if os.path.isdir(folder_path):
            shutil.rmtree(folder_path, ignore_errors=False)
