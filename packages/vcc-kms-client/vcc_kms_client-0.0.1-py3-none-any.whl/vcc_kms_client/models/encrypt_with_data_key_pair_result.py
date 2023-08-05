class EncryptWithDataKeyPairResult:
    def __init__(self, key_id, output, algorithm):
        self.key_id = key_id
        self.output = output
        self.algorithm = algorithm

    def __str__(self):
        str = "key_id = {}, output = {}, algorithm = {}"
        return str.format(self.key_id, self.output, self.algorithm)
