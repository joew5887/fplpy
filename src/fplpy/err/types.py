class InvalidQueryResult(Exception):
    pass


class IDNotUnique(InvalidQueryResult):
    pass


class IDMatchesZeroElements(InvalidQueryResult):
    pass