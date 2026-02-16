# E3686_MARRYMORE_SHOWER
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
	JmpIfBitSet(TEMP_7044_6, ["EVENT_3584_ret_0"]),
	SetBit(TEMP_7044_6),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouthwest(),
		A_VisibilityOff()
	]),
	Pause(30),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	ApplyTileModToLevel(use_alternate=False, room_id=R012_MARRYMORE_INN_SUITE_ROOM, mod_id=1),
	Pause(60),
	PlaySound(sound=SO155_POSTCREDITS_MARIO_THEME_WHISTLE, channel=6),
	Pause(120),
	PlaySound(sound=SO006_RUNNING_WATER, channel=4),
	Pause(480),
	StartLoopNTimes(2),
	PlaySound(sound=SO018_SUDDEN_STOP, channel=6),
	Pause(8),
	StopSound(),
	Pause(20),
	EndLoop(),
	Pause(120),
	PaletteSet(palette_set=142, row=1, bit_3=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferToXYZF(x=10, y=13, z=0, direction=EAST),
		A_TransferXYZFPixels(x=252, y=4, z=0, direction=EAST),
		A_VisibilityOn(),
		A_Pause(30),
		A_ClearSolidityBits(cant_pass_walls=True)
	]),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	ApplyTileModToLevel(use_alternate=True, room_id=R012_MARRYMORE_INN_SUITE_ROOM, mod_id=1),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkSouthwestSteps(2),
		A_Pause(60),
		A_FaceWest(),
		A_Pause(2),
		A_FaceNorthwest(),
		A_Pause(2),
		A_FaceNorth(),
		A_Pause(2),
		A_FaceNortheast()
	]),
	Pause(30),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	ApplyTileModToLevel(use_alternate=False, room_id=R012_MARRYMORE_INN_SUITE_ROOM, mod_id=1),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceEast(),
		A_Pause(2),
		A_FaceSoutheast(),
		A_Pause(2),
		A_FaceSouth()
	]),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	ClearBit(TEMP_7044_7),
	ClearBit(TEMP_7044_6),
	Return()
])
