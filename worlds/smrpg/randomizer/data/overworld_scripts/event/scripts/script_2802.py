# E2802_BEAN_VALLEY_TOP_PIPE_BASEMENT_LOADER
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
	Pause(1, identifier="EVENT_2802_pause_0"),
	JmpIfBitClear(TEMP_7043_0, ["EVENT_2802_pause_0"]),
	Set7000ToTappedButton(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_2802_copy_var_to_var_5"]),
	Jmp(["EVENT_2802_pause_0"]),
	CopyVarToVar(from_var=TEMP_70AE, to_var=PRIMARY_TEMP_7000, identifier="EVENT_2802_copy_var_to_var_5"),
	CompareVarToConst(PRIMARY_TEMP_7000, 2),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_2802_jmp_if_bit_clear_14"]),
	Inc(TEMP_70AE),
	JmpIfBitClear(KNIFE_GUY_PRIZE_GRANTED, ["EVENT_2802_pause_11"]),
	PlaySound(sound=SO014_FLOWER, channel=6),
	Pause(1, identifier="EVENT_2802_pause_11"),
	JmpIfMarioInAir(["EVENT_2802_pause_11"]),
	Jmp(["EVENT_2802_pause_0"]),
	JmpIfBitClear(KNIFE_GUY_PRIZE_GRANTED, ["EVENT_2802_summon_to_level_16"], identifier="EVENT_2802_jmp_if_bit_clear_14"),
	PlaySound(sound=SO014_FLOWER, channel=6),
	SummonObjectToSpecificLevel(NPC_4, R347_BEAN_VALLEY_PIPE_ROOM_TOP_PIPE_LEADS_TO_GRATE_GUYS_CASINO, identifier="EVENT_2802_summon_to_level_16"),
	SummonObjectToCurrentLevel(NPC_4),
	ApplyTileModToLevel(use_alternate=True, room_id=R347_BEAN_VALLEY_PIPE_ROOM_TOP_PIPE_LEADS_TO_GRATE_GUYS_CASINO, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R347_BEAN_VALLEY_PIPE_ROOM_TOP_PIPE_LEADS_TO_GRATE_GUYS_CASINO, mod_id=0),
	Return()
])
