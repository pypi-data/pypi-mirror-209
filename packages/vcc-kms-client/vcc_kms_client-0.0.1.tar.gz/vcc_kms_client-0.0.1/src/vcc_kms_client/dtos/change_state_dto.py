class ChangeStateDto:
    def __init__(self, key_id, state, action):
        self.keyId = key_id
        self.state = state
        self.action = action