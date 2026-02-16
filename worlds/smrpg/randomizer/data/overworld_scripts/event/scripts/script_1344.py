# E1344_TOWER_HENCHMAN_2_ROOM_LOADER
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
	ApplyTileModToLevel(use_alternate=True, room_id=R194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM, mod_id=32),
	ApplyTileModToLevel(use_alternate=True, room_id=R194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM, mod_id=33),
	JmpIfBitClear(SPOOKUM_DIRECTION, ["EVENT_1344_pause_action_script_5"]),
	PlayMusicAtDefaultVolume(M0032_ANDMYNAME_SBOOSTER),
	ClearBit(SPOOKUM_DIRECTION),
	PauseActionScript(NPC_0, identifier="EVENT_1344_pause_action_script_5"),
	PauseActionScript(NPC_1),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_WalkSouthwestPixels(6),
		A_FaceSoutheast()
	]),
	RunEventAsSubroutine(E0798_TOWER_FIRST_RAIL_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	Return()
])
