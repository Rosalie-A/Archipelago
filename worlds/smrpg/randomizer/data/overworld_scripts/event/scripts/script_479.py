# E0479_DISMOUNT_YOSHI_3
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
	JmpIfBitClear(TEMP_7044_5, ["EVENT_256_ret_0"]),
	UnknownCommand(bytearray(b'\xfdE')),
	PauseActionScript(NPC_9),
	ActionQueueSync(target=NPC_9, subscript=[
		A_FaceSouthwest(),
		A_SetSequenceSpeed(FAST)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=5, sprite_offset=6, is_sequence=True, looping=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetWalkingSpeed(SLOW),
		A_BounceToXYWithHeight(x=23, y=54, height=0),
		A_FaceSouthwest()
	]),
	PauseActionScript(NPC_9),
	StartAsyncEmbeddedActionScript(target=NPC_9, prefix=0xF1, subscript=[
		A_SetSequenceSpeed(SLOW),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[]),
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	ClearBit(TEMP_7044_0),
	ClearBit(TEMP_7044_1),
	ClearBit(TEMP_7044_2),
	ClearBit(TEMP_7044_3),
	ClearBit(TEMP_7044_5),
	SetVarToConst(ROSE_WAY_703E, 7),
	SetSyncActionScript(NPC_9, A0289_MARIO_DISMOUNT_YOSHI),
	SetAsyncActionScript(MARIO, A0288_MARIO_DISMOUNT_YOSHI),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetSolidityBits(cant_walk_through=True)
	]),
	ClearBit(TEMP_7044_4),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	Return()
])
