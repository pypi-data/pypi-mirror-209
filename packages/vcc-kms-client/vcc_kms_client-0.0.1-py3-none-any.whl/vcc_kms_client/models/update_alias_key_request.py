from .invalid_argument_exception import InvalidArgumentException

class UpdateAliasKeyRequest:
    def __init__(self, key_id, alias):
        self.validate(key_id, alias)
        self.key_id = key_id
        self.alias = alias

    def validate(self, key_id, alias):
        if key_id == None or key_id=='':
            raise InvalidArgumentException('Required field [key_id]')
        if alias == None or alias=='':
            raise InvalidArgumentException('Required field [alias]')