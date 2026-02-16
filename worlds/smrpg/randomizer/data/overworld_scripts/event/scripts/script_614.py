# E0614_MARRYMORE_SUITE_TIP_BELLHOP
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
	RunDialog(dialog_id=DI0986_TIP_PROMPT, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_614_pause_14"]),
	Pause(10),
	SetVarToConst(SECONDARY_TEMP_7024, 10),
	RunEventAsSubroutine(E0274_CHECK_IF_HAVE_ENOUGH_COINS),
	JmpIfBitSet(INSUFFICIENT_COINS, ["EVENT_614_run_dialog_13"]),
	PlaySound(sound=SO013_COIN, channel=6),
	SetVarToConst(PRIMARY_TEMP_7000, 10),
	Dec7000FromCoins(),
	RunDialog(dialog_id=DI0988_THANKS_FOR_TIP, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfBitSet(BELLHOP_CALLED, ["EVENT_614_pause_16"]),
	SetBit(TEMP_7042_7),
	Jmp(["EVENT_614_pause_16"]),
	RunDialog(dialog_id=DI0987_CANT_AFFORD_TIP, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False, identifier="EVENT_614_run_dialog_13"),
	Pause(10, identifier="EVENT_614_pause_14"),
	RunDialog(dialog_id=DI0973_DUPLICATE, above_object=NPC_0, closable=True, sync=False, multiline=True, use_background=True),
	Pause(10, identifier="EVENT_614_pause_16"),
	JmpIfBitSet(BELLHOP_CALLED, ["EVENT_614_action_queue_28"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(FAST),
		A_Walk1StepSoutheast(),
		A_WalkSouthwestSteps(2),
		A_VisibilityOff(),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	ClearBit(TEMP_7042_1),
	ClearBit(TEMP_7042_2),
	ClearBit(TEMP_7042_3),
	SetBit(TEMP_7042_4),
	ClearBit(BELLHOP_UNKNOWN),
	ClearBit(BELLHOP_CALLED),
	Return(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_Walk1StepNorthwest(),
		A_WalkSouthwestSteps(3),
		A_VisibilityOff()
	], identifier="EVENT_614_action_queue_28"),
	ClearBit(TEMP_7042_1),
	ClearBit(TEMP_7042_2),
	ClearBit(TEMP_7042_3),
	ClearBit(BELLHOP_CALLED),
	ClearBit(BELLHOP_UNKNOWN),
	Return()
])
