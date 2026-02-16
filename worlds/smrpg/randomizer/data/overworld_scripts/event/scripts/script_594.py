# E0594_MINES_BOSS_SHOVES_YOU
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
	MoveScriptToMainThread(),
	EnableControlsUntilReturn([]),
	JmpIfBitSet(MINES_BOSS_2_DEFEATED, ["EVENT_256_ret_0"]),
	StopAllBackgroundEvents(),
	UnsyncActionScript(NPC_0),
	FreezeCamera(),
	RunEventAsSubroutine(E0860_MINES_BOSS_SHOVE_SUBROUTINE),
	UnfreezeCamera(),
	Pause(30),
	FadeOutToBlack(sync=False),
	EnterArea(room_id=R288_MOLEVILLE_MINES_AREA_16_LARGE_SAVEPOINT_ROOM_WFOUR_BOBOMBS, face_direction=NORTHEAST, x=27, y=96, z=0),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=7, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthwestSteps(10),
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=6),
		A_JumpToHeight(height=64, silent=True),
		A_SetSpriteSequence(index=9, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(FAST),
		A_WalkNortheastSteps(2),
		A_ResetProperties(),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(40),
		A_SetWalkingSpeed(FASTEST),
		A_WalkNortheastPixels(4),
		A_WalkSouthwestPixels(8),
		A_WalkNortheastPixels(8),
		A_WalkSouthwestPixels(6),
		A_WalkNortheastPixels(2),
		A_WalkSouthwestPixels(4),
		A_WalkNortheastPixels(4),
		A_WalkSouthwestPixels(2)
	]),
	FadeInFromBlack(sync=True),
	PauseScriptUntilEffectDone(),
	RememberLastObject(),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Return()
])
