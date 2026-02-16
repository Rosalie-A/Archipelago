# E3198_SHYGUY_CART_PUSHES_MARIO_INTO_SMALLER_ROOM
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
	PauseScriptIfMenuOpen(identifier="EVENT_3198_pause_script_if_menu_open_0"),
	DisableObjectTrigger(NPC_1),
	SetBit(TEMP_7044_7),
	ResumeActionScript(NPC_1),
	ResumeActionScript(NPC_6),
	PlaySound(sound=SO048_MINECART_START, channel=6),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True, cant_pass_npcs=True, bit_7=True),
		A_TransferToObjectXY(MEM_70A8),
		A_ShiftXYPixels(x=240, y=8),
		A_SetSpriteSequence(index=6, sprite_offset=3, is_sequence=True, looping=True),
		A_SetWalkingSpeed(FAST),
		A_WalkToXYCoords(x=2, y=124),
		A_VisibilityOff()
	]),
	RemoveObjectFromCurrentLevel(NPC_6),
	RemoveObjectFromSpecificLevel(NPC_6, R285_MOLEVILLE_MINES_AREA_13_LONG_MINECART_TRACKS_ROOM),
	EnterArea(room_id=R286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM, face_direction=SOUTHWEST, x=20, y=25, z=0),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	ClearBit(TEMP_7043_0),
	RunBackgroundEvent(event_id=E3413_MINES_SHYGUY_COLLIDE_WITH_BOXES, return_on_level_exit=True),
	ActionQueueSync(target=MARIO, subscript=[
		A_VisibilityOn(),
		A_ClearSolidityBits(cant_pass_npcs=True, bit_7=True),
		A_SetSpriteSequence(index=6, sprite_offset=3, is_sequence=True, looping=True),
		A_WalkToXYCoords(x=20, y=26),
		A_SetBit(TEMP_7043_2),
		A_JumpToHeight(height=128, silent=True),
		A_Pause(16),
		A_WalkSouthwestSteps(2),
		A_Pause(1, identifier="EVENT_3198_action_queue_13_SUBSCRIPT_pause_8"),
		A_JmpIfMarioInAir(["EVENT_3198_action_queue_13_SUBSCRIPT_pause_8"]),
		A_SetSpriteSequence(index=0, sprite_offset=3, is_mold=True, is_sequence=True, looping=True),
		A_JumpToHeight(height=32, silent=True),
		A_Pause(16),
		A_SetWalkingSpeed(NORMAL),
		A_ResetProperties(),
		A_FaceSoutheast(),
		A_SetSolidityBits(cant_pass_walls=True, cant_pass_npcs=True, bit_7=True)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(1, identifier="EVENT_3198_action_queue_14_SUBSCRIPT_pause_0"),
		A_JmpIfBitClear(TEMP_7043_2, ["EVENT_3198_action_queue_14_SUBSCRIPT_pause_0"]),
		A_PlaySound(sound=SO021_RUMBLING, channel=6),
		A_SetWalkingSpeed(FAST),
		A_StartLoopNTimes(3),
		A_WalkSouthwestPixels(4),
		A_WalkNortheastPixels(4),
		A_EndLoop(),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ShiftToXYCoords(x=21, y=24),
		A_SetSpriteSequence(index=7, is_sequence=True, looping=True),
		A_Pause(6),
		A_VisibilityOn(),
		A_WalkSouthwestSteps(2),
		A_StartLoopNTimes(1),
		A_WalkWestPixels(2),
		A_WalkEastPixels(2),
		A_EndLoop(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_Walk1StepNortheast(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_Pause(32),
		A_SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True),
		A_SequenceLoopingOff(),
		A_SequencePlaybackOff()
	]),
	JmpIfBitSet(RUNAWAY_MINECART_ITEM_OBTAINED, ["EVENT_3198_action_queue_17"]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetSequenceSpeed(FAST),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ShiftToXYCoords(x=21, y=24),
		A_TransferXYZFPixels(x=0, y=0, z=8, direction=EAST),
		A_SequencePlaybackOn(),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_Pause(6),
		A_VisibilityOn(),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=False),
		A_WalkSouthwestSteps(2),
		A_StartLoopNTimes(1),
		A_WalkWestPixels(2),
		A_WalkEastPixels(2),
		A_EndLoop(),
		A_JumpToHeight(128),
		A_SequenceLoopingOn(),
		A_SetAllSpeeds(NORMAL),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=False),
		A_PlaySound(sound=SO079_YELP_IN_DISTANCE, channel=4),
		A_SetBit(TEMP_7043_0),
		A_BounceToXYWithHeight(x=21, y=28, height=0),
		A_Pause(8),
		A_SetAllSpeeds(VERY_FAST),
		A_PlaySound(sound=SO024_TAPPING_FEET, channel=4),
		A_ResetProperties(),
		A_SequenceLoopingOn(),
		A_JumpToHeight(48),
		A_Pause(20),
		A_JumpToHeight(48),
		A_Pause(20),
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
		A_WalkToXYCoords(x=19, y=32),
		A_VisibilityOff(),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	], identifier="EVENT_3198_action_queue_17"),
	SummonObjectToSpecificLevel(NPC_0, R286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_1, R285_MOLEVILLE_MINES_AREA_13_LONG_MINECART_TRACKS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_0, R287_MOLEVILLE_MINES_AREA_14_2LEVEL_ROOM_FROM_LONG_MINECART_TRACKS_ROOM),
	Return()
])
