# E2315_TOWER_PARACHUTE_ROOM_LOADER
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
	JmpIfBitSet(DIRECTIONAL_7045_0, ["EVENT_2315_jmp_if_bit_set_9"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShiftZUpSteps(15)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShiftZUpSteps(11),
		A_WalkSouthwestPixels(4)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ShiftZUpSteps(8)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_ShiftZUpSteps(15)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_FixedFCoordOn(),
		A_WalkEastPixels(4),
		A_ShiftZUpSteps(15)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_FixedFCoordOn(),
		A_WalkEastPixels(4),
		A_WalkSouthwestPixels(4),
		A_ShiftZUpSteps(11)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_FixedFCoordOn(),
		A_WalkEastPixels(4),
		A_ShiftZUpSteps(7)
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_FixedFCoordOn(),
		A_WalkEastPixels(4),
		A_ShiftZUpSteps(15)
	]),
	JmpIfBitSet(DIRECTIONAL_7045_0, ["EVENT_2315_freeze_camera_12"], identifier="EVENT_2315_jmp_if_bit_set_9"),
	FadeInFromBlack(sync=False),
	Jmp(["EVENT_2315_jmp_if_bit_clear_20"]),
	FreezeCamera(identifier="EVENT_2315_freeze_camera_12"),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthSteps(8),
		A_SetWalkingSpeed(FAST)
	]),
	FadeInFromBlack(sync=False),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkSouthSteps(6),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=3, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_ShadowOn(),
		A_UnknownCommand(bytearray(b' \x07')),
		A_UnknownCommand(bytearray(b'$\xc0\x00`\x00')),
		A_UnknownCommand(bytearray(b'%\x00\n\x80\xff')),
		A_Pause(40),
		A_BPL262728(),
		A_PlaySound(sound=SO058_INSERT, channel=4)
	]),
	StopEmbeddedActionScript(MARIO),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	StopEmbeddedActionScript(SCREEN_FOCUS),
	JmpIfBitClear(DIRECTIONAL_7045_0, ["EVENT_2315_unfreeze_camera_22"], identifier="EVENT_2315_jmp_if_bit_clear_20"),
	Pause(24),
	UnfreezeCamera(identifier="EVENT_2315_unfreeze_camera_22"),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	ClearBit(DIRECTIONAL_7045_0),
	Return()
])
