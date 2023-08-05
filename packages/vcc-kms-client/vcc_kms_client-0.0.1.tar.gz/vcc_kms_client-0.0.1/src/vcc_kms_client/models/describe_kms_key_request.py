from .invalid_argument_exception import InvalidArgumentException

class DescribeKMSKeyRequest:
    def __init__(self, key_id):
        self.validate(key_id)
        self.key_id = key_id

    def validate(self, key_id):
        if key_id == None or key_id=='':
            raise InvalidArgumentException('Required field [key_id]')