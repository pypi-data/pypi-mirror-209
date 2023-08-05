class SignDto:
    def  __init__(self, key_id, message, action, sign_algorithm):
        self.keyId = key_id
        self.message = message
        self.action = action
        self.signAlgorithm = sign_algorithm