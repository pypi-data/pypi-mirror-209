from .invalid_argument_exception import InvalidArgumentException

class ListKMSKeyByAliasRequest:
    def __init__(self, limit, offset, alias):
        self.validate(alias)
        self.limit = limit
        self.offset = offset
        self.alias = alias

    def validate(self, alias):
        if alias == None or alias=='':
            raise InvalidArgumentException('Required field [alias]')