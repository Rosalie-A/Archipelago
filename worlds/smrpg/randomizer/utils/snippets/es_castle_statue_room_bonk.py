"""Castle statue room bonk script snippet."""

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScript
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.commands import (
    ActionQueueAsync,
    ActionQueueSync,
    Return,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.commands import (
    A_FaceSouthwest,
    A_FixedFCoordOff,
    A_FixedFCoordOn,
    A_JumpToHeight,
    A_Pause,
    A_SequencePlaybackOff,
    A_SequencePlaybackOn,
    A_SetAllSpeeds,
    A_SetSpriteSequence,
    A_SetWalkingSpeed,
    A_Walk1StepNortheast,
    A_WalkSouthwestSteps,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments.sequence_speeds import (
    FAST,
    NORMAL,
    VERY_FAST,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import NPC_3


script = EventScript([
    ActionQueueAsync(
        target=NPC_3,
        subscript=[
            A_SequencePlaybackOn(),
            A_SetAllSpeeds(NORMAL),
            A_Pause(3),
            A_FaceSouthwest(),
            A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True),
            A_Pause(9),
            A_FixedFCoordOn(),
            A_SetSpriteSequence(index=0, is_sequence=True),
            A_Walk1StepNortheast(),
            A_SetAllSpeeds(VERY_FAST),
            A_WalkSouthwestSteps(2),
            A_SequencePlaybackOff(),
        ],
    ),
    ActionQueueSync(
        target=NPC_3,
        subscript=[
            A_SetWalkingSpeed(FAST),
            A_JumpToHeight(50),
            A_Walk1StepNortheast(),
            A_FixedFCoordOff(),
            A_SetAllSpeeds(NORMAL),
            A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True),
        ],
    ),
    Return(),
])
