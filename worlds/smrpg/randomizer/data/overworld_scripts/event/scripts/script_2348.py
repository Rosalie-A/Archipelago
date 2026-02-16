# E2348_TOWER_BULLET_BILL_ROOM_LOADER
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
	PlaySound(sound=SO000_SILENCE, channel=6),
	JmpIfObjectInCurrentLevel(NPC_4, ["EVENT_2348_jmp_if_present_in_current_level_3"]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_WalkNorthPixels(8),
		A_FaceSouthwest()
	]),
	JmpIfObjectInCurrentLevel(NPC_5, ["EVENT_2348_jmp_if_present_in_current_level_5"], identifier="EVENT_2348_jmp_if_present_in_current_level_3"),
	ActionQueueSync(target=NPC_5, subscript=[
		A_WalkWestPixels(18),
		A_FaceNortheast()
	]),
	JmpIfObjectInCurrentLevel(NPC_6, ["EVENT_2348_jmp_if_present_in_current_level_7"], identifier="EVENT_2348_jmp_if_present_in_current_level_5"),
	ActionQueueSync(target=NPC_6, subscript=[
		A_WalkNorthPixels(8),
		A_FaceSouthwest()
	]),
	JmpIfObjectInCurrentLevel(NPC_8, ["EVENT_2348_action_queue_9"], identifier="EVENT_2348_jmp_if_present_in_current_level_7"),
	ActionQueueSync(target=NPC_8, subscript=[
		A_WalkSoutheastPixels(8),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkWestPixels(20),
		A_WalkSouthPixels(4),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_VisibilityOff()
	], identifier="EVENT_2348_action_queue_9"),
	RunEventAsSubroutine(E0799_TOWER_JUMPING_SPOOKUM_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	Return()
])
