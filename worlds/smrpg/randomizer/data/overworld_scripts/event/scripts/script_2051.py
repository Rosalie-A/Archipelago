# E2051_MONSTRO_SHOP_LOADER
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
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SequenceLoopingOn(),
		A_WalkSoutheastPixels(8),
		A_WalkNortheastPixels(2),
		A_FaceSouthwest(),
		A_SequenceLoopingOn(),
		A_VisibilityOn()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOff(),
		A_SetSequenceSpeed(NORMAL),
		A_SequenceLoopingOn(),
		A_WalkSoutheastPixels(12),
		A_WalkSouthwestPixels(4),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_ShadowOn()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOff(),
		A_SetSequenceSpeed(NORMAL),
		A_SequenceLoopingOn(),
		A_WalkSoutheastPixels(8),
		A_WalkSouthwestPixels(4),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_ShadowOn()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_FloatingOff(),
		A_SetSequenceSpeed(NORMAL),
		A_SequenceLoopingOn(),
		A_WalkSoutheastPixels(4),
		A_WalkSouthwestPixels(4),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_ShadowOn()
	]),
	ApplySolidityModToLevel(permanent=True, room_id=R398_MONSTRO_TOWN_WEAPON_AND_ARMOR_SHOP, mod_id=0),
	FadeInFromBlack(sync=False),
	Return()
])
