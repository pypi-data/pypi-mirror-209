class DecryptWithDataKeyResult:
    def __init__(self, key_id, output):
        self.key_id = key_id
        self.output = output

    def __str__(self):
        str = "key_id = {}, output = {}"
        return str.format(self.key_id, self.output)
