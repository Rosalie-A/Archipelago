# E2627_FACTORY_3RD_BOSS_FIGHT
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
	JmpIfObjectNotInSpecificLevel(NPC_10, R472_FACTORY_GROUNDS_AREA_03, ["EVENT_2627_ret_15"]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkToXYCoords(x=7, y=88)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(1, identifier="EVENT_2627_action_queue_2_SUBSCRIPT_pause_0"),
		A_JmpIfMarioInAir(["EVENT_2627_action_queue_2_SUBSCRIPT_pause_0"]),
		A_WalkToXYCoords(x=11, y=113),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkSoutheastSteps(7)
	]),
	Pause(32),
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	JmpIfBitClear(GAME_OVER, ["EVENT_2627_restore_all_hp_8"]),
	ResetAndChooseGame(),
	RestoreAllHP(identifier="EVENT_2627_restore_all_hp_8"),
	RestoreAllFP(),
	StopEmbeddedActionScript(NPC_10),
	RemoveObjectFromSpecificLevel(NPC_10, R472_FACTORY_GROUNDS_AREA_03),
	RemoveObjectFromCurrentLevel(NPC_10),
	FadeInFromBlack(sync=False),
	RunEventAsSubroutine(E1243_INNER_FACTORY_3_BOSS_UNLOCKS),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
	Return(identifier="EVENT_2627_ret_15")
])
