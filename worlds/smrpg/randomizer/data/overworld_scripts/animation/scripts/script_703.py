#A0703_TOWER_CHOMP_GROUP
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
	A_JmpIfRandom2of3(['ACTION_703_set_700C_to_pressed_button_18', 'ACTION_703_set_700C_to_pressed_button_18'], identifier="ACTION_703_jmp_if_random_above_66_0"),
	A_JmpIfRandom1of2(["ACTION_703_set_700C_to_pressed_button_10"]),
	A_Set700CToPressedButton(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 20, ["ACTION_703_set_sprite_sequence_7"]),
	A_SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(58),
	A_Jmp(["ACTION_703_jmp_if_random_above_66_0"]),
	A_SetSpriteSequence(index=3, is_sequence=True, looping=True, identifier="ACTION_703_set_sprite_sequence_7"),
	A_Pause(58),
	A_Jmp(["ACTION_703_jmp_if_random_above_66_0"]),
	A_Set700CToPressedButton(identifier="ACTION_703_set_700C_to_pressed_button_10"),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 20, ["ACTION_703_set_sprite_sequence_15"]),
	A_SetSpriteSequence(index=4, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(56),
	A_Jmp(["ACTION_703_jmp_if_random_above_66_0"]),
	A_SetSpriteSequence(index=4, is_sequence=True, looping=True, identifier="ACTION_703_set_sprite_sequence_15"),
	A_Pause(56),
	A_Jmp(["ACTION_703_jmp_if_random_above_66_0"]),
	A_Set700CToPressedButton(identifier="ACTION_703_set_700C_to_pressed_button_18"),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 20, ["ACTION_703_set_sprite_sequence_23"]),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
	A_Pause(112),
	A_Jmp(["ACTION_703_jmp_if_random_above_66_0"]),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True, identifier="ACTION_703_set_sprite_sequence_23"),
	A_Pause(112),
	A_Jmp(["ACTION_703_jmp_if_random_above_66_0"])
])
