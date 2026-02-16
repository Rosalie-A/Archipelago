# E1722_SKY_BRIDGE_ROOM_LOADER
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
	JmpIfBitSet(FLOWER_TOWER_ASCENDED, ["EVENT_1722_action_queue_2"]),
	RemoveObjectFromCurrentLevel(NPC_18),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ShiftZUpPixels(1)
	], identifier="EVENT_1722_action_queue_2"),
	ActionQueueSync(target=NPC_3, subscript=[
		A_ShiftZUpPixels(1)
	]),
	FadeInFromBlack(sync=True),
	JmpIfBitClear(TEMP_7044_0, ["EVENT_1722_jmp_if_bit_clear_8"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_JumpToHeight(height=128, silent=True),
		A_Walk1StepSouth(),
		A_FloatingOn(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_Pause(1, identifier="EVENT_1722_action_queue_6_SUBSCRIPT_pause_9"),
		A_JmpIfMarioInAir(["EVENT_1722_action_queue_6_SUBSCRIPT_pause_9"]),
		A_PlaySound(sound=SO058_INSERT, channel=4)
	]),
	Jmp(["EVENT_1722_set_action_script_10"]),
	JmpIfBitClear(TEMP_7043_7, ["EVENT_1722_set_action_script_10"], identifier="EVENT_1722_jmp_if_bit_clear_8"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_JumpToHeight(height=108, silent=True),
		A_Walk1StepSouth(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_Pause(1, identifier="EVENT_1722_action_queue_9_SUBSCRIPT_pause_6"),
		A_JmpIfMarioInAir(["EVENT_1722_action_queue_9_SUBSCRIPT_pause_6"]),
		A_PlaySound(sound=SO058_INSERT, channel=4)
	]),
	SetSyncActionScript(MARIO, A0823_PLAYER_RESET_IN_SKY_BRIDGE_ROOM, identifier="EVENT_1722_set_action_script_10"),
	SetBit(SKY_BRIDGE_COURSE_CHOICE),
	SetBit(SKY_BRIDGE_COURSE_1_CHOSEN),
	SetVarToConst(TEMP_702E, 48),
	SetVarToConst(TEMP_702C, 70),
	ActionQueueSync(target=NPC_16, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthPixels(16),
		A_Pause(300, identifier="EVENT_1722_action_queue_15_SUBSCRIPT_pause_2"),
		A_ShiftZDownPixels(16),
		A_Pause(1, identifier="EVENT_1722_action_queue_15_SUBSCRIPT_pause_4"),
		A_SetVarToConst(TEMP_7034, 32774),
		A_CreatePacketAtObjectCoords(packet=P032_BLUE_CLOUD, target_npc=DUMMY_0X07, destinations=["EVENT_1722_action_queue_15_SUBSCRIPT_pause_4"]),
		A_Pause(120),
		A_ShiftZUpPixels(16),
		A_Jmp(["EVENT_1722_action_queue_15_SUBSCRIPT_pause_2"])
	]),
	Return()
])
