# E2416_FOREST_TRAMPOLINE_BUSINESS_LOGIC
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
	SetBit(DIRECTIONAL_7047_0, identifier="EVENT_2416_set_bit_0"),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_SetSpriteSequence(index=0, looping=False)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FixedFCoordOn(),
		A_FloatingOff(),
		A_SequencePlaybackOff(),
		A_ShadowOn(),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSouthPixels(8)
	]),
	SetAsyncActionScript(MARIO, A0408_JUMP_ON_SAVE_BLOCK),
	PlaySound(sound=SO010_TRAMPOLINE, channel=6),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(4),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\x0f\xf0\xff')),
		A_Pause(48),
		A_BPL262728()
	]),
	Pause(24),
	FadeOutToBlack(sync=False, duration=8),
	StopEmbeddedActionScript(MARIO),
	JmpIfBitSet(DIRECTIONAL_7045_0, ["EVENT_2416_clear_bit_15"]),
	JmpIfBitSet(DIRECTIONAL_7045_1, ["EVENT_2416_clear_bit_18"]),
	JmpIfBitSet(DIRECTIONAL_7045_2, ["EVENT_2416_clear_bit_21"]),
	JmpIfBitSet(DIRECTIONAL_7045_3, ["EVENT_2416_clear_bit_24"]),
	JmpIfBitSet(DIRECTIONAL_7045_4, ["EVENT_2416_clear_bit_27"]),
	JmpIfBitSet(DIRECTIONAL_7045_5, ["EVENT_2416_clear_bit_30"]),
	ClearBit(DIRECTIONAL_7045_0, identifier="EVENT_2416_clear_bit_15"),
	EnterArea(room_id=R226_FOREST_MAZE_AREA_02, face_direction=SOUTH, x=16, y=24, z=0, run_entrance_event=True),
	Return(),
	ClearBit(DIRECTIONAL_7045_1, identifier="EVENT_2416_clear_bit_18"),
	EnterArea(room_id=R228_FOREST_MAZE_AREA_04, face_direction=SOUTH, x=6, y=110, z=0, run_entrance_event=True),
	Return(),
	ClearBit(DIRECTIONAL_7045_2, identifier="EVENT_2416_clear_bit_21"),
	EnterArea(room_id=R229_FOREST_MAZE_AREA_06, face_direction=SOUTH, x=20, y=108, z=0, run_entrance_event=True),
	Return(),
	ClearBit(DIRECTIONAL_7045_2, identifier="EVENT_2416_clear_bit_24"),
	EnterArea(room_id=R231_FOREST_MAZE_SECRET_ENTRANCE, face_direction=SOUTH, x=19, y=74, z=0, run_entrance_event=True),
	Return(),
	ClearBit(DIRECTIONAL_7045_4, identifier="EVENT_2416_clear_bit_27"),
	EnterArea(room_id=R227_FOREST_MAZE_AREA_09_LEADS_TO_4PATH_MAZE, face_direction=SOUTH, x=6, y=40, z=0, run_entrance_event=True),
	Return(),
	ClearBit(DIRECTIONAL_7045_5, identifier="EVENT_2416_clear_bit_30"),
	JmpIfVarEqualsConst(TEMP_70AC, 1, ["EVENT_2416_enter_area_39"]),
	JmpIfVarEqualsConst(TEMP_70AC, 2, ["EVENT_2416_enter_area_41"]),
	JmpIfVarEqualsConst(TEMP_70AC, 3, ["EVENT_2416_enter_area_43"]),
	JmpIfVarEqualsConst(TEMP_70AC, 4, ["EVENT_2416_enter_area_45"]),
	JmpIfVarEqualsConst(TEMP_70AC, 5, ["EVENT_2416_enter_area_47"]),
	JmpIfVarEqualsConst(TEMP_70AC, 6, ["EVENT_2416_enter_area_49"]),
	EnterArea(room_id=R225_FOREST_MAZE_AREA_05_TREE_TRUNK_AREA, face_direction=SOUTH, x=4, y=74, z=0, run_entrance_event=True),
	Return(),
	EnterArea(room_id=R225_FOREST_MAZE_AREA_05_TREE_TRUNK_AREA, face_direction=SOUTH, x=16, y=92, z=0, run_entrance_event=True, identifier="EVENT_2416_enter_area_39"),
	Return(),
	EnterArea(room_id=R225_FOREST_MAZE_AREA_05_TREE_TRUNK_AREA, face_direction=SOUTH, x=13, y=98, z=0, run_entrance_event=True, identifier="EVENT_2416_enter_area_41"),
	Return(),
	EnterArea(room_id=R225_FOREST_MAZE_AREA_05_TREE_TRUNK_AREA, face_direction=SOUTH, x=12, y=86, z=0, run_entrance_event=True, identifier="EVENT_2416_enter_area_43"),
	Return(),
	EnterArea(room_id=R225_FOREST_MAZE_AREA_05_TREE_TRUNK_AREA, face_direction=SOUTH, x=9, y=92, z=0, run_entrance_event=True, identifier="EVENT_2416_enter_area_45"),
	Return(),
	EnterArea(room_id=R225_FOREST_MAZE_AREA_05_TREE_TRUNK_AREA, face_direction=SOUTH, x=9, y=78, z=0, run_entrance_event=True, identifier="EVENT_2416_enter_area_47"),
	Return(),
	EnterArea(room_id=R225_FOREST_MAZE_AREA_05_TREE_TRUNK_AREA, face_direction=SOUTH, x=6, y=84, z=0, run_entrance_event=True, identifier="EVENT_2416_enter_area_49"),
	Return()
])
