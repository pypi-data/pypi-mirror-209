class KMSKeyDto:
    def __init__(self, id, description, alias, state, algorithm):
        self.id = id
        self.description = description
        self.alias = alias
        self.state = state
        self.algorithm = algorithm
