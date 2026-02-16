# E0351_GAMEBOY_KID
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
	JmpIfBitSet(MUSHROOM_KINGDOM_LIBERATED, ["EVENT_351_jmp_if_bit_set_7"]),
	JmpIfBitSet(BEETLEMANIA_UNLOCKED, ["EVENT_351_run_dialog_23"], identifier="EVENT_351_jmp_if_bit_set_1"),
	JmpIfRandom1of2(["EVENT_351_run_dialog_5"]),
	RunDialog(dialog_id=DI3733_GAMEBOY_KID, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI3732_GAMEBOY_KID, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_351_run_dialog_5"),
	Return(),
	JmpIfBitSet(GAMEBOY_KID_PURCHASE_COMPLETE, ["EVENT_351_jmp_if_bit_set_1"], identifier="EVENT_351_jmp_if_bit_set_7"),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_UnknownCommand(bytearray(b'\xfd$\x17\x00')),
		A_Mem700CAndConst(0x00C0),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 64, ["EVENT_351_run_event_as_subroutine_9"]),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_TransferXYZFPixels(x=4, y=0, z=0, direction=EAST),
		A_Jmp(["EVENT_351_run_event_as_subroutine_9"])
	]),
	RunEventAsSubroutine(E3587_SET_70AE_TO_70A8, identifier="EVENT_351_run_event_as_subroutine_9"),
	RunDialog(dialog_id=DI3738_GAMEBOY_KID_SELL_PROMPT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_351_pause_32"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	SetVarToConst(SECONDARY_TEMP_7024, 500),
	RunEventAsSubroutine(E0274_CHECK_IF_HAVE_ENOUGH_COINS),
	JmpIfBitSet(INSUFFICIENT_COINS, ["EVENT_351_run_dialog_35"]),
	PlaySound(sound=SO013_COIN, channel=6),
	SetVarToConst(PRIMARY_TEMP_7000, 500),
	Dec7000FromCoins(),
	SetBit(GAMEBOY_KID_PURCHASE_COMPLETE),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	Jmp(["EVENT_351_action_queue_37"]),
	RunDialog(dialog_id=DI3742_GAMEBOY_KID_TUTORIAL_PROMPT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_351_run_dialog_23"),
	JmpIfDialogOptionBSelected(["EVENT_351_pause_29"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	RunDialog(dialog_id=DI3744_BEETLEMANIA_TUTORIAL, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_351_action_queue_37"]),
	Pause(10, identifier="EVENT_351_pause_29"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Jmp(["EVENT_351_action_queue_37"]),
	Pause(10, identifier="EVENT_351_pause_32"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Jmp(["EVENT_351_action_queue_37"]),
	RunDialog(dialog_id=DI3741_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_351_run_dialog_35"),
	Jmp(["EVENT_351_action_queue_37"]),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_TransferToXYZF(x=9, y=91, z=0, direction=EAST),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	], identifier="EVENT_351_action_queue_37"),
	Return()
])
