# E1909_ABYSS_CONVEYOR_BELT_JABIT_OR_BOWYER
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
	FreezeAllNPCsUntilReturn(),
	JmpIfRandom1of2(["EVENT_1909_set_var_to_const_4"]),
	SetVarToConst(BATTLE_PACK_ID, 136),
	Jmp(["EVENT_1909_start_battle_700E_5"]),
	SetVarToConst(BATTLE_PACK_ID, 137, identifier="EVENT_1909_set_var_to_const_4"),
	StartBattleWithPackAt700E(identifier="EVENT_1909_start_battle_700E_5"),
	JmpIfBitSet(RUN_AWAY, ["EVENT_1909_disable_trigger_10"]),
	JmpIfBitSet(GAME_OVER, ["EVENT_1695_reset_and_choose_game_12"]),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_VisibilityOff()
	]),
	SetBit(UNKNOWN_704D_0),
	DisableObjectTrigger(MEM_70A8, identifier="EVENT_1909_disable_trigger_10"),
	ResumeActionScript(MEM_70A8),
	UnfreezeAllNPCs(),
	FadeInFromBlack(sync=False),
	SetVarToConst(TIMER_701C, 2),
	Return()
])
