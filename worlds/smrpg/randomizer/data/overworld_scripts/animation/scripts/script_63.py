#A0063_EXPLOSION_WITH_SOUND
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
	A_Set700CToCurrentLevel(),
	A_JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 13, ["ACTION_63_sequence_looping_on_3"]),
	A_SetVRAMPriority(PRIORITY_3),
	A_SequenceLoopingOn(identifier="ACTION_63_sequence_looping_on_3"),
	A_SequencePlaybackOn(),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_SetSpriteSequence(index=0, looping=False),
	A_JmpIfBitSet(TEMP_7042_7, ["ACTION_63_play_sound_13"]),
	A_Set700CToCurrentLevel(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 457, ["ACTION_63_play_sound_11"]),
	A_JmpIfVarEqualsConst(CURRENT_OVERWORLD_MARKER_ID, 4, ["ACTION_63_play_sound_17"]),
	A_PlaySound(sound=SO060_DYNAMITE_BOMB_EXPLOSION, channel=4, identifier="ACTION_63_play_sound_11"),
	A_Jmp(["ACTION_63_shift_z_up_pixels_14"]),
	A_PlaySound(sound=SO113_OPEN_CHAMBER_DOOR, channel=4, identifier="ACTION_63_play_sound_13"),
	A_ShiftZUpPixels(18, identifier="ACTION_63_shift_z_up_pixels_14"),
	A_VisibilityOff(),
	A_ReturnQueue(),
	A_PlaySound(sound=SO052_DEEP_BOUNCE, channel=4, identifier="ACTION_63_play_sound_17"),
	A_Jmp(["ACTION_63_shift_z_up_pixels_14"])
])
