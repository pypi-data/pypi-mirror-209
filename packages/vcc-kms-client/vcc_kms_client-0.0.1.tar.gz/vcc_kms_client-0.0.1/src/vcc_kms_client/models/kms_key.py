class KMSKey:
    def __init__(self, key_id, alias, algorithm, state, description):
        self.key_id = key_id
        self.alias = alias
        self.algorithm = algorithm
        self.state = state
        self.description = description

    def __str__(self):
        str = "key_id = {}, alias = {}, algorithm = {}, state = {}, description = {}"
        return str.format(self.key_id, self.alias, self.algorithm, self.state, self.description)