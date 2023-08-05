class EncryptDto:
    def __init__(self, key_id, text, texts, jsons, algorithm, action, content_type):
        self.keyId = key_id
        self.text = text
        self.texts = texts
        self.jsons = jsons
        self.algorithm = algorithm
        self.action = action
        self.contentType = content_type
