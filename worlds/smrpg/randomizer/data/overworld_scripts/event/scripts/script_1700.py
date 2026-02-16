# E1700_BANDITS_WAY_2_LEFT_PLATFORM
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
	JmpIfBitSet(TEMP_7043_5, ["EVENT_1700_ret_26"]),
	PlaySound(sound=SO058_INSERT, channel=6),
	SetBit(TEMP_7043_5),
	EnableControlsUntilReturn([]),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_1700_pause_action_script_9"]),
	SetBit(TEMP_7043_3),
	SetBit(TEMP_7043_1),
	ClearBit(TEMP_7043_2),
	RunBackgroundEvent(event_id=E1705_BANDITS_WAY_2_DOGS_BACKGROUND, return_on_level_exit=True),
	PauseActionScript(NPC_6, identifier="EVENT_1700_pause_action_script_9"),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True, bit_7=True),
	CompareVarToConst(PRIMARY_TEMP_7000, 12),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1700_compare_var_to_const_14"]),
	Return(),
	CompareVarToConst(PRIMARY_TEMP_7000, 15, identifier="EVENT_1700_compare_var_to_const_14"),
	JmpIfComparisonResultIsLesser(["EVENT_1700_copy_var_to_var_17"]),
	Return(),
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_7000, identifier="EVENT_1700_copy_var_to_var_17"),
	CompareVarToConst(PRIMARY_TEMP_7000, 26),
	JmpIfLoadedMemoryIsNot0(["EVENT_1700_set_var_to_const_21"]),
	AddConstToVar(SECONDARY_TEMP_7024, 128),
	SetVarToConst(TEMP_70A9, 26, identifier="EVENT_1700_set_var_to_const_21"),
	SetVarToConst(ROSE_WAY_703E, 26),
	SetSyncActionScript(NPC_7, A0478_BANDITS_WAY_1ST_PLATFORMS_SWING),
	Pause(34),
	SetSyncActionScript(NPC_7, A0477_BANDITS_WAY_1ST_PLATFORMS_STATIC),
	Return(identifier="EVENT_1700_ret_26")
])
