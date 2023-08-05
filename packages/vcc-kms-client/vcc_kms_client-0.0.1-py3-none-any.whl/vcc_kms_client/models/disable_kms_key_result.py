class DisableKMSKeyResult:
    def __init__(self, key_id, state):
        self.key_id = key_id
        self.state = state

    def __str__(self):
        str = "key_id = {}, state = {}"
        return str.format(self.key_id, self.state)
