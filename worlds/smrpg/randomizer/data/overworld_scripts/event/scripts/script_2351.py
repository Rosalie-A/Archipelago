# E2351_TOWER_START_BULLET_BILLS_ANIMATION
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
	Pause(1, identifier="EVENT_2351_pause_0"),
	JmpIfBitClear(TEMP_7043_3, ["EVENT_2351_pause_0"]),
	ClearBit(TEMP_7043_3),
	JmpIfObjectInCurrentLevel(NPC_8, ["EVENT_2351_ret_40"]),
	JmpIfObjectInCurrentLevel(NPC_0, ["EVENT_2351_reset_coords_6"]),
	Jmp(["EVENT_2351_jmp_if_present_in_current_level_13"]),
	ResetCoords(NPC_0, identifier="EVENT_2351_reset_coords_6"),
	SetSyncActionScript(NPC_0, A0389_TOWER_BULLET_BILL_APPEARS),
	Pause(16),
	SummonObjectToCurrentLevel(NPC_7),
	Pause(8),
	RemoveObjectFromCurrentLevel(NPC_7),
	Jmp(["EVENT_2351_pause_0"]),
	JmpIfObjectInCurrentLevel(NPC_1, ["EVENT_2351_reset_coords_15"], identifier="EVENT_2351_jmp_if_present_in_current_level_13"),
	Jmp(["EVENT_2351_jmp_if_present_in_current_level_22"]),
	ResetCoords(NPC_1, identifier="EVENT_2351_reset_coords_15"),
	SetSyncActionScript(NPC_1, A0389_TOWER_BULLET_BILL_APPEARS),
	Pause(16),
	SummonObjectToCurrentLevel(NPC_7),
	Pause(8),
	RemoveObjectFromCurrentLevel(NPC_7),
	Jmp(["EVENT_2351_pause_0"]),
	JmpIfObjectInCurrentLevel(NPC_2, ["EVENT_2351_reset_coords_24"], identifier="EVENT_2351_jmp_if_present_in_current_level_22"),
	Jmp(["EVENT_2351_jmp_if_present_in_current_level_31"]),
	ResetCoords(NPC_2, identifier="EVENT_2351_reset_coords_24"),
	SetSyncActionScript(NPC_2, A0389_TOWER_BULLET_BILL_APPEARS),
	Pause(16),
	SummonObjectToCurrentLevel(NPC_7),
	Pause(8),
	RemoveObjectFromCurrentLevel(NPC_7),
	Jmp(["EVENT_2351_pause_0"]),
	JmpIfObjectInCurrentLevel(NPC_3, ["EVENT_2351_reset_coords_33"], identifier="EVENT_2351_jmp_if_present_in_current_level_31"),
	Jmp(["EVENT_2351_jmp_39"]),
	ResetCoords(NPC_3, identifier="EVENT_2351_reset_coords_33"),
	SetSyncActionScript(NPC_3, A0389_TOWER_BULLET_BILL_APPEARS),
	Pause(16),
	SummonObjectToCurrentLevel(NPC_7),
	Pause(8),
	RemoveObjectFromCurrentLevel(NPC_7),
	Jmp(["EVENT_2351_pause_0"], identifier="EVENT_2351_jmp_39"),
	Return(identifier="EVENT_2351_ret_40")
])
