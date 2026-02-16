# E1848_CANNONBALL_ROOM_BOMB_2
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
	JmpIf316DIs3(["EVENT_1848_enable_controls_10"]),
	FreezeAllNPCsUntilReturn(),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	EnableControlsUntilReturn([]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_PlaySound(sound=SO089_LIT_FUSE, channel=4),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True),
		A_Pause(30)
	]),
	Pause(1, identifier="EVENT_1848_pause_5"),
	CreatePacketAtObjectCoords(packet=P024_REGULAR_SOUND_EXPLOSION, target_npc=NPC_2, destinations=["EVENT_1848_pause_5"]),
	PlaySound(sound=SO060_DYNAMITE_BOMB_EXPLOSION, channel=6),
	RemoveObjectFromCurrentLevel(NPC_2),
	Jmp(["EVENT_1847_action_queue_9"]),
	EnableControls([], identifier="EVENT_1848_enable_controls_10"),
	RunBackgroundEvent(event_id=E1850_CANNONBALL_ROOM_BOMB_2_CONTD, return_on_level_exit=True),
	Return()
])
