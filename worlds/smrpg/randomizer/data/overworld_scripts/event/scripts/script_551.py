# E0551_ROSE_TOWN_OCCUPIED_MODS
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
	Pause(120),
	ApplyTileModToLevel(use_alternate=True, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=3),
	ApplySolidityModToLevel(permanent=True, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=1),
	SetSyncActionScript(NPC_5, A0664_ROSE_TOWN_OCCUPIED_WATER_GUY),
	Pause(60),
	ApplyTileModToLevel(use_alternate=False, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=2),
	ApplySolidityModToLevel(permanent=True, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=3),
	Pause(1, identifier="EVENT_551_pause_7"),
	JmpIfBitClear(ROSE_TOWN_WATER_PUMPERS_POSITION, ["EVENT_551_apply_tile_mod_10"]),
	Jmp(["EVENT_551_pause_7"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=3, identifier="EVENT_551_apply_tile_mod_10"),
	ApplySolidityModToLevel(permanent=True, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=1),
	Pause(60),
	ApplyTileModToLevel(use_alternate=True, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=2),
	ApplySolidityModToLevel(permanent=True, room_id=R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, mod_id=3),
	Pause(120),
	JmpToEvent(E0551_ROSE_TOWN_OCCUPIED_MODS)
])
