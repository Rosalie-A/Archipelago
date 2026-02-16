#A0666_PIPE_VAULT_PIRANHA
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
	A_ShadowOn(identifier="ACTION_666_shadow_on_0"),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_Pause(60),
	A_Pause(1, identifier="ACTION_666_pause_3"),
	A_JmpIfBitClear(TEMP_7044_4, ["ACTION_666_visibility_on_6"]),
	A_Jmp(["ACTION_666_shadow_on_0"]),
	A_VisibilityOn(identifier="ACTION_666_visibility_on_6"),
	A_SetPriority(3),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_AddZCoord1Step(),
	A_ShiftZUpPixels(12),
	A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
	A_Pause(48),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_DecZCoord1Step(),
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_ShiftZDownPixels(12),
	A_VisibilityOff(),
	A_JmpIfRandom1of2(["ACTION_666_pause_3"]),
	A_Jmp(["ACTION_666_shadow_on_0"])
])
