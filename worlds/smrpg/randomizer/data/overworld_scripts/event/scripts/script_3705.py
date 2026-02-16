# E3705_JAWFUL_BATTLE
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
	StartBattleAtBattlefield(PACK099_SHAMAN_ALWAYS_WITH_OTHER_MONSTERS, BF22_NIMBUS_CASTLE),
	JmpIfBitSet(RUN_AWAY, ["EVENT_3705_set_temp_action_script_8"]),
	JmpIfBitSet(GAME_OVER, ["EVENT_3705_jmp_to_event_19"]),
	RemoveObjectAt70A8FromCurrentLevel(),
	RemoveObjectFromCurrentLevel(MEM_70A8),
	FadeInFromBlack(sync=False),
	Return(),
	SetTempSyncActionScript(MEM_70A8, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES, identifier="EVENT_3705_set_temp_action_script_8"),
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 410, ["EVENT_3705_set_temp_action_script_15"]),
	SetTempSyncActionScript(NPC_5, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
	SetTempSyncActionScript(NPC_6, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
	FadeInFromBlack(sync=False),
	Return(),
	SetTempSyncActionScript(NPC_6, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES, identifier="EVENT_3705_set_temp_action_script_15"),
	SetTempSyncActionScript(NPC_7, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
	FadeInFromBlack(sync=False),
	Return(),
	JmpToEvent(E0287_RESET_GAME, identifier="EVENT_3705_jmp_to_event_19")
])
