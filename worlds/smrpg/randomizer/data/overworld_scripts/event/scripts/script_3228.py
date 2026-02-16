# E3228_SHIP_CLONE_CONTROL
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
	Pause(1, identifier="EVENT_3228_pause_0"),
	JmpIfMarioInAir(["EVENT_3228_clear_bit_12"]),
	Set7000ToTappedButton(),
	JmpIf7000AllBitsClear(bits=[7], destinations=["EVENT_3228_clear_bit_12"]),
	JmpIfBitSet(TEMP_7044_0, ["EVENT_3228_start_embedded_action_script_11"]),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True, bit_7=True),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 17, ["EVENT_3228_start_embedded_action_script_11"]),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Y, pixel=True, bit_7=True),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 121, ["EVENT_3228_start_embedded_action_script_11"]),
	SetBit(TEMP_7044_5),
	SetBit(TEMP_7044_0),
	StartSyncEmbeddedActionScript(target=NPC_0, prefix=0xF1, subscript=[
		A_JumpToHeight(108)
	], identifier="EVENT_3228_start_embedded_action_script_11"),
	ClearBit(TEMP_7044_7, identifier="EVENT_3228_clear_bit_12"),
	Set7000ToPressedButton(),
	JmpIf7000AllBitsClear(bits=[6], destinations=["EVENT_3228_set_7000_to_pressed_button_16"]),
	SetBit(TEMP_7044_7),
	Set7000ToPressedButton(identifier="EVENT_3228_set_7000_to_pressed_button_16"),
	JmpIf7000AllBitsClear(bits=[0, 1, 2, 3], destinations=["EVENT_3228_pause_0"]),
	StartSyncEmbeddedActionScript(target=NPC_0, prefix=0xF1, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_JmpIfBitClear(TEMP_7044_7, ["EVENT_3228_start_embedded_action_script_18_SUBSCRIPT_set_700C_to_object_coord_3"]),
		A_SetAllSpeeds(FAST),
		A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_F, identifier="EVENT_3228_start_embedded_action_script_18_SUBSCRIPT_set_700C_to_object_coord_3"),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["EVENT_3228_start_embedded_action_script_18_SUBSCRIPT_shift_south_pixels_16"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["EVENT_3228_start_embedded_action_script_18_SUBSCRIPT_shift_southeast_pixels_14"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["EVENT_3228_start_embedded_action_script_18_SUBSCRIPT_shift_east_pixels_12"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["EVENT_3228_start_embedded_action_script_18_SUBSCRIPT_shift_northeast_pixels_26"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["EVENT_3228_start_embedded_action_script_18_SUBSCRIPT_shift_north_pixels_24"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 5, ["EVENT_3228_start_embedded_action_script_18_SUBSCRIPT_shift_northwest_pixels_22"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 6, ["EVENT_3228_start_embedded_action_script_18_SUBSCRIPT_shift_west_pixels_20"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["EVENT_3228_start_embedded_action_script_18_SUBSCRIPT_shift_southwest_pixels_18"]),
		A_WalkEastPixels(5, identifier="EVENT_3228_start_embedded_action_script_18_SUBSCRIPT_shift_east_pixels_12"),
		A_ReturnQueue(),
		A_WalkSoutheastPixels(3, identifier="EVENT_3228_start_embedded_action_script_18_SUBSCRIPT_shift_southeast_pixels_14"),
		A_ReturnQueue(),
		A_WalkSouthPixels(1, identifier="EVENT_3228_start_embedded_action_script_18_SUBSCRIPT_shift_south_pixels_16"),
		A_ReturnQueue(),
		A_WalkSouthwestPixels(3, identifier="EVENT_3228_start_embedded_action_script_18_SUBSCRIPT_shift_southwest_pixels_18"),
		A_ReturnQueue(),
		A_WalkWestPixels(5, identifier="EVENT_3228_start_embedded_action_script_18_SUBSCRIPT_shift_west_pixels_20"),
		A_ReturnQueue(),
		A_WalkNorthwestPixels(3, identifier="EVENT_3228_start_embedded_action_script_18_SUBSCRIPT_shift_northwest_pixels_22"),
		A_ReturnQueue(),
		A_WalkNorthPixels(1, identifier="EVENT_3228_start_embedded_action_script_18_SUBSCRIPT_shift_north_pixels_24"),
		A_ReturnQueue(),
		A_WalkNortheastPixels(3, identifier="EVENT_3228_start_embedded_action_script_18_SUBSCRIPT_shift_northeast_pixels_26"),
		A_ReturnQueue()
	]),
	Jmp(["EVENT_3228_pause_0"])
])
