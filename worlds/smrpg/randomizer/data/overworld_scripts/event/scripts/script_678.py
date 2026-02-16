# E0678_MARRYMORE_JUMP_ON_ORGAN_PIPE
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
	JmpIfBitSet(TEMP_7043_0, ["EVENT_256_ret_0"]),
	SetBit(TEMP_7043_0),
	PlaySound(sound=SO131_JUMP_ON_ORGAN, channel=6),
	SetSyncActionScript(NPC_0, A0636_54_VELOCITY_SINGLE_JUMP),
	SetSyncActionScript(NPC_5, A0636_54_VELOCITY_SINGLE_JUMP),
	SetSyncActionScript(NPC_4, A0636_54_VELOCITY_SINGLE_JUMP),
	Pause(30),
	StopSound(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True),
		A_JumpToHeight(height=108, silent=True),
		A_Pause(1, identifier="EVENT_678_action_queue_8_SUBSCRIPT_pause_2"),
		A_JmpIfMarioInAir(["EVENT_678_action_queue_8_SUBSCRIPT_pause_2"])
	]),
	RunDialog(dialog_id=DI2184_JUMP_ON_ORGAN, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_JumpToHeight(96),
		A_WalkSoutheastSteps(2),
		A_WalkSoutheastPixels(8),
		A_Pause(1, identifier="EVENT_678_action_queue_10_SUBSCRIPT_pause_4"),
		A_JmpIfMarioInAir(["EVENT_678_action_queue_10_SUBSCRIPT_pause_4"])
	]),
	ClearBit(TEMP_7043_0),
	SetSyncActionScript(NPC_0, A0119_SLOW_SEQUENCE_LOOP),
	SetSyncActionScript(NPC_5, A0119_SLOW_SEQUENCE_LOOP),
	SetSyncActionScript(NPC_4, A0119_SLOW_SEQUENCE_LOOP),
	Return()
])
