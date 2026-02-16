# E2058_MONSTRO_FAN_SETTING
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
	RunDialog(dialog_id=DI2987_FAN_SETTING, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBOrCSelected(['EVENT_2058_action_queue_4', 'EVENT_2058_action_queue_6']),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_Pause(5),
		A_PlaySound(sound=SO005_BLOCK_SWITCH, channel=4),
		A_SetSequenceSpeed(SLOW),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Return(),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_Pause(5),
		A_PlaySound(sound=SO005_BLOCK_SWITCH, channel=4),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True)
	], identifier="EVENT_2058_action_queue_4"),
	Return(),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_Pause(5),
		A_PlaySound(sound=SO005_BLOCK_SWITCH, channel=4),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True)
	], identifier="EVENT_2058_action_queue_6"),
	Return()
])
