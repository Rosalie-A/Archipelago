#A0819_LANDS_END_GECKO_CANNON
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
	A_SetPriority(3),
	A_SequenceLoopingOff(),
	A_FixedFCoordOn(),
	A_Set700CToPressedButton(),
	A_AddConstToVar(PRIMARY_TEMP_700C, 65516),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(9),
	A_EndLoop(),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_819_set_sprite_sequence_8"),
	A_Pause(16),
	A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True),
	A_Set700CToPressedButton(),
	A_AddConstToVar(PRIMARY_TEMP_700C, 65515),
	A_AddConstToVar(PRIMARY_TEMP_700C, 25),
	A_SetMem704XAt700CBit(),
	A_AddConstToVar(PRIMARY_TEMP_700C, 4),
	A_SetMem704XAt700CBit(),
	A_Pause(16),
	A_Set700CToPressedButton(),
	A_AddConstToVar(PRIMARY_TEMP_700C, 65515),
	A_AddConstToVar(PRIMARY_TEMP_700C, 25),
	A_ClearMem704XAt700CBit(),
	A_AddConstToVar(PRIMARY_TEMP_700C, 4),
	A_ClearMem704XAt700CBit(),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(16),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(16),
	A_Jmp(["ACTION_819_set_sprite_sequence_8"])
])
