# E3123_SEWER_DRAIN_WATER
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
	DisableObjectTrigger(MEM_70A8),
	SetBit(SEWER_WATER_LEVEL),
	SetSyncActionScript(MEM_70A8, A0056_SEWER_WATER_DRAIN),
	PlaySound(sound=SO009_GREEN_SWITCH, channel=6),
	ActionQueueSync(target=MARIO, subscript=[
		A_JumpToHeight(height=0, silent=True),
		A_ClearSolidityBits(cant_pass_npcs=True),
		A_ShiftZDownPixels(2),
		A_ResetProperties(),
		A_SetSolidityBits(cant_pass_npcs=True)
	]),
	PlaySound(sound=SO008_WATERFALL, channel=4),
	RunDialog(dialog_id=DI1585_WATER_DRAINED, above_object=MARIO, closable=False, sync=True, multiline=False, use_background=False, bit_6=True),
	ApplySolidityModToLevel(permanent=True, room_id=R056_KERO_SEWERS_AREA_02_LONG_ROOM_WTHREE_PIPES, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R056_KERO_SEWERS_AREA_02_LONG_ROOM_WTHREE_PIPES, mod_id=1),
	ApplySolidityModToLevel(permanent=True, room_id=R057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER, mod_id=1),
	ApplySolidityModToLevel(permanent=True, room_id=R058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE, mod_id=1),
	Return()
])
