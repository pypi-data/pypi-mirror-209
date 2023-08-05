class ListKMSKeyByAliasResult:
    def __init__(self, keys, alias):
        self.keys = keys
        self.alias = alias

    def __str__(self):
        str = "keys = {}, alias = {}"
        return str.format(self.keys, self.alias)