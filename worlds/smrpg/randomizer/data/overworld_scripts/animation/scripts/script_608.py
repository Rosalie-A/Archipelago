#A0608_ROSE_WAY_5_CHEST_SHY_GUY
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.event_script_names import *
from ....variables.overworld_sfx_names import *
from ....variables.room_names import *
from ....variables.variable_names import *
from ....packets import *
from ....items import *

script = ActionScript([
	A_ShadowOn(),
	A_SetVRAMPriority(PRIORITY_3),
	A_SetPriority(3),
	A_SetObjectMemoryBits(arg_1=0x0E, bits=[0, 2]),
	A_FaceMario(identifier="ACTION_608_face_mario_4"),
	A_Pause(1),
	A_Set700CToPressedButton(),
	A_AddConstToVar(PRIMARY_TEMP_700C, 65535),
	A_JmpIfMem704XAt700CBitClear(["ACTION_608_face_mario_4"]),
	A_ShadowOff(),
	A_SetObjectMemoryBits(arg_1=0x0E, bits=[]),
	A_JumpToHeight(108),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 3),
	A_JmpIfComparisonResultIsGreaterOrEqual(["ACTION_608_set_sprite_sequence_19"]),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 7),
	A_JmpIfComparisonResultIsLesser(["ACTION_608_set_sprite_sequence_19"]),
	A_SetSpriteSequence(index=4, looping=False, mirror_sprite=True),
	A_Jmp(["ACTION_608_shift_f_direction_steps_20"]),
	A_SetSpriteSequence(index=4, looping=False, identifier="ACTION_608_set_sprite_sequence_19"),
	A_WalkFDirectionSteps(2, identifier="ACTION_608_shift_f_direction_steps_20"),
	A_SetVRAMPriority(NORMAL_PRIORITY),
	A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
	A_PlaySound(sound=SO079_YELP_IN_DISTANCE, channel=4),
	A_Pause(30),
	A_ResetProperties(),
	A_Set700CToPressedButton(identifier="ACTION_608_set_700C_to_pressed_button_26"),
	A_SetVarToConst(SECONDARY_TEMP_7024, 5),
	A_DecVarFrom700C(SECONDARY_TEMP_7024),
	A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_70A9),
	A_FaceSouthwest7D(arg=0x11),
	A_Walk1StepFDirection(),
	A_JumpToHeight(56),
	A_Pause(25),
	A_JmpIfRandom2of3(['ACTION_608_set_700C_to_pressed_button_26', 'ACTION_608_set_700C_to_pressed_button_26']),
	A_TurnRandomDirection(),
	A_Walk1StepFDirection(),
	A_Jmp(["ACTION_608_set_700C_to_pressed_button_26"])
])
