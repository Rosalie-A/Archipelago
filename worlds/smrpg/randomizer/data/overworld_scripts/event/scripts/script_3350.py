# E3350_KEEP_ALL_DOOR_PATHS_EXIT_TO_REWARD_ROOM
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
	FadeOutToBlack(sync=False),
	EnableObjectTriggerInSpecificLevel(NPC_0, R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM),
	EnableObjectTriggerInSpecificLevel(NPC_0, R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS),
	CopyVarToVar(from_var=KEEP_DOORS_EXIT_TYPE_2, to_var=PRIMARY_TEMP_7000),
	Mem7000AndConst(0x0070),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 32, ["EVENT_3350_copy_var_to_var_14"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 48, ["EVENT_3350_copy_var_to_var_18"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 64, ["EVENT_3350_copy_var_to_var_22"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 80, ["EVENT_3350_copy_var_to_var_26"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 96, ["EVENT_3350_copy_var_to_var_30"]),
	CopyVarToVar(from_var=UNKNOWN_70E7, to_var=PRIMARY_TEMP_7000),
	Mem7000OrConst(0x0080),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_70E7),
	Jmp(["EVENT_3350_copy_var_to_var_33"]),
	CopyVarToVar(from_var=UNKNOWN_70E7, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3350_copy_var_to_var_14"),
	Mem7000OrConst(0x0008),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_70E7),
	Jmp(["EVENT_3350_copy_var_to_var_33"]),
	CopyVarToVar(from_var=UNKNOWN_70E8, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3350_copy_var_to_var_18"),
	Mem7000OrConst(0x0080),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_70E8),
	Jmp(["EVENT_3350_copy_var_to_var_33"]),
	CopyVarToVar(from_var=UNKNOWN_70E8, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3350_copy_var_to_var_22"),
	Mem7000OrConst(0x0008),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_70E8),
	Jmp(["EVENT_3350_copy_var_to_var_33"]),
	CopyVarToVar(from_var=UNKNOWN_70E9, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3350_copy_var_to_var_26"),
	Mem7000OrConst(0x0080),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_70E9),
	Jmp(["EVENT_3350_copy_var_to_var_33"]),
	CopyVarToVar(from_var=UNKNOWN_70E9, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3350_copy_var_to_var_30"),
	Mem7000OrConst(0x0008),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_70E9),
	CopyVarToVar(from_var=KEEP_DOORS_EXIT_TYPE_2, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3350_copy_var_to_var_33"),
	Mem7000AndConst(0x0007),
	AddConstToVar(PRIMARY_TEMP_7000, 512),
	Dec(PRIMARY_TEMP_7000),
	JmpIfMem704XAt7000BitClear(["EVENT_3350_inc_40"]),
	DisableObjectTriggerInSpecificLevel(NPC_0, R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM),
	DisableObjectTriggerInSpecificLevel(NPC_0, R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS),
	Inc(KEEP_DOORS_EXIT_TYPE_1, identifier="EVENT_3350_inc_40"),
	JmpIfVarEqualsConst(KEEP_DOORS_EXIT_TYPE_1, 4, ["EVENT_3350_enter_area_44"],  identifier="check_doors_complete"),
	EnterArea(room_id=R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM, face_direction=NORTHEAST, x=4, y=79, z=0, run_entrance_event=True),
	Return(),
	EnterArea(room_id=R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS, face_direction=NORTHEAST, x=16, y=79, z=0, run_entrance_event=True, identifier="EVENT_3350_enter_area_44"),
	Return()
])
