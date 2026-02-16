# E3361_KEEP_EXIT_COMPLETED_DOORS_TO_BOSS_ANTECHAMBER
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
	EnterArea(room_id=R448_BOWSERS_KEEP_AREA_09_TALL_ROOM_WSAVE_POINT, face_direction=SOUTHEAST, x=2, y=42, z=10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_WalkSoutheastPixels(3)
	]),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JmpIfBitSet(MAGIKOOPA_SAVE_ANIMATION_DONE, ["EVENT_3361_action_queue_3_SUBSCRIPT_set_solidity_bits_19"]),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(64),
		A_ResetProperties(),
		A_Pause(32),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(24),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=3, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(64),
		A_StartLoopNTimes(7),
		A_SetSpriteSequence(index=8, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(4),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_EndLoop(),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True),
		A_Pause(48),
		A_FaceNorthwest(),
		A_ResetProperties(),
		A_SetSolidityBits(cant_pass_walls=True, identifier="EVENT_3361_action_queue_3_SUBSCRIPT_set_solidity_bits_19"),
		A_FloatingOn(),
		A_JumpToHeight(height=0, silent=True),
		A_PlaySound(sound=SO019_LONG_FALL, channel=4),
		A_Pause(1, identifier="EVENT_3361_action_queue_3_SUBSCRIPT_pause_23"),
		A_JmpIfMarioInAir(["EVENT_3361_action_queue_3_SUBSCRIPT_pause_23"]),
		A_PlaySound(sound=SO058_INSERT, channel=4),
		A_SetBit(MAGIKOOPA_SAVE_ANIMATION_DONE),
		A_SetSequenceSpeed(NORMAL)
	]),
	Return()
])
