class UpdateDescriptionKeyResult:
    def __init__(self, key_id, description):
        self.key_id = key_id
        self.description = description

    def __str__(self):
        str = "key_id = {}, description = {}"
        return str.format(self.key_id, self.description)