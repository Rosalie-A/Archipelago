# E0395_WALLET_TOAD_2
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
    


	JmpIfBitSet(REFUSED_TO_RETURN_WALLET, ["EVENT_395_run_event_as_subroutine_25"]),
	JmpIfBitSet(RETURNED_WALLET, ["attempt_second_wallet_prize"]),
	StoreItemAmountTo7000(WalletItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["first_time_meeting_wallet_guy"]),
	RunEventAsSubroutine(E3587_SET_70AE_TO_70A8),
	RunDialog(dialog_id=DI0669_ASKS_FOR_WALLET_BACK, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_395_set_action_script_19"], identifier="EVENT_395_jmp_if_dialog_option_b_7"),
	Pause(10),
	RunEventAsSubroutine(E3587_SET_70AE_TO_70A8),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	RunDialog(dialog_id=DI0671_THANKS_FOR_RETURNING_WALLET, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	RunEventAsSubroutine(E0179_NPC_QUEST_2_CONTAINER),
	RemoveOneOfItemFromInventory(WalletItem),
	SetBit(RETURNED_WALLET),
	ClearBit(REFUSED_TO_RETURN_WALLET),
    Return(),
    
	JmpIfBitSet(SECOND_WALLET_PRIZE_RECEIVED, ["EVENT_395_run_dialog_30"], identifier="attempt_second_wallet_prize"),
	JmpIfBitClear(MARRYMORE_LIBERATED, ["EVENT_395_run_dialog_30"]),
    
	RunEventAsSubroutine(E0180_NPC_QUEST_3_CONTAINER),
    SetBit(SECOND_WALLET_PRIZE_RECEIVED),
	Return(),


	SetSyncActionScript(MEM_70A8, A0978_RANDOMLY_FACE_SOUTHWEST),
	Return(),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO, identifier="EVENT_395_set_action_script_19"),
	RememberLastObject(),
	Pause(10),
	RunDialog(dialog_id=DI0670_YOURE_TERRIBLE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(REFUSED_TO_RETURN_WALLET),
	Return(),
	RunEventAsSubroutine(E3587_SET_70AE_TO_70A8, identifier="EVENT_395_run_event_as_subroutine_25"),
	RunDialog(dialog_id=DI0672_DEMANDS_WALLET_BACK_AGAIN, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_395_jmp_if_dialog_option_b_7"]),
	RunDialog(dialog_id=DI0668_THAT_WAS_TOO_DARN_CLOSE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_395_run_dialog_30"),
	Return(),
    


	# first time meeting wallet guy
	RunDialog(dialog_id=DI0578_WALLET_GUY_INTRO, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True, identifier="first_time_meeting_wallet_guy"),
	RunDialog(dialog_id=DI0579_WALLET_GUY_PROMISE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	StartAsyncEmbeddedActionScript(target=MEM_70A8, prefix=0xF1, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetSolidityBits(cant_walk_through=True)
	]),
	SetSyncActionScript(MEM_70A8, A0021_STAND_STILL_AND_MOVE_RANDOM_DIRECTIONS),
	Return(),
])
