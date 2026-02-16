"""Script snippets that can be inserted easily."""

from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.classes import (
    UsableActionScriptCommand)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.commands import (
    A_FaceSouthwest,
    A_Pause,
    A_SetWalkingSpeed,
    A_ShiftZDownPixels,
    A_ShiftZUpPixels,
    A_ShiftZUpSteps,
    A_VisibilityOn,
    A_FixedFCoordOn,
    A_FixedFCoordOff,
    A_JumpToHeight,
    A_WalkNortheastSteps,
    A_SetSequenceSpeed,
    A_SetSpriteSequence
)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments.sequence_speeds import (
    FAST,
    VERY_FAST)

commands: list[UsableActionScriptCommand] = [
    A_FaceSouthwest(),
    A_VisibilityOn(),
    A_Pause(35),
    A_SetWalkingSpeed(VERY_FAST),
    A_ShiftZUpSteps(2),
    A_SetWalkingSpeed(FAST),
    A_ShiftZDownPixels(6),
    A_ShiftZUpPixels(6),
    A_ShiftZDownPixels(4),
    A_ShiftZUpPixels(4),
    A_ShiftZDownPixels(2),
    A_ShiftZUpPixels(2),
    A_Pause(20),
]

def get_mimic_rise_dojo() -> list[UsableActionScriptCommand]:
    """Get the commands for the mimic rising animation in the dojo."""
    return [
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(height=53, silent=True),
		A_WalkNortheastSteps(1), 
		A_Pause(20),
        A_SetWalkingSpeed(VERY_FAST),
        A_ShiftZUpSteps(2),
        A_SetWalkingSpeed(FAST),
        A_ShiftZDownPixels(6),
        A_ShiftZUpPixels(6),
        A_ShiftZDownPixels(4),
        A_ShiftZUpPixels(4),
        A_ShiftZDownPixels(2),
        A_ShiftZUpPixels(2),
        A_Pause(20),
	]

def get_mimic_rise_kamek() -> list[UsableActionScriptCommand]:
    """Get the commands for the mimic rising animation in the dojo."""
    return [
        A_SetWalkingSpeed(VERY_FAST),
        A_ShiftZUpSteps(2),
        A_SetWalkingSpeed(FAST),
        A_ShiftZDownPixels(6),
        A_ShiftZUpPixels(6),
        A_ShiftZDownPixels(4),
        A_ShiftZUpPixels(4),
        A_ShiftZDownPixels(2),
        A_ShiftZUpPixels(2),
        A_Pause(20),
	]
