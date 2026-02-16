# E2423_ABYSS_TRAMPOLINE_TO_1ST_BOSS
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
	StopAllBackgroundEvents(),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_SetSpriteSequence(index=0, looping=False, mirror_sprite=True)
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
		A_SetSpriteSequence(index=4, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_UnknownCommand(bytearray(b' \x07')),
		A_UnknownCommand(bytearray(b'$0\x02\xe0\xfe')),
		A_UnknownCommand(bytearray(b'%\x00\t\x80\xff')),
		A_Pause(56),
		A_BPL262728()
	]),
	Pause(24),
	FreezeCamera(),
	Pause(24),
	FadeOutToBlack(sync=False, duration=16),
	StopEmbeddedActionScript(MARIO),
	JmpIfBitSet(ABYSS_BOSS_1_DEFEATED, ["EVENT_2423_enter_area_14"]),
	EnterArea(room_id=R223_SMITHY_FACTORY_AREA_07_COUNT_DOWNS_ROOM, face_direction=SOUTH, x=4, y=113, z=10, run_entrance_event=True),
	Return(),
	EnterArea(room_id=R507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN, face_direction=SOUTH, x=15, y=10, z=0, run_entrance_event=True, identifier="EVENT_2423_enter_area_14"),
	Return()
])
