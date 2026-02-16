from randomizer.types.gameworld import GameWorld
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.types.classes import (
    UsableActionScriptCommand,
)
from typing import TypeVar

T = TypeVar('T', bound=UsableActionScriptCommand)


def get_subscript_command_by_identifier(
    world: GameWorld,
    event_cmd_id: str,
    subscript_cmd_id: str,
    cmd_type: type[T],
) -> T:
    """Convenience wrapper for world.event_scripts.get_subscript_command_by_identifier."""
    return world.event_scripts.get_subscript_command_by_identifier(
        event_cmd_id, subscript_cmd_id, cmd_type
    )
