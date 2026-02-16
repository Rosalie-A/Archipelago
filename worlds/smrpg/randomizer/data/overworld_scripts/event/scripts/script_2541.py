# E2541_BEAN_VALLEY_TOP_PIPE_BASEMENT_LOADER
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
	PlaySound(sound=SO019_LONG_FALL, channel=6),
	FreezeCamera(),
	ActionQueueSync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZUpSteps(11),
		A_SetWalkingSpeed(NORMAL),
		A_FloatingOn()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthwestPixels(8)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthwestPixels(6),
		A_SetWalkingSpeed(SLOW)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSoutheastPixels(3),
		A_WalkSouthwestPixels(4),
		A_SetWalkingSpeed(SLOW)
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthwestPixels(8),
		A_WalkNortheastPixels(6)
	]),
	SetSyncActionScript(NPC_1, A0405_FOREST_MAZE_AREA_FREEMOVING_AMANITA),
	SetSyncActionScript(NPC_2, A0846_VALLEY_TOP_PIPE_RIGHT_GECKO),
	SetSyncActionScript(NPC_3, A0847_VALLEY_TOP_PIPE_MID_GECKO),
	SetSyncActionScript(NPC_5, A0194_BEAN_VALLEY_CHOMP),
	FadeInFromBlack(sync=False),
	JmpIfObjectInSpecificLevel(NPC_4, R347_BEAN_VALLEY_PIPE_ROOM_TOP_PIPE_LEADS_TO_GRATE_GUYS_CASINO, ["EVENT_2541_action_queue_14"]),
	RunBackgroundEvent(event_id=E2802_BEAN_VALLEY_TOP_PIPE_BASEMENT_LOADER, return_on_level_exit=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(height=0, silent=True),
		A_Pause(1, identifier="EVENT_2541_action_queue_14_SUBSCRIPT_pause_1"),
		A_JmpIfMarioInAir(["EVENT_2541_action_queue_14_SUBSCRIPT_pause_1"]),
		A_PlaySound(sound=SO058_INSERT, channel=4)
	], identifier="EVENT_2541_action_queue_14"),
	UnfreezeCamera(),
	Return()
])
