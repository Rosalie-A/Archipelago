# E3657_ROOM_SERVICE_MENU
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
	JmpIfDialogOptionBOrCSelected(['room_service_price_2_a', 'EVENT_3657_close_dialog_11']),
	SetVarToConst(SECONDARY_TEMP_7024, 10, identifier="room_service_price_1_a"),
	RunEventAsSubroutine(E0274_CHECK_IF_HAVE_ENOUGH_COINS),
	JmpIfBitSet(INSUFFICIENT_COINS, ["EVENT_3657_run_dialog_23"]),
	SetVarToConst(ITEM_ID, PickMeUpItem, identifier="room_service_item_id_1"),
	SetVarToConst(PRIMARY_TEMP_7000, 10, identifier="room_service_price_1_b"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703A),
	SetVarToConst(PRIMARY_TEMP_7000, 3852, identifier="EVENT_3657_set_var_to_const_7"),
	RunEventAsSubroutine(E3827_GRANT_ITEM_STANDARD_SOUND),
	CopyVarToVar(from_var=ROSE_WAY_703A, to_var=PRIMARY_TEMP_7000),
	Dec7000FromCoins(),
	CloseDialog(identifier="EVENT_3657_close_dialog_11"),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4])
	]),
	SetSyncActionScript(NPC_0, A0978_RANDOMLY_FACE_SOUTHWEST),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return(),
	SetVarToConst(SECONDARY_TEMP_7024, 150, identifier="room_service_price_2_a"),
	RunEventAsSubroutine(E0274_CHECK_IF_HAVE_ENOUGH_COINS),
	JmpIfBitSet(INSUFFICIENT_COINS, ["EVENT_3657_run_dialog_23"]),
	SetVarToConst(ITEM_ID, KerokeroColaItem, identifier="room_service_item_id_2"),
	SetVarToConst(PRIMARY_TEMP_7000, 150, identifier="room_service_price_2_b"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703A),
	Jmp(["EVENT_3657_set_var_to_const_7"]),
	RunDialog(dialog_id=DI3853_ROOM_SERVICE_INSUFFICIENT_COINS, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_3657_run_dialog_23"),
	Jmp(["EVENT_3657_close_dialog_11"])
])
