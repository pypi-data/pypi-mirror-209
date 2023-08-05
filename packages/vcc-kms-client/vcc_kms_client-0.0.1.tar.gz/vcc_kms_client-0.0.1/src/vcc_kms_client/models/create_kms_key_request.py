from .invalid_argument_exception import InvalidArgumentException

class CreateKMSKeyRequest:
    def __init__(self, description, alias, algorithm):
        self.validate(algorithm)
        self.description=description
        self.alias=alias
        self.algorithm=algorithm

    def validate(self,algorithm):
        if algorithm == None or algorithm=='':
            raise InvalidArgumentException('Required field [algorithm]')