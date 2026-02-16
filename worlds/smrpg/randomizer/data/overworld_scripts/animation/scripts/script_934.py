#A0934_CORKPEDITE
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.event_script_names import *
from ....variables.overworld_sfx_names import *
from ....variables.room_names import *
from ....variables.variable_names import *
from ....packets import *
from ....items import *

script = ActionScript([
	A_SequencePlaybackOff(identifier="ACTION_934_sequence_playback_off_0"),
	A_SequenceLoopingOff(),
	A_Pause(2, identifier="ACTION_934_pause_2"),
	A_JmpIfBitClear(TEMP_7043_0, ["ACTION_934_pause_2"]),
	A_SequenceLoopingOn(),
	A_FloatingOff(),
	A_SetWalkingSpeed(FAST),
	A_ShiftZUpPixels(16),
	A_SetWalkingSpeed(NORMAL),
	A_ShiftZUpPixels(8),
	A_SetWalkingSpeed(SLOW),
	A_ShiftZUpPixels(4),
	A_SetWalkingSpeed(VERY_SLOW),
	A_ShiftZUpPixels(2),
	A_Pause(12),
	A_FloatingOn(),
	A_ClearBit(TEMP_7043_0),
	A_Jmp(["ACTION_934_sequence_playback_off_0"])
])
