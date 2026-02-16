# E2393_ABYSS_EXIT_TRAMPOLINE
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
	ExitToWorldMap(area=OW05_GATE, bit_6=True, bit_7=True),
	Return()
])
