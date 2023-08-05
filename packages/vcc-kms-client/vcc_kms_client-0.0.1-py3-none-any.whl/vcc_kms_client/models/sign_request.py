from .invalid_argument_exception import InvalidArgumentException

class SignRequest:
    def __init__(self, key_id, message, sign_algorithm):
        self.validate(key_id, message, sign_algorithm)
        self.key_id = key_id
        self.message = message
        self.sign_algorithm = sign_algorithm

    def validate(self, key_id, message, sign_algorithm):
        if key_id == None or key_id == '':
            raise InvalidArgumentException('Required field [key_id]')
        if message == None or message == '':
            raise InvalidArgumentException('Required field [message]')
        if sign_algorithm == None or sign_algorithm == '':
            raise InvalidArgumentException('Required field [sign_algorithm]')
