# E1758_LANDS_END_PENULTIMATE_WHIRLPOOL_1
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
	JmpIfObjectInSpecificLevel(NPC_2, R403_LANDS_END_DESERT_AREA_05, ["EVENT_1758_copy_var_to_var_9"]),
	CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 20, ["EVENT_1759_run_event_as_subroutine_3"]),
	RunEventAsSubroutine(E1544_SAND_WHIRLPOOL, identifier="EVENT_1758_run_event_as_subroutine_3"),
	EnterArea(room_id=R319_LANDS_END_DESERT_AREA_06, face_direction=SOUTH, x=8, y=110, z=0),
	RunEventAsSubroutine(E1844_SUMMON_CLOUD_BOSS),
	SetVarToConst(ACTIVE_NPC, 21),
	RunEventAsSubroutine(E1545_SAND_WHIRLPOOL),
	JmpToEvent(E1783_LANDS_END_FINAL_WHIRLPOOL_ROOM_LOADER),
	CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000, identifier="EVENT_1758_copy_var_to_var_9"),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 20, ["EVENT_1759_run_event_as_subroutine_3"]),
	JmpIfBitSet(TEMP_7044_4, ["EVENT_1758_pause_14"], identifier="EVENT_1758_jmp_if_bit_set_11"),
	SetVarToConst(ACTIVE_NPC, 22),
	Jmp(["EVENT_1885_jmp_if_bit_set_4"]),
	Pause(1, identifier="EVENT_1758_pause_14"),
	Return(),
	Jmp(["EVENT_1759_run_event_as_subroutine_3"])
])
