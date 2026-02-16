# E2118_INITIATE_STATUE_POLISHER_MANUAL_BOSS_FIGHT
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
	EnableControlsUntilReturn([]),
	SetVarToConst(PRIMARY_TEMP_7000, 520),
	RunEventAsSubroutine(E0353_BOSS_BATTLE),
	JmpIfBitClear(GAME_OVER, ["EVENT_2118_remove_from_level_5"]),
	ResetAndChooseGame(),
	RemoveObjectFromSpecificLevel(NPC_2, R112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT, identifier="EVENT_2118_remove_from_level_5"),
	RemoveObjectFromCurrentLevel(NPC_2),
	FadeInFromBlack(sync=False),
	ClearBit(STATUE_KEEPER_FIGHT_PRESENT),
	JmpIfBitSet(STATUE_KEEPER_STAR_PIECE, ["EVENT_2118_ret_13"]),
	SetBit(STATUE_KEEPER_STAR_PIECE),
	RunEventAsSubroutine(E1230_STATUE_BOSS_UNLOCKS),
	SetVarToConst(PRIMARY_TEMP_7000, 520),
	JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE),
	Return(identifier="EVENT_2118_ret_13")
])
