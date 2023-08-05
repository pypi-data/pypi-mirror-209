class SignResult:
    def __init__(self, key_id, signature, sign_algorithm):
        self.key_id = key_id
        self.signature = signature
        self.sign_algorithm = sign_algorithm

    def __str__(self):
        str = "key_id = {}, signature = {}, sign_algorithm = {}"
        return str.format(self.key_id, self.signature, self.sign_algorithm)
