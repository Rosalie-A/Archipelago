# E1705_BANDITS_WAY_2_DOGS_BACKGROUND
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
	Pause(1, identifier="EVENT_1705_pause_0"),
	JmpIfMarioInAir(["EVENT_1705_clear_bit_3"]),
	Jmp(["EVENT_1705_pause_0"]),
	ClearBit(TEMP_7043_5, identifier="EVENT_1705_clear_bit_3"),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_1705_pause_13"]),
	SetBit(TEMP_7043_1),
	ClearBit(TEMP_7043_2),
	SetVarToConst(TEMP_70AB, 20),
	StartLoopNTimes(1),
	JmpIfObjectInCurrentLevel(MEM_70AB, ["EVENT_1705_inc_11"]),
	SetSyncActionScript(MEM_70AB, A0474_BANDITS_WAY_2_CHEST_ROOM_CHEST),
	Inc(TEMP_70AB, identifier="EVENT_1705_inc_11"),
	EndLoop(),
	Pause(1, identifier="EVENT_1705_pause_13"),
	JmpIfMarioInAir(["EVENT_1705_pause_13"]),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True, bit_7=True),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1705_pause_0"]),
	JmpIfBitSet(TEMP_7043_2, ["EVENT_1705_pause_0"]),
	SetBit(TEMP_7043_2),
	ClearBit(TEMP_7043_1),
	SetVarToConst(TEMP_70AB, 20),
	StartLoopNTimes(1),
	JmpIfObjectInCurrentLevel(MEM_70AB, ["EVENT_1705_inc_24"]),
	SetSyncActionScript(MEM_70AB, A0475_CHOW_UNKNOWN),
	Inc(TEMP_70AB, identifier="EVENT_1705_inc_24"),
	EndLoop(),
	Jmp(["EVENT_1705_pause_0"])
])
