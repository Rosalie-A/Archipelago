# E1333_PORTRAIT_GAME_2
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
	JmpIfBitSet(TEMP_7043_4, ["EVENT_1333_ret_17"]),
	JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 4, ["EVENT_1333_apply_tile_mod_10"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=39),
	Pause(5),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=41),
	PlaySound(sound=SO088_WRONG_SIGNAL, channel=6),
	Pause(30),
	StartBattleAtBattlefield(PACK046_SPOOKUM_WITH_OTHER_MONSTERS, BF12_BOOSTER_TOWER),
	FadeInFromBlack(sync=False),
	Jmp(["EVENT_1338_pause_0"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=39, identifier="EVENT_1333_apply_tile_mod_10"),
	Pause(5),
	ApplyTileModToLevel(use_alternate=True, room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, mod_id=40),
	PlaySound(sound=SO087_CORRECT_SIGNAL, channel=6),
	Pause(10),
	Inc(SECONDARY_TEMP_7024),
	SetBit(TEMP_7043_4),
	Return(identifier="EVENT_1333_ret_17")
])
