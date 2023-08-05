class GenerateDataKeyResult:
    def __init__(self, key_id, algorithm, plaintext_data_key, encrypt_data_key):
        self.key_id = key_id
        self.algorithm = algorithm
        self.plaintext_data_key = plaintext_data_key
        self.encrypt_data_key = encrypt_data_key


    def __str__(self):
        str = "key_id = {}, algorithm = {}, plaintext_data_key = {}, encrypt_data_key = {}"
        return str.format(self.key_id, self.algorithm, self.plaintext_data_key, self.encrypt_data_key)
