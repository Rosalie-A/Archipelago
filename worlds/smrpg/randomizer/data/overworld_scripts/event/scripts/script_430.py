# E0430_PIPE_VAULT_MARIO_HIT_BY_THWOMP
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
	ClearBit(TEMP_7043_3),
	JmpIfBitClear(TEMP_7043_4, ["EVENT_256_ret_0"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_VisibilityOff(),
		A_ShadowOn(),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_Pause(1, identifier="EVENT_430_action_queue_2_SUBSCRIPT_pause_3"),
		A_JmpIfBitClear(TEMP_7043_4, ["EVENT_430_action_queue_2_SUBSCRIPT_set_sprite_sequence_6"]),
		A_Jmp(["EVENT_430_action_queue_2_SUBSCRIPT_pause_3"]),
		A_SetSpriteSequence(index=8, sprite_offset=2, is_sequence=True, looping=True, identifier="EVENT_430_action_queue_2_SUBSCRIPT_set_sprite_sequence_6"),
		A_TransferToXYZF(x=25, y=28, z=10, direction=EAST),
		A_VisibilityOn(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSouthwestPixels(14),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FloatingOff(),
		A_StartLoopNTimes(3),
		A_SetSpriteSequence(index=2, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_TransferXYZFPixels(x=0, y=0, z=19, direction=NORTHEAST),
		A_ShiftZDownPixels(3),
		A_SetSpriteSequence(index=8, sprite_offset=2, is_sequence=True, looping=True),
		A_WalkSouthwestPixels(16),
		A_EndLoop(),
		A_Pause(60),
		A_FaceNortheast(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FloatingOn(),
		A_SetWalkingSpeed(NORMAL),
		A_ShadowOff()
	]),
	FreezeAllNPCsUntilReturn(),
	RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
	UnfreezeAllNPCs(),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return()
])
