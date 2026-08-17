from .Connection import Connection
from .SMRPGLocation import SMRPGLocation


class SMRPGRegion:
    name: str
    connections: list[Connection] = []
    locations: list[SMRPGLocation] = []

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.__repr__()