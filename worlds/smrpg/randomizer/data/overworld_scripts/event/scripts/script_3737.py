# E3737_NIMBUS_CASTLE_BACK_EXIT_LOADER
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
	JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_3585_fade_in_from_black_async_0"]),
	SetBit(NIMBUS_BOSS_IN_TOWN_SQUARE),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=15, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(1),
		A_ResetProperties(),
		A_ShadowOn()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_Walk1StepEast()
	]),
	FadeInFromBlack(sync=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_SetSequenceSpeed(FAST),
		A_Walk1StepNortheast(),
		A_SequenceLoopingOn(),
		A_Pause(60),
		A_SetSequenceSpeed(NORMAL),
		A_Pause(30),
		A_SetSequenceSpeed(SLOW),
		A_Pause(10),
		A_SequenceLoopingOff(),
		A_Pause(60),
		A_SetSpriteSequence(index=15, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=15, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(30),
		A_SetSpriteSequence(index=9, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(FAST),
		A_StartLoopNTimes(2),
		A_WalkSouthwestPixels(4),
		A_Pause(3),
		A_WalkNortheastPixels(4),
		A_EndLoop(),
		A_ResetProperties(),
		A_FaceSouthwest(),
		A_SequenceLoopingOn(),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(60),
		A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True),
		A_FloatingOn()
	]),
	Pause(10),
	FadeOutToBlack(sync=False),
	EnterArea(room_id=R371_NIMBUS_LAND_FALL_FROM_PLATFORM_1ST, face_direction=NORTHEAST, x=27, y=29, z=6),
	RunEventAtReturn(E3745_NIMBUS_BACK_EXIT_INITIATE_FALLING_SEQUENCE),
	Return()
])
