# E3706_ACTIVATE_JAWFUL_EXTENDED_HITBOXES
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
	JmpIfBitClear(TEMP_7043_0, ["EVENT_3584_ret_0"]),
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 114, ["EVENT_3706_jmp_if_object_not_in_level_16"]),
	JmpIfObjectNotInSpecificLevel(NPC_5, R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE, ["EVENT_3584_ret_0"]),
	StartBattleAtBattlefield(PACK099_SHAMAN_ALWAYS_WITH_OTHER_MONSTERS, BF22_NIMBUS_CASTLE),
	JmpIfBitSet(GAME_OVER, ["EVENT_3705_jmp_to_event_19"]),
	JmpIfBitSet(RUN_AWAY, ["EVENT_3706_set_temp_action_script_28"]),
	RemoveObjectFromCurrentLevel(NPC_5),
	RemoveObjectFromCurrentLevel(NPC_6),
	RemoveObjectFromCurrentLevel(NPC_7),
	RemoveObjectFromSpecificLevel(NPC_5, R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE),
	RemoveObjectFromSpecificLevel(NPC_6, R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE),
	RemoveObjectFromSpecificLevel(NPC_7, R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE),
	FadeInFromBlack(sync=False),
	Return(),
	JmpIfObjectNotInSpecificLevel(NPC_4, R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM, ["EVENT_3584_ret_0"], identifier="EVENT_3706_jmp_if_object_not_in_level_16"),
	StartBattleAtBattlefield(PACK099_SHAMAN_ALWAYS_WITH_OTHER_MONSTERS, BF22_NIMBUS_CASTLE),
	JmpIfBitSet(GAME_OVER, ["EVENT_3705_jmp_to_event_19"]),
	JmpIfBitSet(RUN_AWAY, ["EVENT_3706_set_temp_action_script_28"]),
	RemoveObjectFromCurrentLevel(NPC_4),
	RemoveObjectFromCurrentLevel(NPC_5),
	RemoveObjectFromCurrentLevel(NPC_6),
	RemoveObjectFromSpecificLevel(NPC_4, R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_5, R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_6, R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM),
	FadeInFromBlack(sync=False),
	Return(),
	SetTempSyncActionScript(MEM_70A8, A0889_JAWFUL_EXTENDED_HITBOXES, identifier="EVENT_3706_set_temp_action_script_28"),
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 410, ["EVENT_3706_set_temp_action_script_34"]),
	SetTempSyncActionScript(NPC_4, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
	FadeInFromBlack(sync=False),
	Return(),
	SetTempSyncActionScript(NPC_5, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES, identifier="EVENT_3706_set_temp_action_script_34"),
	FadeInFromBlack(sync=False),
	Return()
])
