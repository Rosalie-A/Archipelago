# E1645_BUCKET_GIRL
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
	StoreItemAmountTo7000(CarboCookieItem),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1645_run_dialog_7"]),
	RunDialog(dialog_id=DI1146_WISH_I_HAD_CARBO_COOKIE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI1147_CARBO_COOKIE_PROMPT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1645_run_dialog_7"),
	JmpIfDialogOptionBSelected(["EVENT_1645_pause_33"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	RemoveOneOfItemFromInventory(CarboCookieItem),
	RunDialog(dialog_id=DI1149_BUCKET_GIRL_LEAVES, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(CARBO_COOKIE_GIVEN),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_PlaySound(sound=SO004_JUMP, channel=4),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_JumpToHeight(80),
		A_SetAllSpeeds(NORMAL),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_WalkSouthSteps(2),
		A_FixedFCoordOff(),
		A_FaceMario(),
		A_Pause(1)
	]),
	RunDialog(dialog_id=DI1232_DONT_TAKE_MY_BUCKET, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_SetAllSpeeds(FAST),
		A_WalkSoutheastSteps(9),
		A_VisibilityOff()
	], identifier="EVENT_1645_action_queue_20"),
	RemoveObjectFromCurrentLevel(MEM_70A8, identifier="EVENT_1645_remove_from_current_level_24"),
	RemoveObjectFromSpecificLevel(MEM_70A8, R108_MOLEVILLE_OUTSIDE),
    RemoveOneOfItemFromInventory(CarboCookieItem),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
    Return(),
    
	Pause(10, identifier="EVENT_1645_pause_33"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	RunDialog(dialog_id=DI1148_CARBO_COOKIE_DECLINE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
])
