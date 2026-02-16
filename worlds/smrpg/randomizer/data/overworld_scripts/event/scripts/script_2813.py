# E2813_MUSHROOM_WAY_3_SUMMON_SPINYS
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
	Pause(3, identifier="EVENT_2813_pause_0"),
	JmpIfBitSet(TEMP_7043_7, ["EVENT_2813_jmp_20"]),
	JmpIfBitClear(TEMP_7043_0, ["EVENT_2813_jmp_20"]),
	ClearBit(TEMP_7043_0),
	JmpIfObjectNotInSpecificLevel(NPC_0, R205_MUSHROOM_WAY_AREA_03, ["EVENT_2813_summon_to_level_16"]),
	JmpIfObjectNotInSpecificLevel(NPC_1, R205_MUSHROOM_WAY_AREA_03, ["EVENT_2813_summon_to_level_12"]),
	JmpIfObjectNotInSpecificLevel(NPC_2, R205_MUSHROOM_WAY_AREA_03, ["EVENT_2813_summon_to_level_8"]),
	Jmp(["EVENT_2813_jmp_20"]),
	SummonObjectToSpecificLevel(NPC_2, R205_MUSHROOM_WAY_AREA_03, identifier="EVENT_2813_summon_to_level_8"),
	SetSyncActionScript(NPC_2, A0196_SPIKEY_BANDITS_WAY),
	SetTempSyncActionScript(NPC_6, A0556_BOOSTER_PASS_LAKITU_TOSSING),
	Jmp(["EVENT_2813_pause_19"]),
	SummonObjectToSpecificLevel(NPC_1, R205_MUSHROOM_WAY_AREA_03, identifier="EVENT_2813_summon_to_level_12"),
	SetSyncActionScript(NPC_1, A0196_SPIKEY_BANDITS_WAY),
	SetTempSyncActionScript(NPC_6, A0556_BOOSTER_PASS_LAKITU_TOSSING),
	Jmp(["EVENT_2813_pause_19"]),
	SummonObjectToSpecificLevel(NPC_0, R205_MUSHROOM_WAY_AREA_03, identifier="EVENT_2813_summon_to_level_16"),
	SetSyncActionScript(NPC_0, A0196_SPIKEY_BANDITS_WAY),
	SetTempSyncActionScript(NPC_6, A0556_BOOSTER_PASS_LAKITU_TOSSING),
	Pause(32, identifier="EVENT_2813_pause_19"),
	Jmp(["EVENT_2813_pause_0"], identifier="EVENT_2813_jmp_20")
])
