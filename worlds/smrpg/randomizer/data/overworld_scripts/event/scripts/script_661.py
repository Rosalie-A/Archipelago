# E0661_BOWSERS_KEEP_BUTTON_ROOM_FORFEIT
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
	RunDialog(dialog_id=DI2888_DR_TOPPER_PROMPT_TO_QUIT_BUTTON_PUZZLE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_661_play_sound_3"]),
	Jmp(["EVENT_661_action_queue_12"]),
	PlaySound(sound=SO088_WRONG_SIGNAL, channel=4, identifier="EVENT_661_play_sound_3"),
	Pause(16),
	SetBit(TEMP_7044_7),
	PlayMusicAtDefaultVolume(M0066_BOWSER_SCASTLE_2NDTIME),
	SlowDownMusic(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=12, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(2)
	]),
	Pause(180),
	FadeOutToBlack(sync=False),
	JmpToEvent(E3356_KEEP_RESPAWN_IN_LOBBY_UPON_FAILURE),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkToXYCoords(x=23, y=31)
	], identifier="EVENT_661_action_queue_12"),
	Return()
])
