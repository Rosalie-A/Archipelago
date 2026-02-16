# E0557_ROSE_TOWN_LIBERATED_LOADER_BACKGROUND
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
	Pause(60, identifier="EVENT_557_pause_0"),
	ApplyTileModToLevel(use_alternate=True, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=3),
	ApplySolidityModToLevel(permanent=True, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=1),
	SetSyncActionScript(NPC_5, A0662_ROSE_TOWN_LIBERATED_WATER_GUY),
	SetBit(ROSE_TOWN_WATER_PUMPERS_POSITION),
	Pause(1, identifier="EVENT_557_pause_5"),
	JmpIfBitSet(TEMP_7043_7, ["EVENT_557_set_action_script_8"]),
	Jmp(["EVENT_557_pause_5"]),
	SetSyncActionScript(NPC_2, A0672_ROSE_TOWN_LIBERATED_WATER_KID, identifier="EVENT_557_set_action_script_8"),
	SetSyncActionScript(NPC_3, A0674_ROSE_TOWN_LIBERATED_WATER_KID),
	SetSyncActionScript(NPC_4, A0675_ROSE_TOWN_LIBERATED_WATER_KID),
	Pause(1, identifier="EVENT_557_pause_11"),
	JmpIfBitSet(TEMP_7044_0, ["EVENT_557_set_action_script_14"]),
	Jmp(["EVENT_557_pause_11"]),
	SetSyncActionScript(NPC_5, A0663_ROSE_TOWN_LIBERATED_WATER_GUY, identifier="EVENT_557_set_action_script_14"),
	Pause(1, identifier="EVENT_557_pause_15"),
	JmpIfBitSet(TEMP_7044_1, ["EVENT_557_apply_tile_mod_18"]),
	Jmp(["EVENT_557_pause_15"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=2, identifier="EVENT_557_apply_tile_mod_18"),
	ApplySolidityModToLevel(permanent=True, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=3),
	ClearBit(TEMP_7043_7),
	ClearBit(TEMP_7044_0),
	ClearBit(TEMP_7044_1),
	ClearBit(ROSE_TOWN_WATER_PUMPERS_POSITION),
	Pause(120),
	Jmp(["EVENT_557_pause_0"])
])
