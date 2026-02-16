# E1805_TEMPLE_3_FORTUNE_SHAMAN
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
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AE),
	JmpIfMarioOnAnObjectOrNot(['EVENT_1805_set_var_to_const_42', 'EVENT_1805_set_var_to_const_42']),
	StoreCoinCountTo7000(),
	CompareVarToConst(PRIMARY_TEMP_7000, 50),
	JmpIfComparisonResultIsLesser(["EVENT_1805_run_dialog_40"]),
	RunDialog(dialog_id=DI1240_FORTUNE_SHAMAN_PROMPT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_1805_pause_45"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SequenceLoopingOn(),
		A_Pause(30),
		A_SetSequenceSpeed(VERY_SLOW)
	]),
	SetVarToConst(PRIMARY_TEMP_7000, 50),
	Dec7000FromCoins(),
	PlaySound(sound=SO055_LOSE_COINS_COIN_FOUNTAIN, channel=6),
	RunDialog(dialog_id=DI1241_FORTUNE_SHAMAN_INSTRUCTIONS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetVarToConst(TEMP_70AA, 23),
	JmpToSubroutine(["EVENT_1794_action_queue_69"]),
	SetBit(BELOME_FORTUNE_1),
	ClearBit(UNKNOWN_BELOME_FORTUNE),
	Inc(UNKNOWN_70AD),
	JmpIfBitClear(HAS_A_PRIZE_FORTUNE, ["EVENT_1805_ret_39"]),
	Pause(16),
	SetVarToConst(TEMP_70AB, 24),
	RunEventAsSubroutine(E1739_REFOCUS_CAMERA),
	PlaySound(sound=SO084_SMOKED, channel=6),
	ActionQueueSync(target=NPC_0, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=10, y=26, z=20, direction=EAST)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_VisibilityOff(),
		A_TransferToXYZF(x=10, y=26, z=23, direction=EAST)
	]),
	SetVarToConst(TEMP_7034, 1),
	Set70107015ToObjectXYZ(target=NPC_0),
	StartLoopNTimes(14),
	Pause(1, identifier="EVENT_1805_pause_30"),
	CreatePacketAt7010(packet=P032_BLUE_CLOUD, destinations=["EVENT_1805_pause_30"]),
	Pause(4),
	AddConstToVar(TEMP_7034, 3),
	AddConstToVar(Z_COORD_1, 80),
	EndLoop(),
	SetVarToConst(TEMP_70AB, 0),
	RunEventAsSubroutine(E1739_REFOCUS_CAMERA),
	RemoveObjectFromSpecificLevel(NPC_3, R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM),
	Return(identifier="EVENT_1805_ret_39"),
	RunDialog(dialog_id=DI1239_FORTUNE_SHAMAN_NOT_ENOUGH_COINS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1805_run_dialog_40"),
	Return(),
	SetVarToConst(TEMP_70AA, 23, identifier="EVENT_1805_set_var_to_const_42"),
	JmpToSubroutine(["EVENT_1794_action_queue_69"]),
	Return(),
	Pause(10, identifier="EVENT_1805_pause_45"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Return()
])
