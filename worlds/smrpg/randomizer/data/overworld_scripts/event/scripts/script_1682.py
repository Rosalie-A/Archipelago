# E1682_TRAMPOLINE_SHAMAN
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
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000, identifier="EVENT_1682_copy_var_to_var_0"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AE),
	StoreCoinCountTo7000(),
	CompareVarToConst(PRIMARY_TEMP_7000, 100),
	JmpIfComparisonResultIsLesser(["EVENT_1682_action_queue_19"]),
	RunDialog(dialog_id=DI1228_SHAMAN_TRAMPOLINE_SALE, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_1682_pause_22"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SequenceLoopingOn(),
		A_Pause(30),
		A_SetSequenceSpeed(VERY_SLOW)
	]),
	SetVarToConst(PRIMARY_TEMP_7000, 100),
	Dec7000FromCoins(),
	PlaySound(sound=SO055_LOSE_COINS_COIN_FOUNTAIN, channel=6),
	Pause(50),
	SetVarToConst(TEMP_70AA, 20),
	JmpToSubroutine(["EVENT_1794_action_queue_69"]),
	RemoveObjectFromSpecificLevel(NPC_0, R428_BELOME_TEMPLE_AREA_01_WWARP_TRAMPOLINE),
	SetBit(TRAMPOLINE_SHAMAN_PAID),
	Return(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceMario()
	], identifier="EVENT_1682_action_queue_19"),
	RunDialog(dialog_id=DI1229_SHAMAN_TRAMPOLINE_SALE_NOT_ENOUGH_MONEY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Return(),
	Pause(10, identifier="EVENT_1682_pause_22"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Return()
])
