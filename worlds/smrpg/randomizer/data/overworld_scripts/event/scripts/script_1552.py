# E1552_FOREST_TREE_TRUNK_AREA_LOADER
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
	JmpIfBitClear(DIRECTIONAL_7047_0, ["EVENT_1552_fade_in_from_black_sync_10"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_VisibilityOff()
	]),
	FreezeAllNPCsUntilReturn(),
	FadeInFromBlack(sync=False),
	FreezeCamera(),
	SetAsyncActionScript(MARIO, A0482_FOREST_PLAYER_FALLS_TO_UNDERGROUND),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	UnfreezeCamera(),
	UnfreezeAllNPCs(),
	Jmp(["EVENT_1552_set_var_to_const_11"]),
	FadeInFromBlack(sync=True, identifier="EVENT_1552_fade_in_from_black_sync_10"),
	SetVarToConst(TEMP_70A9, 20, identifier="EVENT_1552_set_var_to_const_11"),
	StartLoopNTimes(7),
	ActionQueueSync(target=MEM_70A9, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_walk_through=True)
	]),
	Inc(TEMP_70A9),
	EndLoop(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ObjectMemorySetBit(arg_1=0x0B, bits=[3])
	]),
	SetVarToConst(TEMP_70AB, 28),
	RunBackgroundEvent(event_id=E1553_FOREST_TREE_TRUNK_AREA_LOADER_CONTD, return_on_level_exit=True),
	Return()
])
