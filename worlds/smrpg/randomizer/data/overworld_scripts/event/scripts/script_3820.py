# E3820_FORCED_TOWER_BOSS_1_FIGHT
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
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	JmpIfBitClear(GAME_OVER, ["EVENT_3820_remove_from_level_4"]),
	ResetAndChooseGame(),
	RemoveObjectFromSpecificLevel(NPC_7, R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, identifier="EVENT_3820_remove_from_level_4"),
	RemoveObjectFromCurrentLevel(NPC_7),
	FadeInFromBlack(sync=False),
    JmpIfBitSet(CURTAIN_MINIGAME_COMPLETED, ["EVENT_3820_sp_doublecheck"]),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	JmpIfBitSet(TOWER_BOSS_1_STAR_PIECE, ["EVENT_3820_ret_10"], identifier="EVENT_3820_sp_doublecheck"),
	SetBit(TOWER_BOSS_1_STAR_PIECE),
    RunEventAsSubroutine(E0225_CHECK_VOUCHER_UNLOCK),
	RunEventAsSubroutine(E1201_TOWER_CURTAIN_BOSS_UNLOCKS),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
	Return(identifier="EVENT_3820_ret_10")
])
