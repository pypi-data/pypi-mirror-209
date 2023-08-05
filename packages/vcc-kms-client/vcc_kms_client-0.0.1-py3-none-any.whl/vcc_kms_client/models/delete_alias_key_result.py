class DeleteAliasKeyResult:
    def __init__(self, key_id):
        self.key_id = key_id

    def __str__(self):
        str = "key_id = {}"
        return str.format(self.key_id)