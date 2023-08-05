class GenerateDataKeyPairResult:
    def __init__(self, key_id, algorithm, encrypt_private_data_key, plaintext_private_data_key, plaintext_public_data_key):
        self.key_id = key_id
        self.algorithm = algorithm
        self.encrypt_private_data_key = encrypt_private_data_key
        self.plaintext_private_data_key = plaintext_private_data_key
        self.plaintext_public_data_key = plaintext_public_data_key


    def __str__(self):
        str = "key_id = {}, algorithm = {}, encrypt_private_data_key = {}, plaintext_private_data_key = {}, plaintext_public_data_key = {}"
        return str.format(self.key_id, self.algorithm, self.encrypt_private_data_key, self.plaintext_private_data_key, self.plaintext_public_data_key)
