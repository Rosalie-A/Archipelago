# E3185_PA_MOLE_IN_DEEP_MINES
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
	SetVarToConst(ITEM_ID, BambinoBombItem),
	StoreItemAt70A7QuantityTo7000(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3185_set_var_to_const_5"]),
	RunDialog(dialog_id=DI1632_PA_MOLE_NEEDS_BOMB, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	SetVarToConst(TEMP_70AE, 20, identifier="EVENT_3185_set_var_to_const_5"),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(1),
	Store02To0248(),
	SetBit(BAMBINO_BOMB_UNKNOWN),
	Pause(2),
	ApplyTileModToLevel(use_alternate=True, room_id=R272_MOLEVILLE_MINES_AREA_11_BOMBED_ROOM_WSINGING_MOLES, mod_id=32),
	ApplySolidityModToLevel(permanent=True, room_id=R272_MOLEVILLE_MINES_AREA_11_BOMBED_ROOM_WSINGING_MOLES, mod_id=0),
	Pause(2),
	ClearBit(BAMBINO_BOMB_UNKNOWN),
	Store00To0248(),
	Pause(1),
	JmpIfBitClear(TEMP_7043_5, ["EVENT_3185_action_queue_18"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetAllSpeeds(FAST),
		A_Walk1StepSoutheast(),
		A_WalkNortheastSteps(2),
		A_Walk1StepNorthwest(),
		A_FaceSouthwest(),
		A_SetAllSpeeds(NORMAL)
	], identifier="EVENT_3185_action_queue_18"),
	SetVarToConst(TEMP_70AE, 20),
	SetSyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	SetSyncActionScript(MARIO, A0670_NOD_YES),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_Pause(16),
		A_FaceSouthwest(),
		A_SetAllSpeeds(VERY_FAST),
		A_SequenceLoopingOn(),
		A_JumpToHeight(72),
		A_Pause(20),
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
		A_WalkToXYCoords(x=6, y=24),
		A_WalkToXYCoords(x=4, y=20),
		A_WalkSouthwestSteps(2),
		A_UnknownCommand(bytearray(b'\xfd\xf2')),
		A_VisibilityOff()
	]),
	SetBit(MINES_BACK_OPENED),
	RemoveOneOfItemFromInventory(BambinoBombItem),
	Return()
])
