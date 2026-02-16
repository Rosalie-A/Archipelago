# E2360_ABYSS_1ST_TRAMPOLINE_CATCHER_LOADER
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
	ActionQueueAsync(target=NPC_0, subscript=[
		A_WalkNortheastPixels(10)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_OverwriteSolidity(),
		A_FloatingOff(),
		A_TransferToXYZF(x=14, y=9, z=20, direction=EAST),
		A_WalkNorthPixels(14),
		A_WalkWestPixels(3)
	]),
	FadeInFromBlack(sync=False),
	PlaySound(sound=SO019_LONG_FALL, channel=6),
	Pause(64),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SequencePlaybackOff(),
		A_SetSpriteSequence(index=0, sprite_offset=3, is_mold=True, is_sequence=True, looping=True),
		A_OverwriteSolidity(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_FloatingOn(),
		A_Pause(1, identifier="EVENT_2360_action_queue_5_SUBSCRIPT_pause_4"),
		A_JmpIfMarioInAir(["EVENT_2360_action_queue_5_SUBSCRIPT_pause_4"]),
		A_PlaySound(sound=SO000_SILENCE, channel=4)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=0, looping=False, mirror_sprite=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSouthPixels(8)
	]),
	PlaySound(sound=SO010_TRAMPOLINE, channel=6),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkNorthwestSteps(4)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_ShadowOn(),
		A_UnknownCommand(bytearray(b' \x07')),
		A_UnknownCommand(bytearray(b'$\x00\xff\x00\xff')),
		A_UnknownCommand(bytearray(b'%\x00\x0c\xf0\xff')),
		A_Pause(32),
		A_BPL262728()
	]),
	Pause(24),
	FadeOutToBlack(sync=False, duration=16),
	StopEmbeddedActionScript(MARIO),
	StopEmbeddedActionScript(SCREEN_FOCUS),
	JmpIfVarEqualsConst(FACTORY_FALL_1, 220, ["EVENT_2360_set_var_to_const_32"]),
	JmpIfVarEqualsConst(FACTORY_FALL_1, 239, ["EVENT_2360_jmp_if_bit_set_38"]),
	SetBit(DIRECTIONAL_7045_7),
	JmpIfBitSet(DIRECTIONAL_7045_0, ["EVENT_2360_enter_area_24"]),
	JmpIfBitSet(DIRECTIONAL_7045_1, ["EVENT_2360_enter_area_26"]),
	JmpIfBitSet(DIRECTIONAL_7045_2, ["EVENT_2360_enter_area_28"]),
	JmpIfBitSet(DIRECTIONAL_7045_4, ["EVENT_2360_enter_area_30"]),
	EnterArea(room_id=R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS, face_direction=SOUTH, x=14, y=99, z=10, run_entrance_event=True),
	Jmp(["EVENT_2362_set_var_to_const_118"]),
	EnterArea(room_id=R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS, face_direction=SOUTH, x=4, y=124, z=10, run_entrance_event=True, identifier="EVENT_2360_enter_area_24"),
	Jmp(["EVENT_2362_set_var_to_const_40"]),
	EnterArea(room_id=R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS, face_direction=SOUTH, x=9, y=111, z=10, run_entrance_event=True, identifier="EVENT_2360_enter_area_26"),
	Jmp(["EVENT_2362_set_var_to_const_66"]),
	EnterArea(room_id=R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS, face_direction=SOUTH, x=14, y=121, z=10, run_entrance_event=True, identifier="EVENT_2360_enter_area_28"),
	Jmp(["EVENT_2362_set_var_to_const_92"]),
	EnterArea(room_id=R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS, face_direction=SOUTH, x=19, y=110, z=10, run_entrance_event=True, identifier="EVENT_2360_enter_area_30"),
	Jmp(["EVENT_2362_set_var_to_const_144"]),
	SetVarToConst(FACTORY_FALL_1, 238, identifier="EVENT_2360_set_var_to_const_32"),
	JmpIfBitSet(DIRECTIONAL_7045_1, ["EVENT_2360_enter_area_36"]),
	EnterArea(room_id=R220_SMITHY_FACTORY_AREA_02_WSAVE_POINT, face_direction=SOUTH, x=5, y=75, z=10, run_entrance_event=True),
	Jmp(["EVENT_2359_set_var_to_const_26"]),
	EnterArea(room_id=R220_SMITHY_FACTORY_AREA_02_WSAVE_POINT, face_direction=SOUTH, x=10, y=67, z=10, run_entrance_event=True, identifier="EVENT_2360_enter_area_36"),
	Jmp(["EVENT_2359_set_var_to_const_39"]),
	JmpIfBitSet(DIRECTIONAL_7045_0, ["EVENT_2360_enter_area_41"], identifier="EVENT_2360_jmp_if_bit_set_38"),
	EnterArea(room_id=R239_SMITHY_FACTORY_AREA_06_ULTRA_HAMMER, face_direction=NORTHEAST, x=21, y=53, z=7, run_entrance_event=True),
	Jmp(["EVENT_2409_jmp_if_bit_clear_50"]),
	EnterArea(room_id=R239_SMITHY_FACTORY_AREA_06_ULTRA_HAMMER, face_direction=NORTHEAST, x=29, y=37, z=10, run_entrance_event=True, identifier="EVENT_2360_enter_area_41"),
	Jmp(["EVENT_2409_set_var_to_const_32"])
])
