# E3221_SHIP_3D_MAZE_HIT_BUTTON
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
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_PlaySound(sound=SO009_GREEN_SWITCH, channel=4),
		A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4])
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_ShiftZDownPixels(1),
		A_ResetProperties()
	]),
	SetSyncActionScript(NPC_1, A0338_SHIP_TRAMPOLINE_PUZZLE_SCROLL),
	JmpIfBitSet(SHIP_MAZE_PRIZE, ["EVENT_3221_ret_10"]),
	SetVarToConst(X_COORD_1, 26),
	SetVarToConst(Y_COORD_1, 110),
	SetVarToConst(Z_COORD_1, 21),
	UnknownCommand(bytearray(b'\xfd\xc4')),
	Pause(1, identifier="EVENT_3221_pause_8"),
	RunEventAsSubroutine(E3386_SHIP_3D_MAZE_SPAWN_PRIZE),
	Return(identifier="EVENT_3221_ret_10")
])
