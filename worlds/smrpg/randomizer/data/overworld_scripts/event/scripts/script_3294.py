# E3294_SHIP_BULLET_COLLISION_BACKGROUND
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
	EnableControls([]),
	ClearBit(TEMP_7044_7),
	ActionQueueSync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_npcs=True, bit_7=True),
		A_SetWalkingSpeed(FAST),
		A_Set700CToObjectCoord(target_npc=MEM_70AA, coord=COORD_F),
		A_Mem700CAndConst(0x000F),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["EVENT_3294_action_queue_2_SUBSCRIPT_set_sprite_sequence_6"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["EVENT_3294_action_queue_2_SUBSCRIPT_set_sprite_sequence_10"]),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True, identifier="EVENT_3294_action_queue_2_SUBSCRIPT_set_sprite_sequence_6"),
		A_WalkSoutheastPixels(2),
		A_JmpIfMarioInAir(["EVENT_3294_action_queue_2_SUBSCRIPT_set_bit_14"]),
		A_Jmp(["EVENT_3294_action_queue_2_SUBSCRIPT_set_sprite_sequence_6"]),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True, identifier="EVENT_3294_action_queue_2_SUBSCRIPT_set_sprite_sequence_10"),
		A_WalkSouthwestPixels(2),
		A_JmpIfMarioInAir(["EVENT_3294_action_queue_2_SUBSCRIPT_set_bit_14"]),
		A_Jmp(["EVENT_3294_action_queue_2_SUBSCRIPT_set_sprite_sequence_10"]),
		A_SetBit(TEMP_7044_7, identifier="EVENT_3294_action_queue_2_SUBSCRIPT_set_bit_14"),
		A_ResetProperties(),
		A_SetWalkingSpeed(NORMAL),
		A_ShiftZDownPixels(1),
		A_SetSolidityBits(cant_pass_npcs=True, bit_7=True),
		A_ReturnQueue()
	]),
	Pause(1, identifier="EVENT_3294_pause_3"),
	JmpIfBitClear(TEMP_7044_7, ["EVENT_3294_pause_3"]),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	Return()
])
