# E2478_BEAN_VALLEY_BEANSTALK_ROOM_LOADER
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
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 39),
	SummonObjectToSpecificLevel(NPC_0, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
	SummonObjectToSpecificLevel(NPC_1, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
	SummonObjectToSpecificLevel(NPC_3, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
	SummonObjectToSpecificLevel(NPC_4, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
	SummonObjectToSpecificLevel(NPC_5, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
	SummonObjectToSpecificLevel(NPC_6, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
	SummonObjectToSpecificLevel(NPC_7, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
	SummonObjectToSpecificLevel(NPC_9, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
	SummonObjectToSpecificLevel(NPC_10, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
	SummonObjectToSpecificLevel(NPC_11, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_WalkNortheastPixels(5),
		A_WalkNorthPixels(5),
		A_WalkWestPixels(2),
		A_JmpIfBitClear(TEMP_708C_4, ["EVENT_2478_action_queue_11_SUBSCRIPT_set_sprite_sequence_8"]),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True),
		A_ReturnQueue(),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, identifier="EVENT_2478_action_queue_11_SUBSCRIPT_set_sprite_sequence_8"),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_WalkNortheastPixels(7),
		A_WalkEastPixels(4),
		A_WalkNorthPixels(1),
		A_WalkWestPixels(2),
		A_JmpIfBitClear(TEMP_708C_4, ["EVENT_2478_action_queue_12_SUBSCRIPT_set_sprite_sequence_9"]),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True),
		A_ReturnQueue(),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, identifier="EVENT_2478_action_queue_12_SUBSCRIPT_set_sprite_sequence_9"),
		A_VisibilityOff()
	]),
	JmpIfBitClear(TEMP_708C_4, ["EVENT_2478_set_7000_to_object_coord_15"]),
	SetSyncActionScript(NPC_2, A0015_DO_NOTHING),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Y, pixel=True, bit_7=True, identifier="EVENT_2478_set_7000_to_object_coord_15"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 27, ["EVENT_2478_freeze_camera_19"]),
	FadeInFromBlack(sync=False),
	Return(),
	FreezeCamera(identifier="EVENT_2478_freeze_camera_19"),
	ActionQueueSync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_ShadowOn(),
		A_SetWalkingSpeed(FASTEST),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetPriority(3),
		A_OverwriteSolidity(),
		A_SetSpriteSequence(index=7, sprite_offset=6, is_sequence=True, looping=True),
		A_TransferToXYZF(x=27, y=27, z=24, direction=EAST),
		A_WalkEastPixels(8),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkToXYCoords(x=22, y=5),
		A_SetWalkingSpeed(NORMAL)
	]),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_UnknownCommand(bytearray(b' \x01')),
		A_UnknownCommand(bytearray(b'$\xe3\xff\x00\x00')),
		A_ShiftZDownSteps(8),
		A_BPL262728(),
		A_SetSpriteSequence(index=14, sprite_offset=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(16)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=3, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_FaceSouthwest(),
		A_PlaySound(sound=SO004_JUMP, channel=4),
		A_UnknownCommand(bytearray(b' \x07')),
		A_UnknownCommand(bytearray(b'$\x80\xfe\xb0\x00')),
		A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
		A_Pause(37),
		A_BPL262728()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkSouthSteps(4)
	]),
	UnfreezeCamera(),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return()
])
