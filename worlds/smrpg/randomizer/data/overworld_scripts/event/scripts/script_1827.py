# E1827_KEEP_LINEAR_PLATFORM_ROOM_LOADER
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
	ClearBit(UNKNOWN_704D_1),
	JmpIfBitSet(TEMP_7044_6, ["EVENT_1827_set_var_to_const_3"]),
	ClearBit(TEMP_7095_4),
	SetVarToConst(ROSE_WAY_7038, 3712, identifier="EVENT_1827_set_var_to_const_3"),
	SetVarToConst(ROSE_WAY_703A, 14976),
	SetVarToConst(ROSE_WAY_703C, 512),
	SetVarToConst(TEMP_70A9, 21),
	StartLoopNTimes(8),
	ActionQueueSync(target=MEM_70A9, subscript=[
		A_ShiftZUpPixels(4),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	Inc(TEMP_70A9),
	EndLoop(),
	StartLoopNTimes(3),
	ActionQueueSync(target=MEM_70A9, subscript=[
		A_ShiftZUpPixels(4)
	]),
	Inc(TEMP_70A9),
	EndLoop(),
	SetVarToConst(TEMP_70A9, 21),
	StartLoopNTimes(8),
	SetSyncActionScript(MEM_70A9, A0829_KEEP_XY_PLATFORMS),
	Inc(TEMP_70A9),
	EndLoop(),
	RemoveObjectFromCurrentLevel(NPC_9),
	RunBackgroundEvent(event_id=E1828_KEEP_MARIO_FALLS_IN_LAVA, return_on_level_exit=True),
	RunBackgroundEvent(event_id=E1833_KEEP_LINEAR_PLATFORM_ROOM_BACKGROUND, return_on_level_exit=True, bit_6=True),
	JmpToEvent(E1829_KEEP_DISPLAY_REMAINING_TRIES)
])
