# E0505_PIPE_VAULT_MARIO_THWOMP_TUMBLE
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
	Pause(1, identifier="EVENT_505_pause_0"),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_505_pause_3"]),
	Jmp(["EVENT_505_pause_0"]),
	Pause(1, identifier="EVENT_505_pause_3"),
	JmpIfMarioInAir(["EVENT_505_pause_3"]),
	JmpIfBitClear(TEMP_7043_2, ["EVENT_505_pause_0"]),
	JmpIfBitClear(TEMP_7043_3, ["EVENT_505_pause_0"]),
	EnableControls([]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetSpriteSequence(index=9, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(height=72, silent=True),
		A_WalkSouthwestSteps(2),
		A_Pause(1, identifier="EVENT_505_action_queue_8_SUBSCRIPT_pause_5"),
		A_JmpIfMarioInAir(["EVENT_505_action_queue_8_SUBSCRIPT_pause_5"]),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=6, sprite_offset=3, is_sequence=True, looping=True),
		A_WalkToXYCoords(x=21, y=36)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouthwest(),
		A_ResetProperties(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetWalkingSpeed(NORMAL)
	]),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	ClearBit(TEMP_7043_3),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	JmpToEvent(E0505_PIPE_VAULT_MARIO_THWOMP_TUMBLE)
])
