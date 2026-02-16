# E2466_BEAN_VALLEY_1ST_ROOM_LOADER
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
	SummonObjectToSpecificLevel(NPC_0, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
	SummonObjectToSpecificLevel(NPC_1, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
	SummonObjectToSpecificLevel(NPC_3, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
	SummonObjectToSpecificLevel(NPC_4, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
	SummonObjectToSpecificLevel(NPC_5, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
	SummonObjectToSpecificLevel(NPC_6, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
	SummonObjectToSpecificLevel(NPC_7, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
	SummonObjectToSpecificLevel(NPC_9, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
	SummonObjectToSpecificLevel(NPC_10, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
	SummonObjectToSpecificLevel(NPC_11, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
	ClearBit(DIRECTIONAL_7047_0),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True, bit_7=True),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_2466_set_7000_to_object_coord_19"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_2466_action_queue_33"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_2466_set_7000_to_object_coord_22"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 9, ["EVENT_2466_action_queue_25"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 13, ["EVENT_2466_action_queue_29"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 16, ["EVENT_2466_action_queue_29"]),
	Jmp(["EVENT_2466_fade_in_from_black_async_36"]),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Y, pixel=True, bit_7=True, identifier="EVENT_2466_set_7000_to_object_coord_19"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 70, ["EVENT_2466_action_queue_33"]),
	Jmp(["EVENT_2466_action_queue_25"]),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Y, pixel=True, bit_7=True, identifier="EVENT_2466_set_7000_to_object_coord_22"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 75, ["EVENT_2466_action_queue_33"]),
	Jmp(["EVENT_2466_action_queue_25"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShiftToXYCoords(x=8, y=112),
		A_JmpIfRandom1of2(["EVENT_2466_action_queue_25_SUBSCRIPT_face_southeast_4"]),
		A_FaceSouthwest(),
		A_ReturnQueue(),
		A_FaceSoutheast(identifier="EVENT_2466_action_queue_25_SUBSCRIPT_face_southeast_4")
	], identifier="EVENT_2466_action_queue_25"),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ShiftToXYCoords(x=6, y=111),
		A_JmpIfRandom1of2(["EVENT_2466_action_queue_26_SUBSCRIPT_face_southeast_4"]),
		A_FaceSouthwest(),
		A_ReturnQueue(),
		A_FaceSoutheast(identifier="EVENT_2466_action_queue_26_SUBSCRIPT_face_southeast_4")
	]),
	RemoveObjectFromCurrentLevel(NPC_1),
	Jmp(["EVENT_2466_fade_in_from_black_async_36"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShiftToXYCoords(x=15, y=72),
		A_JmpIfRandom1of2(["EVENT_2466_action_queue_29_SUBSCRIPT_face_southeast_4"]),
		A_FaceSouthwest(),
		A_ReturnQueue(),
		A_FaceSoutheast(identifier="EVENT_2466_action_queue_29_SUBSCRIPT_face_southeast_4")
	], identifier="EVENT_2466_action_queue_29"),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=13, y=70),
		A_JmpIfRandom1of2(["EVENT_2466_action_queue_30_SUBSCRIPT_face_southeast_4"]),
		A_FaceSouthwest(),
		A_ReturnQueue(),
		A_FaceSoutheast(identifier="EVENT_2466_action_queue_30_SUBSCRIPT_face_southeast_4")
	]),
	RemoveObjectFromCurrentLevel(NPC_2),
	Jmp(["EVENT_2466_fade_in_from_black_async_36"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShiftToXYCoords(x=5, y=72),
		A_FaceSoutheast()
	], identifier="EVENT_2466_action_queue_33"),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=8, y=82),
		A_JmpIfRandom1of2(["EVENT_2466_action_queue_34_SUBSCRIPT_face_southeast_4"]),
		A_FaceSouthwest(),
		A_ReturnQueue(),
		A_FaceSoutheast(identifier="EVENT_2466_action_queue_34_SUBSCRIPT_face_southeast_4")
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ShiftToXYCoords(x=7, y=88),
		A_JmpIfRandom1of2(["EVENT_2466_action_queue_35_SUBSCRIPT_face_southeast_4"]),
		A_FaceSouthwest(),
		A_ReturnQueue(),
		A_FaceSoutheast(identifier="EVENT_2466_action_queue_35_SUBSCRIPT_face_southeast_4")
	]),
	FadeInFromBlack(sync=False, identifier="EVENT_2466_fade_in_from_black_async_36"),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_2466_ret_41"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2466_ret_41"]),
	RunEventAsSubroutine(E3911_BEAN_VALLEY_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_2466_ret_41")
])
