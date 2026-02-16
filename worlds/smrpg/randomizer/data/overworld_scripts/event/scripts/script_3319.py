# E3319_SET_VOMER_PACK
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
	JmpIfBitClear(TEMP_7076_0, ["EVENT_3319_set_7000_to_current_level_2"]),
	JmpToEvent(E0255_EXP_STAR_HIT),
	Set7000ToCurrentLevel(identifier="EVENT_3319_set_7000_to_current_level_2"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 367, ["EVENT_3319_start_battle_7"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 364, ["EVENT_3319_start_battle_7"]),
	StartBattleAtBattlefield(PACK108_VOMER_PACK_1, BF20_BARREL_VOLCANO),
	Jmp(["EVENT_3319_jmp_if_bit_set_8"]),
	StartBattleAtBattlefield(PACK109_VOMER_PACK_2, BF20_BARREL_VOLCANO, identifier="EVENT_3319_start_battle_7"),
	JmpIfBitSet(RUN_AWAY, ["EVENT_3319_set_temp_action_script_14"], identifier="EVENT_3319_jmp_if_bit_set_8"),
	JmpIfBitSet(GAME_OVER, ["EVENT_3319_reset_and_choose_game_17"]),
	SetTempSyncActionScript(MEM_70A8, A0273_VOLCANO_DRY_BONES_COLLAPSE),
	ActionQueueSync(target=MARIO, subscript=[
		A_JumpToHeight(height=0, silent=True),
		A_ClearSolidityBits(cant_pass_npcs=True),
		A_ShiftZDownPixels(2),
		A_ResetProperties(),
		A_SetSolidityBits(cant_pass_npcs=True)
	]),
	FadeInFromBlack(sync=False),
	Return(),
	SetTempSyncActionScript(MEM_70A8, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES, identifier="EVENT_3319_set_temp_action_script_14"),
	FadeInFromBlack(sync=False),
	Return(),
	ResetAndChooseGame(identifier="EVENT_3319_reset_and_choose_game_17")
])
