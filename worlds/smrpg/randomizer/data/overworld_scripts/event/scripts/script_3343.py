# E3343_VOLCANO_FINAL_BOSS_PATH_ROOM_LOADER
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
	JmpIfBitSet(VOLCANO_PENULTIMATE_ROOM_ANIMATION_COMPLETED, ["EVENT_3343_ret_7"]),
	SetBit(VOLCANO_PENULTIMATE_ROOM_ANIMATION_COMPLETED),
	ActionQueueSync(target=NPC_0, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\xf2')),
		A_Walk1StepSouthwest(),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\xf2')),
		A_WalkSouthwestSteps(2),
		A_VisibilityOff()
	], identifier="axem_henchman_1_aq_2"),
	ActionQueueSync(target=NPC_2, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\xf2')),
		A_WalkSouthwestSteps(3),
		A_VisibilityOff()
	], identifier="axem_henchman_2_aq_2"),
	ActionQueueSync(target=NPC_3, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\xf2')),
		A_WalkSouthwestSteps(4),
		A_VisibilityOff()
	], identifier="axem_henchman_3_aq_2"),
	ActionQueueSync(target=NPC_4, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\xf2')),
		A_WalkSouthwestSteps(5),
		A_VisibilityOff()
	], identifier="axem_henchman_4_aq_2"),
	Return(identifier="EVENT_3343_ret_7")
])
