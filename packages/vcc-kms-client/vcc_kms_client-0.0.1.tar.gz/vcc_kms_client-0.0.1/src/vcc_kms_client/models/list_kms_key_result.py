class ListKMSKeyResult:
    def __init__(self, keys):
        self.keys = keys

    def __str__(self):
        str = "keys = {}"
        return str.format(self.keys)