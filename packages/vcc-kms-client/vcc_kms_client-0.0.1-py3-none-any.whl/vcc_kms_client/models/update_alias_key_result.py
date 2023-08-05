class UpdateAliasKeyResult:
    def __init__(self, key_id, alias):
        self.key_id = key_id
        self.alias = alias

    def __str__(self):
        str = "key_id = {}, alias = {}"
        return str.format(self.key_id, self.alias)