class GenerateDataKeyDto:
    def __init__(self,
                 key_id,
                 algorithm,
                 encrypt_private_data_key,
                 plaintext_private_data_key,
                 plaintext_public_data_key,
                 encrypt_secret_data_key,
                 plaintext_secret_data_key,
                 action):
        self.keyId = key_id
        self.algorithm = algorithm
        self.encryptPrivateDataKey = encrypt_private_data_key
        self.plaintextPrivateDataKey = plaintext_private_data_key
        self.plaintextPublicDataKey = plaintext_public_data_key
        self.encryptSecretDataKey = encrypt_secret_data_key
        self.plaintext_secret_data_key = plaintext_secret_data_key
        self.action = action