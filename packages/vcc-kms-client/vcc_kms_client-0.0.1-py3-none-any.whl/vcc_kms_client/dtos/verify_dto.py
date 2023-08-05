class VerifyDto:
    def __init__(self, key_id, message, signed_message, action, sign_algorithm, signature_valid):
        self.keyId = key_id
        self.message = message
        self.signedMessage = signed_message
        self.action = action
        self.signAlgorithm = sign_algorithm
        self.signatureValid = signature_valid