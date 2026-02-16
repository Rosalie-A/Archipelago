# E3219_SHIP_BARREL_PUZZLE_BUTTON
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
	SetSyncActionScript(MEM_70A8, A0336_SHIP_BARREL_PUZZLE_BUTTON),
	ActionQueueSync(target=MARIO, subscript=[
		A_JumpToHeight(height=0, silent=True),
		A_ClearSolidityBits(cant_pass_npcs=True),
		A_ShiftZDownPixels(2),
		A_ResetProperties(),
		A_SetSolidityBits(cant_pass_npcs=True)
	]),
	Inc(TEMP_70AE),
	JmpIfVarEqualsConst(TEMP_70AE, 2, ["EVENT_3219_action_queue_6"]),
	Return(),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_IncPaletteRowBy(15, 15)
	], identifier="EVENT_3219_action_queue_6"),
	SetSyncActionScript(NPC_3, A0338_SHIP_TRAMPOLINE_PUZZLE_SCROLL),
	JmpIfBitSet(UNKNOWN_707D_5, ["EVENT_3219_action_queue_15"]),
	SetVarToConst(X_COORD_1, 17),
	SetVarToConst(Y_COORD_1, 18),
	SetVarToConst(Z_COORD_1, 21),
	UnknownCommand(bytearray(b'\xfd\xc4')),
	Pause(1, identifier="EVENT_3219_pause_13"),
	RunEventAsSubroutine(E3389_SHIP_BARREL_PUZZLE_SPAWN_PRIZE),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4])
	], identifier="EVENT_3219_action_queue_15"),
	SetSyncActionScript(NPC_1, A0336_SHIP_BARREL_PUZZLE_BUTTON),
	SetSyncActionScript(NPC_2, A0336_SHIP_BARREL_PUZZLE_BUTTON),
	Return()
])
