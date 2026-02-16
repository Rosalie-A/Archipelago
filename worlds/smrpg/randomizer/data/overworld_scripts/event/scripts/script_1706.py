# E1706_BANDITS_WAY_LEFT_CHEST_STAR_CHECK
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
	Pause(20),
	JmpIfBitSet(TEMP_7076_0, ["EVENT_1706_pause_3"]),
	Return(),
	Pause(1, identifier="EVENT_1706_pause_3"),
	JmpIfBitClear(TEMP_7076_0, ["EVENT_1706_pause_16"]),
	SetVarToConst(TEMP_70AB, 22),
	StartLoopNTimes(3),
	JmpIfObjectInCurrentLevel(MEM_70AB, ["EVENT_1706_pause_9"]),
	Jmp(["EVENT_1706_inc_12"]),
	Pause(1, identifier="EVENT_1706_pause_9"),
	SummonObjectToSpecificLevel(MEM_70AB, R078_BANDITS_WAY_AREA_04),
	SetSyncActionScript(MEM_70AB, A0471_BANDITS_WAY_2_CHEST_ROOM_CHEST),
	Inc(TEMP_70AB, identifier="EVENT_1706_inc_12"),
	EndLoop(),
	Pause(3),
	Jmp(["EVENT_1706_pause_3"]),
	Pause(1, identifier="EVENT_1706_pause_16"),
	SetVarToConst(TEMP_70AB, 22),
	StartLoopNTimes(3),
	JmpIfObjectNotInSpecificLevel(MEM_70AB, R078_BANDITS_WAY_AREA_04, ["EVENT_1706_inc_23"]),
	PauseActionScript(MEM_70AB),
	ResetCoords(MEM_70AB),
	SetSyncActionScript(MEM_70AB, A0474_BANDITS_WAY_2_CHEST_ROOM_CHEST),
	Inc(TEMP_70AB, identifier="EVENT_1706_inc_23"),
	EndLoop(),
	Return()
])
