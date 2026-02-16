# E1895_ABYSS_AFTER_BOSS_1_TRAMPOLINE_BACKWARD
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
	RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
	JmpIfBitSet(ABYSS_TRAMPOLINE_DIRECTIONAL_BIT, ["EVENT_1895_set_bit_4"]),
	EnterArea(room_id=R239_SMITHY_FACTORY_AREA_06_ULTRA_HAMMER, face_direction=SOUTH, x=29, y=37, z=10, run_entrance_event=True),
	Return(),
	SetBit(ABYSS_FINAL_ROOM_TRAMPOLINE, identifier="EVENT_1895_set_bit_4"),
	JmpIfVarEqualsConst(TEMP_7026, 5, ["EVENT_1895_enter_area_17"]),
	JmpIfVarEqualsConst(TEMP_7026, 4, ["EVENT_1895_enter_area_15"]),
	JmpIfVarEqualsConst(TEMP_7026, 3, ["EVENT_1895_enter_area_13"]),
	JmpIfVarEqualsConst(TEMP_7026, 2, ["EVENT_1895_enter_area_11"]),
	EnterArea(room_id=R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS, face_direction=SOUTH, x=22, y=116, z=10, run_entrance_event=True),
	Return(),
	EnterArea(room_id=R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS, face_direction=SOUTH, x=27, y=86, z=9, run_entrance_event=True, identifier="EVENT_1895_enter_area_11"),
	Return(),
	EnterArea(room_id=R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS, face_direction=SOUTH, x=19, y=82, z=12, run_entrance_event=True, identifier="EVENT_1895_enter_area_13"),
	Return(),
	EnterArea(room_id=R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS, face_direction=SOUTH, x=25, y=72, z=12, run_entrance_event=True, identifier="EVENT_1895_enter_area_15"),
	Return(),
	EnterArea(room_id=R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS, face_direction=SOUTH, x=28, y=106, z=9, run_entrance_event=True, identifier="EVENT_1895_enter_area_17"),
	Return()
])
