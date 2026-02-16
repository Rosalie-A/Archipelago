# E2524_STAR_HILL_2ND_ROOM_LOADER
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
	ActionQueueSync(target=NPC_16, subscript=[
		A_WalkEastPixels(7)
	]),
	ActionQueueSync(target=NPC_17, subscript=[
		A_WalkEastPixels(6)
	]),
	ActionQueueSync(target=NPC_18, subscript=[
		A_WalkWestPixels(9)
	]),
	ActionQueueSync(target=NPC_19, subscript=[
		A_WalkWestPixels(8)
	]),
	ActionQueueSync(target=NPC_20, subscript=[
		A_WalkWestPixels(10)
	]),
	FreezeCamera(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ShiftToXYCoords(x=14, y=22),
		A_OverwriteSolidity(),
		A_FloatingOff(),
		A_ShadowOn()
	]),
	FadeInFromBlack(sync=False),
	Pause(16),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R157_STAR_HILL_AREA_03, mod_id=0),
	PlaySound(sound=SO126_EMERGE_DEEP_WATER, channel=6),
	Pause(16),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSequenceSpeed(FAST),
		A_WalkSouthwestSteps(2)
	]),
	Pause(16),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R157_STAR_HILL_AREA_03, mod_id=13),
	PlaySound(sound=SO125_ENTER_DEEP_WATER, channel=6),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	UnfreezeCamera(),
	Return()
])
