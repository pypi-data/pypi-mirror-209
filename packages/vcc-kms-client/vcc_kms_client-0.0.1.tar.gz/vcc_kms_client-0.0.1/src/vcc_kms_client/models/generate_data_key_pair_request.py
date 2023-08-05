from .invalid_argument_exception import InvalidArgumentException

class GenerateDataKeyPairRequest:
    def __init__(self, key_id, algorithm):
        self.validate(key_id, algorithm)
        self.key_id = key_id
        self.algorithm = algorithm

    def validate(self, key_id, algorithm):
        if key_id == None or key_id=='':
            raise InvalidArgumentException('Required field [key_id]')
        if algorithm == None or algorithm=='':
            raise InvalidArgumentException('Required field [algorithm]')