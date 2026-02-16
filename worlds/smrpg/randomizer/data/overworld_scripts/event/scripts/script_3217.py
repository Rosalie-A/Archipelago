# E3217_SHIP_CANNONBALL_PUZZLE_CANNONBALL
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
	PauseActionScript(MEM_70A8),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_JumpToHeight(height=96, silent=True),
		A_Pause(20),
		A_VisibilityOff()
	]),
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	Dec(PRIMARY_TEMP_7000),
	Dec(PRIMARY_TEMP_7000),
	Dec(PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
	JmpIfObjectsAreLessThanXYStepsApart(MEM_70A8, MEM_70A9, 192, 0, ["EVENT_3217_pause_9"]),
	Return(),
	Pause(12, identifier="EVENT_3217_pause_9"),
	PauseActionScript(MEM_70A9),
	SetTempSyncActionScript(MEM_70A9, A0337_VARIOUS_SHIP_OBJECTS),
	PlaySound(sound=SO087_CORRECT_SIGNAL, channel=4),
	Inc(TEMP_70AF),
	JmpIfVarEqualsConst(TEMP_70AF, 3, ["EVENT_3217_set_action_script_20"]),
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	Inc(PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
	SetSyncActionScript(MEM_70A9, A0319_SHIP_CANNONBALL_PUZZLE_CANNONBALL),
	Return(),
	SetSyncActionScript(NPC_7, A0338_SHIP_TRAMPOLINE_PUZZLE_SCROLL, identifier="EVENT_3217_set_action_script_20"),
	JmpIfBitSet(SHIP_CANNONBALL_PRIZE, ["EVENT_3217_ret_28"]),
	SetVarToConst(X_COORD_1, 7),
	SetVarToConst(Y_COORD_1, 62),
	SetVarToConst(Z_COORD_1, 21),
	UnknownCommand(bytearray(b'\xfd\xc4')),
	Pause(1),
	RunEventAsSubroutine(E3387_SHIP_CANNONBALL_PUZZLE_SPAWN_PRIZE),
	Return(identifier="EVENT_3217_ret_28")
])
