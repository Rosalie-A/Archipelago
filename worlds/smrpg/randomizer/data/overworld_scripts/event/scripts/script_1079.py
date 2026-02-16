# E1079_MELODY_BAY_SONG_1_VALIDATOR
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
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1074_jmp_if_var_equals_const_123"]),
	JmpIfVarNotEqualsConst(SECONDARY_TEMP_7024, 1, ["EVENT_1079_set_action_script_6"]),
	SetSyncActionScript(NPC_0, A0571_MELODY_BAY_TADPOLE_AFFIRMATIVE),
	SetBit(TEMP_7043_0),
	Jmp(["EVENT_1079_pause_8"]),
	SetSyncActionScript(NPC_0, A0572_MELODY_BAY_TADPOLE_INCORRECT, identifier="EVENT_1079_set_action_script_6"),
	ClearBit(TEMP_7043_0),
	Pause(35, identifier="EVENT_1079_pause_8"),
	CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1074_jmp_if_var_equals_const_123"]),
	JmpIfVarNotEqualsConst(TEMP_7026, 2, ["EVENT_1079_set_action_script_15"]),
	SetSyncActionScript(NPC_1, A0571_MELODY_BAY_TADPOLE_AFFIRMATIVE),
	SetBit(TEMP_7043_1),
	Jmp(["EVENT_1079_pause_17"]),
	SetSyncActionScript(NPC_1, A0572_MELODY_BAY_TADPOLE_INCORRECT, identifier="EVENT_1079_set_action_script_15"),
	ClearBit(TEMP_7043_1),
	Pause(35, identifier="EVENT_1079_pause_17"),
	CopyVarToVar(from_var=TEMP_7028, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1074_jmp_if_var_equals_const_123"]),
	JmpIfVarNotEqualsConst(TEMP_7028, 6, ["EVENT_1079_set_action_script_24"]),
	SetSyncActionScript(NPC_2, A0571_MELODY_BAY_TADPOLE_AFFIRMATIVE),
	SetBit(TEMP_7043_2),
	Jmp(["EVENT_1079_pause_26"]),
	SetSyncActionScript(NPC_2, A0572_MELODY_BAY_TADPOLE_INCORRECT, identifier="EVENT_1079_set_action_script_24"),
	ClearBit(TEMP_7043_2),
	Pause(35, identifier="EVENT_1079_pause_26"),
	CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1074_jmp_if_var_equals_const_123"]),
	JmpIfVarNotEqualsConst(TEMP_702A, 5, ["EVENT_1079_set_action_script_33"]),
	SetSyncActionScript(NPC_3, A0571_MELODY_BAY_TADPOLE_AFFIRMATIVE),
	SetBit(TEMP_7043_3),
	Jmp(["EVENT_1079_pause_35"]),
	SetSyncActionScript(NPC_3, A0572_MELODY_BAY_TADPOLE_INCORRECT, identifier="EVENT_1079_set_action_script_33"),
	ClearBit(TEMP_7043_3),
	Pause(35, identifier="EVENT_1079_pause_35"),
	CopyVarToVar(from_var=TEMP_702C, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1074_jmp_if_var_equals_const_123"]),
	JmpIfVarNotEqualsConst(TEMP_702C, 4, ["EVENT_1079_set_action_script_42"]),
	SetSyncActionScript(NPC_4, A0571_MELODY_BAY_TADPOLE_AFFIRMATIVE),
	SetBit(TEMP_7043_4),
	Jmp(["EVENT_1079_pause_44"]),
	SetSyncActionScript(NPC_4, A0572_MELODY_BAY_TADPOLE_INCORRECT, identifier="EVENT_1079_set_action_script_42"),
	ClearBit(TEMP_7043_4),
	Pause(35, identifier="EVENT_1079_pause_44"),
	CopyVarToVar(from_var=TEMP_702E, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1074_jmp_if_var_equals_const_123"]),
	JmpIfVarNotEqualsConst(TEMP_702E, 5, ["EVENT_1079_set_action_script_51"]),
	SetSyncActionScript(NPC_5, A0571_MELODY_BAY_TADPOLE_AFFIRMATIVE),
	SetBit(TEMP_7043_5),
	Jmp(["EVENT_1079_pause_53"]),
	SetSyncActionScript(NPC_5, A0572_MELODY_BAY_TADPOLE_INCORRECT, identifier="EVENT_1079_set_action_script_51"),
	ClearBit(TEMP_7043_5),
	Pause(35, identifier="EVENT_1079_pause_53"),
	CopyVarToVar(from_var=TEMP_7030, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1074_jmp_if_var_equals_const_123"]),
	JmpIfVarNotEqualsConst(TEMP_7030, 4, ["EVENT_1079_set_action_script_60"]),
	SetSyncActionScript(NPC_6, A0571_MELODY_BAY_TADPOLE_AFFIRMATIVE),
	SetBit(TEMP_7043_6),
	Jmp(["EVENT_1079_pause_62"]),
	SetSyncActionScript(NPC_6, A0572_MELODY_BAY_TADPOLE_INCORRECT, identifier="EVENT_1079_set_action_script_60"),
	ClearBit(TEMP_7043_6),
	Pause(35, identifier="EVENT_1079_pause_62"),
	CopyVarToVar(from_var=TEMP_7032, to_var=PRIMARY_TEMP_7000),
	JmpToSubroutine(["EVENT_1074_jmp_if_var_equals_const_123"]),
	JmpIfVarNotEqualsConst(TEMP_7032, 5, ["EVENT_1079_set_action_script_69"]),
	SetSyncActionScript(NPC_7, A0571_MELODY_BAY_TADPOLE_AFFIRMATIVE),
	SetBit(TEMP_7043_7),
	Jmp(["EVENT_1079_pause_71"]),
	SetSyncActionScript(NPC_7, A0572_MELODY_BAY_TADPOLE_INCORRECT, identifier="EVENT_1079_set_action_script_69"),
	ClearBit(TEMP_7043_7),
	Pause(35, identifier="EVENT_1079_pause_71"),
	Pause(45),
	PlayMusicAtCurrentVolume(M0017_TADPOLEPOND),
	SetVarToConst(PRIMARY_TEMP_7000, 0),
	JmpIfVarNotEqualsConst(SECONDARY_TEMP_7024, 1, ["EVENT_1079_jmp_if_var_not_equals_const_77"]),
	Inc(PRIMARY_TEMP_7000),
	JmpIfVarNotEqualsConst(TEMP_7026, 2, ["EVENT_1079_jmp_if_var_not_equals_const_79"], identifier="EVENT_1079_jmp_if_var_not_equals_const_77"),
	Inc(PRIMARY_TEMP_7000),
	JmpIfVarNotEqualsConst(TEMP_7028, 6, ["EVENT_1079_jmp_if_var_not_equals_const_81"], identifier="EVENT_1079_jmp_if_var_not_equals_const_79"),
	Inc(PRIMARY_TEMP_7000),
	JmpIfVarNotEqualsConst(TEMP_702A, 5, ["EVENT_1079_jmp_if_var_not_equals_const_83"], identifier="EVENT_1079_jmp_if_var_not_equals_const_81"),
	Inc(PRIMARY_TEMP_7000),
	JmpIfVarNotEqualsConst(TEMP_702C, 4, ["EVENT_1079_jmp_if_var_not_equals_const_85"], identifier="EVENT_1079_jmp_if_var_not_equals_const_83"),
	Inc(PRIMARY_TEMP_7000),
	JmpIfVarNotEqualsConst(TEMP_702E, 5, ["EVENT_1079_jmp_if_var_not_equals_const_87"], identifier="EVENT_1079_jmp_if_var_not_equals_const_85"),
	Inc(PRIMARY_TEMP_7000),
	JmpIfVarNotEqualsConst(TEMP_7030, 4, ["EVENT_1079_jmp_if_var_not_equals_const_89"], identifier="EVENT_1079_jmp_if_var_not_equals_const_87"),
	Inc(PRIMARY_TEMP_7000),
	JmpIfVarNotEqualsConst(TEMP_7032, 5, ["EVENT_1079_jmp_if_var_equals_const_91"], identifier="EVENT_1079_jmp_if_var_not_equals_const_89"),
	Inc(PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1074_pause_59"], identifier="EVENT_1079_jmp_if_var_equals_const_91"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_1074_pause_64"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_1074_pause_64"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_1074_pause_71"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_1074_pause_71"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_1074_pause_78"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_1074_pause_78"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_1074_pause_85"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_1074_pause_92"])
])
