# E2483_BEAN_VALLEY_LEFTMOST_PIRANHA
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
	JmpIfRandom1of2(["EVENT_2483_start_battle_3"]),
	StartBattleAtBattlefield(PACK088_CHEWY_WITH_SHYAWAY_OR_SPINTHRA, BF41_BEAN_VALLEY_GRASSLANDS),
	Jmp(["EVENT_2483_jmp_if_bit_set_4"]),
	StartBattleAtBattlefield(PACK089_CHEWY_ALWAYS_WITH_OTHER_MONSTERS, BF41_BEAN_VALLEY_GRASSLANDS, identifier="EVENT_2483_start_battle_3"),
	JmpIfBitSet(RUN_AWAY, ["EVENT_2483_set_temp_action_script_12"], identifier="EVENT_2483_jmp_if_bit_set_4"),
	JmpIfBitSet(GAME_OVER, ["EVENT_2483_reset_and_choose_game_15"]),
	RemoveObjectFromSpecificLevel(NPC_5, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
	RemoveObjectFromSpecificLevel(NPC_11, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
	RemoveObjectFromCurrentLevel(NPC_5),
	RemoveObjectFromCurrentLevel(NPC_11),
	FadeInFromBlack(sync=False),
	Return(),
	SetTempSyncActionScript(NPC_11, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES, identifier="EVENT_2483_set_temp_action_script_12"),
	FadeInFromBlack(sync=False),
	Return(),
	ResetAndChooseGame(identifier="EVENT_2483_reset_and_choose_game_15"),
	Return()
])
