# E1346_TOWER_HENCHMAN_2
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
	RunEventAsSubroutine(E1603_EXP_STAR_SUBROUTINE_CANCEL_TILE_EVENT),
	JmpIfObjectNotInSpecificLevel(NPC_0, R194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM, ["EVENT_1346_ret_16"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetAllSpeeds(FAST),
		A_TransferToXYZF(x=2, y=106, z=0, direction=EAST),
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetAllSpeeds(FAST),
		A_TransferToXYZF(x=1, y=105, z=0, direction=EAST),
		A_VisibilityOn(),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FixedFCoordOn(),
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSoutheastSteps(3)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FixedFCoordOn(),
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSoutheastSteps(3)
	]),
	Pause(30),
	RunDialog(dialog_id=DI2572_TOWER_HENCHMAN_2, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Pause(5),
	RunEventAsSubroutine(E1186_HENCHMAN_BATTLE_PACK_SELECTOR),
	JmpIfBitClear(GAME_OVER, ["EVENT_1346_remove_from_current_level_12"]),
	ResetAndChooseGame(),
	RemoveObjectFromCurrentLevel(NPC_0, identifier="EVENT_1346_remove_from_current_level_12"),
	RemoveObjectFromSpecificLevel(NPC_0, R194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	FadeInFromBlack(sync=False),
	Return(identifier="EVENT_1346_ret_16")
])
