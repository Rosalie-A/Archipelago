# E3326_STUMPET_ERUPTION
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
	ClearBit(TEMP_7043_0, identifier="EVENT_3326_clear_bit_0"),
	Pause(1),
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 390, ["EVENT_3326_jmp_if_object_not_in_level_9"]),
	JmpIfObjectNotInSpecificLevel(NPC_6, R386_VOLCANO_AREA_12_ERUPTING_STUMPET, ["EVENT_3326_set_var_to_const_14"]),
	JmpIfObjectNotInSpecificLevel(NPC_7, R386_VOLCANO_AREA_12_ERUPTING_STUMPET, ["EVENT_3326_set_var_to_const_16"]),
	JmpIfObjectNotInSpecificLevel(NPC_8, R386_VOLCANO_AREA_12_ERUPTING_STUMPET, ["EVENT_3326_set_var_to_const_18"]),
	JmpIfObjectNotInSpecificLevel(NPC_9, R386_VOLCANO_AREA_12_ERUPTING_STUMPET, ["EVENT_3326_set_var_to_const_20"]),
	Jmp(["EVENT_3326_clear_bit_0"]),
	JmpIfObjectNotInSpecificLevel(NPC_6, R390_VOLCANO_AREA_16_ERUPTING_STUMPET, ["EVENT_3326_set_var_to_const_14"], identifier="EVENT_3326_jmp_if_object_not_in_level_9"),
	JmpIfObjectNotInSpecificLevel(NPC_7, R390_VOLCANO_AREA_16_ERUPTING_STUMPET, ["EVENT_3326_set_var_to_const_16"]),
	JmpIfObjectNotInSpecificLevel(NPC_8, R390_VOLCANO_AREA_16_ERUPTING_STUMPET, ["EVENT_3326_set_var_to_const_18"]),
	JmpIfObjectNotInSpecificLevel(NPC_9, R390_VOLCANO_AREA_16_ERUPTING_STUMPET, ["EVENT_3326_set_var_to_const_20"]),
	Jmp(["EVENT_3326_clear_bit_0"]),
	SetVarToConst(TEMP_70AA, 26, identifier="EVENT_3326_set_var_to_const_14"),
	Jmp(["EVENT_3326_pause_21"]),
	SetVarToConst(TEMP_70AA, 27, identifier="EVENT_3326_set_var_to_const_16"),
	Jmp(["EVENT_3326_pause_21"]),
	SetVarToConst(TEMP_70AA, 28, identifier="EVENT_3326_set_var_to_const_18"),
	Jmp(["EVENT_3326_pause_21"]),
	SetVarToConst(TEMP_70AA, 29, identifier="EVENT_3326_set_var_to_const_20"),
	Pause(60, identifier="EVENT_3326_pause_21"),
	CopyVarToVar(from_var=TEMP_70AA, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ACTIVE_NPC),
	SummonObjectAt70A8ToCurrentLevel(),
	SetBit(TEMP_7043_0),
	SetSyncActionScript(MEM_70AA, A0933_ERUPT),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\x9c\x15')),
		A_StartLoopNTimes(33),
		A_WalkNorthPixels(1),
		A_WalkSouthPixels(1),
		A_EndLoop()
	]),
	Pause(68),
	Jmp(["EVENT_3326_clear_bit_0"])
])
