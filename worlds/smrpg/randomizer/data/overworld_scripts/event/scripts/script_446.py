# E0446_GOOMBA_THUMPIN_SCOREKEEPING
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
	Dec(TEMP_7026),
	JmpIfVarEqualsConst(TEMP_7026, 10, ["EVENT_446_copy_var_to_var_23"]),
	JmpIfVarEqualsConst(TEMP_7026, 0, ["EVENT_446_run_dialog_6"], identifier="EVENT_446_jmp_if_var_equals_const_2"),
	CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000),
	RunDialog(dialog_id=DI0835_DUPLICATE, above_object=MARIO, closable=False, sync=True, multiline=True, use_background=False),
	Jmp(["EVENT_446_set_var_to_const_20"]),
	RunDialog(dialog_id=DI0866_X_POINTS, above_object=MARIO, closable=False, sync=True, multiline=True, use_background=False, identifier="EVENT_446_run_dialog_6"),
	StopAllBackgroundEvents(),
	UnknownCommand(bytearray(b'\xfdD')),
	UnfreezeCamera(),
	FadeOutMusicToVolume(duration=2, volume=0),
	ClearBit(TEMP_7044_6),
	SetBit(TEMP_7044_5),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	SetBit(UNKNOWN_7083_7),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Pause(1, identifier="EVENT_446_pause_16"),
	JmpIfMarioInAir(["EVENT_446_pause_16"]),
	PlayMusicAtDefaultVolume(M0007_PIPEVAULT),
	Return(),
	SetVarToConst(TIMER_701C, 80, identifier="EVENT_446_set_var_to_const_20"),
	RunBackgroundEventWithPauseReturnOnExit(event_id=E0446_GOOMBA_THUMPIN_SCOREKEEPING, timer_var=TIMER_701C, bit_4=True, bit_5=True),
	Return(),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000, identifier="EVENT_446_copy_var_to_var_23"),
	CompareVarToConst(PRIMARY_TEMP_7000, 20),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_446_set_bit_27"]),
	Jmp(["EVENT_446_jmp_if_var_equals_const_2"]),
	SetBit(TEMP_7049_6, identifier="EVENT_446_set_bit_27"),
	Jmp(["EVENT_446_jmp_if_var_equals_const_2"])
])
