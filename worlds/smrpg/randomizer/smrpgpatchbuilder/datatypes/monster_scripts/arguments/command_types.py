"""Int subclass instances representing valid command types in battle."""

from .types.classes import CommandType

COMMAND_ATTACK = CommandType(0)
COMMAND_SPECIAL = CommandType(1)
COMMAND_ITEM = CommandType(2)
