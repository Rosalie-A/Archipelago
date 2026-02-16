# E1861_KEEP_DONKEY_ROOM_DONKEY
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
	SetBit(TEMP_7043_0),
	StopAllBackgroundEvents(),
	Pause(2),
	ActionQueueSync(target=MARIO, subscript=[
		A_FixedFCoordOn(),
		A_JumpToHeight(height=48, silent=True),
		A_WalkSoutheastSteps(2),
		A_FixedFCoordOff(),
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_PlaySound(sound=SO119_CZAR_DRAGON_ROAR, channel=4),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetWalkingSpeed(FAST),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_StartLoopNTimes(1),
		A_WalkSouthwestSteps(2),
		A_Pause(1, identifier="EVENT_1861_action_queue_4_SUBSCRIPT_pause_11"),
		A_JmpIfObjectInAir(NPC_8, ["EVENT_1861_action_queue_4_SUBSCRIPT_pause_11"]),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
		A_EndLoop(),
		A_WalkSouthwestSteps(2),
		A_VisibilityOff()
	]),
	Return()
])
