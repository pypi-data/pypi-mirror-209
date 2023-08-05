from .invalid_argument_exception import InvalidArgumentException

class UpdateDescriptionKeyRequest:
    def __init__(self, key_id, description):
        self.validate(key_id, description)
        self.key_id = key_id
        self.description = description

    def validate(self, key_id, description):
        if key_id == None or key_id=='':
            raise InvalidArgumentException('Required field [key_id]')
        if description == None or description=='':
            raise InvalidArgumentException('Required field [description]')