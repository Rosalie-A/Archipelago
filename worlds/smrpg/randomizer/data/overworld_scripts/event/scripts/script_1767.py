# E1767_TEMPLE_FORTUNE_RESULTS_ROOM_GATE_OPENS
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScript
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.colours import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.controller_inputs import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.intro_title_text import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.layers import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_types import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.scenes import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.tutorials import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.battlefield_names import *
from ....variables.dialog_names import *
from ....variables.event_script_names import *
from ....variables.music_names import *
from ....variables.overworld_area_names import *
from ....variables.overworld_sfx_names import *
from ....variables.pack_names import *
from ....variables.room_names import *
from ....variables.shop_names import *
from ....variables.variable_names import *
from ....items import *
from ....packets import *
from ....spells.spells import *

script = EventScript([
	EnableControlsUntilReturn([]),
	SetBit(HAS_A_PRIZE_FORTUNE),
	ClearBit(BELOME_FORTUNE_1),
	ApplySolidityModToLevel(permanent=True, room_id=R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE, mod_id=0),
	PlaySound(sound=SO017_OPEN_FRONT_GATE, channel=6),
	ActionQueueAsync(target=LAYER_1, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthSteps(3),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_TransferXYZFSteps(x=0, y=0, z=18, direction=EAST),
		A_ShiftZUpPixels(1),
		A_FloatingOn(),
		A_SetSolidityBits(bit_4=True),
		A_ObjectMemorySetBit(arg_1=0x0B, bits=[3]),
		A_ShadowOff(),
		A_VisibilityOn(),
		A_Pause(1, identifier="EVENT_1767_action_queue_6_SUBSCRIPT_pause_7"),
		A_JmpIfObjectInAir(NPC_4, ["EVENT_1767_action_queue_6_SUBSCRIPT_pause_7"]),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=0, looping=False),
		A_Pause(5),
		A_PlaySound(sound=SO010_TRAMPOLINE, channel=6),
		A_Pause(55)
	]),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(1, identifier="EVENT_1767_action_queue_8_SUBSCRIPT_pause_0"),
		A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_Z, pixel=True, bit_7=True),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["EVENT_1767_ret_9"]),
		A_JumpToHeight(0),
		A_Jmp(["EVENT_1767_action_queue_8_SUBSCRIPT_pause_0"])
	]),
	Return(identifier="EVENT_1767_ret_9")
])
