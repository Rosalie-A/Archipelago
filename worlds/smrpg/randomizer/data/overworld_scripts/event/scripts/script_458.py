# E0458_MUSHROOM_DERBY_BEGINS
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
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkToXYCoords(x=7, y=65),
		A_SetWalkingSpeed(SLOW)
	]),
	ClearBit(YOSHI_UNKNOWN_7061_7),
	UnknownCommand(bytearray(b'\xfdE')),
	PauseActionScript(NPC_9),
	ClearBit(TEMP_7044_5),
	EnableControls([]),
	StartSyncEmbeddedActionScript(target=NPC_9, prefix=0xF1, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[]),
		A_TransferToXYZF(x=10, y=81, z=0, direction=EAST),
		A_FaceNortheast(),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ClearSolidityBits(cant_pass_walls=True)
	]),
	StartAsyncEmbeddedActionScript(target=MARIO, prefix=0xF1, subscript=[
		A_SetSpriteSequence(index=6, sprite_offset=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_TransferToXYZF(x=10, y=81, z=0, direction=EAST),
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	JmpToSubroutine(["EVENT_457_action_queue_0"]),
	FadeInFromBlack(sync=True, duration=60),
	JmpIfBitSet(MUSHROOM_DERBY_AUTO, ["EVENT_458_jmp_to_event_13"]),
	RunBackgroundEvent(event_id=E0465_MUSHROOM_DERBY_BUSINESS_LOGIC, return_on_level_exit=True, run_as_second_script=True),
	Return(),
	JmpToEvent(E3601_MUSHROOM_DERBY_YOSHI_AUTOPLAY, identifier="EVENT_458_jmp_to_event_13")
])
