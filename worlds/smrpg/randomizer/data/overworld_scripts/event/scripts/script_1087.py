# E1087_MELODY_BAY_EXIT_WATER_ANIMATION
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
	PauseActionScript(MARIO),
	UnfreezeCamera(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_JumpToHeight(64),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\x00\x02\x00\xff')),
		A_Pause(16),
		A_BPL262728()
	]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1087_action_queue_12"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_1087_action_queue_14"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_1087_action_queue_14"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_1087_action_queue_14"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 65535, ["EVENT_1087_action_queue_10"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 65534, ["EVENT_1087_action_queue_10"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 65533, ["EVENT_1087_action_queue_10"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=13, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True)
	], identifier="EVENT_1087_action_queue_10"),
	Jmp(["EVENT_1087_action_queue_15"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=14, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True)
	], identifier="EVENT_1087_action_queue_12"),
	Jmp(["EVENT_1087_action_queue_15"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=14, sprite_offset=1, is_sequence=True, looping=True)
	], identifier="EVENT_1087_action_queue_14"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_PlaySound(sound=SO093_JUMP_INTO_WATER, channel=6),
		A_Pause(10),
		A_WalkToXYCoords(x=15, y=32)
	], identifier="EVENT_1087_action_queue_15"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_Pause(10),
		A_JumpToHeight(64),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$\x00\x02\x00\xff')),
		A_Pause(16),
		A_BPL262728()
	]),
	Return()
])
