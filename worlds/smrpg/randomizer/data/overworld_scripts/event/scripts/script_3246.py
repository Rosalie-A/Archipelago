# E3246_DRY_BONES_FIGHT
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
	RunEventAsSubroutine(E1604_EXP_STAR_SUBROUTINE_CANCEL_NPC_EVENT_REMOVE_FROM_LEVEL),
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 169, ["EVENT_3246_start_battle_6"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 182, ["EVENT_3246_start_battle_6"]),
	StartBattleAtBattlefield(PACK072_DRYBONES_WITH_GREAPER_REACHER, BF04_SUNKEN_SHIP),
	Jmp(["EVENT_3246_jmp_if_bit_set_7"]),
	StartBattleAtBattlefield(PACK073_DRYBONES_ALWAYS_WITH_OTHER_MONSTERS, BF04_SUNKEN_SHIP, identifier="EVENT_3246_start_battle_6"),
	JmpIfBitSet(RUN_AWAY, ["EVENT_3246_set_temp_action_script_13"], identifier="EVENT_3246_jmp_if_bit_set_7"),
	JmpIfBitSet(GAME_OVER, ["EVENT_3246_reset_and_choose_game_16"]),
	SetTempSyncActionScript(MEM_70A8, A0920_STATIC_DRY_BONES_COLLAPSE),
	ActionQueueSync(target=MARIO, subscript=[
		A_JumpToHeight(height=0, silent=True),
		A_ClearSolidityBits(cant_pass_npcs=True),
		A_ShiftZDownPixels(2),
		A_ResetProperties(),
		A_SetSolidityBits(cant_pass_npcs=True)
	]),
	FadeInFromBlack(sync=False),
	Return(),
	SetTempSyncActionScript(MEM_70A8, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES, identifier="EVENT_3246_set_temp_action_script_13"),
	FadeInFromBlack(sync=False),
	Return(),
	ResetAndChooseGame(identifier="EVENT_3246_reset_and_choose_game_16")
])
