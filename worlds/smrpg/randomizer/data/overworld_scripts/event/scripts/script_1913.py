# E1913_ABYSS_MACHINE_ARROW_ANIMATE
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
	JmpIfBitSet(TEMP_7043_1, ["EVENT_1913_ret_25"]),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_1913_ret_25"]),
	SetBit(TEMP_7043_0),
	ClearBit(TEMP_7043_2),
	Set7016701BToObjectXYZ(target=MARIO),
	AddConstToVar(Z_COORD_2, 2048),
	Set7000ToPressedButton(),
	JmpIf7000AllBitsClear(bits=[0, 1, 2, 3], destinations=["EVENT_1913_action_queue_24"]),
	Set7000ToPressedButton(),
	JmpIf7000AnyBitsSet(bits=[6], destinations=["EVENT_1913_set_7000_to_object_coord_11"]),
	SetBit(TEMP_7043_2),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_F, pixel=True, identifier="EVENT_1913_set_7000_to_object_coord_11"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_1913_add_const_to_var_18"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_1913_add_const_to_var_20"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1913_add_const_to_var_23"]),
	AddConstToVar(X_COORD_2, 65344),
	AddConstToVar(Y_COORD_2, 192),
	Jmp(["EVENT_1913_action_queue_24"]),
	AddConstToVar(Y_COORD_2, 65152, identifier="EVENT_1913_add_const_to_var_18"),
	Jmp(["EVENT_1913_action_queue_24"]),
	AddConstToVar(X_COORD_2, 384, identifier="EVENT_1913_add_const_to_var_20"),
	AddConstToVar(Y_COORD_2, 65344),
	Jmp(["EVENT_1913_action_queue_24"]),
	AddConstToVar(X_COORD_2, 384, identifier="EVENT_1913_add_const_to_var_23"),
	ActionQueueSync(target=NPC_8, subscript=[
		A_JmpIfBitClear(TEMP_7043_2, ["EVENT_1913_action_queue_24_SUBSCRIPT_db_2"]),
		A_Pause(4),
		A_UnknownCommand(bytearray(b'\x99'), identifier="EVENT_1913_action_queue_24_SUBSCRIPT_db_2"),
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
		A_PlaySound(sound=SO078_CLICK, channel=4),
		A_VisibilityOn(),
		A_FloatingOff(),
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZDownSteps(8),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_StartLoopNTimes(7),
		A_VisibilityOn(),
		A_Pause(1),
		A_VisibilityOff(),
		A_Pause(1),
		A_EndLoop(),
		A_ClearBit(TEMP_7043_0)
	], identifier="EVENT_1913_action_queue_24"),
	Return(identifier="EVENT_1913_ret_25")
])
