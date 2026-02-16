# E3318_SET_OERLIKON_PACK
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
	JmpIfBitClear(TEMP_7076_0, ["EVENT_3318_set_7000_to_current_level_2"]),
	JmpToEvent(E0255_EXP_STAR_HIT),
	Set7000ToCurrentLevel(identifier="EVENT_3318_set_7000_to_current_level_2"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 362, ["EVENT_3318_start_battle_6"]),
	StartBattleAtBattlefield(PACK104_OERLIKON_PACK_1, BF20_BARREL_VOLCANO),
	Jmp(["EVENT_3318_jmp_if_bit_set_7"]),
	StartBattleAtBattlefield(PACK105_OERLIKON_PACK_2, BF20_BARREL_VOLCANO, identifier="EVENT_3318_start_battle_6"),
	JmpIfBitSet(RUN_AWAY, ["EVENT_3319_set_temp_action_script_14"], identifier="EVENT_3318_jmp_if_bit_set_7"),
	JmpIfBitSet(GAME_OVER, ["EVENT_3319_reset_and_choose_game_17"]),
	PauseActionScript(MEM_70A8),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_VisibilityOff(),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_Pause(1)
	]),
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	AddConstToVar(PRIMARY_TEMP_7000, 7),
	ClearMem704XAt7000Bit(),
	FadeInFromBlack(sync=False),
	Return()
])
