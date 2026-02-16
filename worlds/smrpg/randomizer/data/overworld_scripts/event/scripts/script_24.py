# E0024_BATTLE_RESULT_CHECK
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
	JmpIfBitSet(RUN_AWAY, ["EVENT_24_set_temp_action_script_18"]),
	JmpIfBitSet(GAME_OVER, ["EVENT_24_reset_and_choose_game_17"]),
	JmpIfBitClear(TEMP_707C_6, ["EVENT_24_jmp_if_bit_clear_5"], identifier="EVENT_24_jmp_if_bit_clear_2"),
	RemoveObjectAt70A8FromCurrentLevel(),
	Pause(1),
	JmpIfBitClear(TEMP_707C_7, ["EVENT_24_jmp_if_var_not_equals_const_9"], identifier="EVENT_24_jmp_if_bit_clear_5"),
	DisableObjectTrigger(MEM_70A8),
	RemoveObjectFromCurrentLevel(MEM_70A8),
	Pause(1),
	JmpIfVarNotEqualsConst(GAME_OVER_COUNTER_MAYBE, 255, ["EVENT_24_inc_11"], identifier="EVENT_24_jmp_if_var_not_equals_const_9"),
	SetVarToConst(GAME_OVER_COUNTER_MAYBE, 0),
	Inc(GAME_OVER_COUNTER_MAYBE, identifier="EVENT_24_inc_11"),
	JmpIfBitSet(TEMP_707C_5, ["EVENT_24_clear_bit_14"]),
	FadeInFromBlack(sync=False),
	ClearBit(TEMP_707C_5, identifier="EVENT_24_clear_bit_14"),
	ReactivateObject70A8TriggerIfMarioOnTopOfIt(identifier="EVENT_24_reactivate_trigger_if_mario_on_top_of_object_15"),
	Return(),
	ResetAndChooseGame(identifier="EVENT_24_reset_and_choose_game_17"),
	SetTempSyncActionScript(MEM_70A8, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES, identifier="EVENT_24_set_temp_action_script_18"),
	JmpIfBitSet(TEMP_707C_5, ["EVENT_24_clear_bit_14"]),
	FadeInFromBlack(sync=False),
	Jmp(["EVENT_24_reactivate_trigger_if_mario_on_top_of_object_15"])
])
