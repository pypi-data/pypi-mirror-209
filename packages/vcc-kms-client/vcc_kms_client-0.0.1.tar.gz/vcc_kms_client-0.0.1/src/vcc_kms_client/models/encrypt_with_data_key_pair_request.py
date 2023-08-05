from .invalid_argument_exception import InvalidArgumentException

class EncryptWithDataKeyPairRequest:
    def __init__(self, key_id, input, algorithm, content_type):
        self.validate(key_id, input, content_type, algorithm)
        self.key_id = key_id
        self.input = input
        self.content_type = content_type
        self.algorithm = algorithm

    def validate(self, key_id, input, content_type, algorithm):
        if key_id == None or key_id=='':
            raise InvalidArgumentException('Required field [key_id]')
        if input == None or input=='':
            raise InvalidArgumentException('Required field [input]')
        if content_type == None or content_type=='':
            raise InvalidArgumentException('Required field [content_type]')
        if algorithm == None or algorithm=='':
            raise InvalidArgumentException('Required field [algorithm]')
