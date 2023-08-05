class VerifyResult:
    def __init__(self, key_id, signature_valid, sign_algorithm):
        self.key_id = key_id
        self.signature_valid = signature_valid
        self.sign_algorithm = sign_algorithm

    def __str__(self):
        str = "key_id = {}, signature_valid = {}, sign_algorithm = {}"
        return str.format(self.key_id, self.signature_valid, self.sign_algorithm)
