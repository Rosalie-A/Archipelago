# E3780_BEAN_VALLEY_2ND_VINE_ROOM_EXIT_TO_EAST_VINE_ROOM
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
	JmpIfMarioInAir(["EVENT_3584_ret_0"]),
	EnterArea(room_id=R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02, face_direction=SOUTHEAST, x=25, y=114, z=0),
	UnknownCommand(bytearray(b'\xfdI')),
	JmpToSubroutine(["EVENT_3780_jmp_if_present_in_current_level_9"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(132),
		A_WalkSoutheastSteps(2),
		A_SetSolidityBits(cant_pass_walls=True),
		A_WalkSoutheastPixels(20),
		A_SetWalkingSpeed(NORMAL)
	]),
	FadeInFromBlack(sync=False),
	Pause(1, identifier="EVENT_3780_pause_6"),
	JmpIfMarioInAir(["EVENT_3780_pause_6"]),
	Return(),
	JmpIfObjectInCurrentLevel(NPC_3, ["EVENT_3780_jmp_if_present_in_current_level_11"], identifier="EVENT_3780_jmp_if_present_in_current_level_9"),
	ActionQueueSync(target=NPC_3, subscript=[
		A_TransferXYZFPixels(x=6, y=254, z=0, direction=EAST)
	]),
	JmpIfObjectInCurrentLevel(NPC_4, ["EVENT_3780_jmp_if_present_in_current_level_13"], identifier="EVENT_3780_jmp_if_present_in_current_level_11"),
	ActionQueueSync(target=NPC_4, subscript=[
		A_TransferXYZFPixels(x=6, y=254, z=0, direction=EAST)
	]),
	JmpIfObjectInCurrentLevel(NPC_5, ["EVENT_3780_jmp_if_present_in_current_level_15"], identifier="EVENT_3780_jmp_if_present_in_current_level_13"),
	ActionQueueSync(target=NPC_5, subscript=[
		A_TransferXYZFPixels(x=6, y=254, z=0, direction=EAST)
	]),
	JmpIfObjectInCurrentLevel(NPC_6, ["EVENT_3780_jmp_if_present_in_current_level_17"], identifier="EVENT_3780_jmp_if_present_in_current_level_15"),
	ActionQueueSync(target=NPC_6, subscript=[
		A_TransferXYZFPixels(x=6, y=254, z=0, direction=EAST)
	]),
	JmpIfObjectInCurrentLevel(NPC_7, ["EVENT_3780_action_queue_19"], identifier="EVENT_3780_jmp_if_present_in_current_level_17"),
	ActionQueueSync(target=NPC_7, subscript=[
		A_TransferXYZFPixels(x=6, y=254, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_TransferXYZFPixels(x=248, y=4, z=0, direction=EAST)
	], identifier="EVENT_3780_action_queue_19"),
	JmpIfObjectNotInSpecificLevel(NPC_0, R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02, ["EVENT_3780_ret_23"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferXYZFPixels(x=248, y=4, z=0, direction=EAST),
		A_ShadowOn()
	]),
	RemoveObjectFromCurrentLevel(NPC_1),
	Return(identifier="EVENT_3780_ret_23")
])
