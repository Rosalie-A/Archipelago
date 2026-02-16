# E1591_LANDS_END_GROTTO_BARREL_KICK
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
	JmpIfBitSet(LANDS_END_GROTTO_BARREL_FLIPPED, ["EVENT_1591_ret_5"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_JumpToHeight(height=80, silent=True),
		A_SetWalkingSpeed(FAST),
		A_Walk1StepSouthwest(),
		A_SetWalkingSpeed(NORMAL),
		A_FloatingOn()
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkSoutheastSteps(4),
		A_WalkSouthSteps(2),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_PlaySound(sound=SO049_BIG_SHELL_HIT, channel=4),
		A_JumpToHeight(64),
		A_SetAllSpeeds(FAST),
		A_WalkSoutheastSteps(3),
		A_SetSolidityBits(cant_pass_walls=True),
		A_StartLoopNTimes(1),
		A_Pause(1, identifier="EVENT_1591_action_queue_3_SUBSCRIPT_pause_8"),
		A_JmpIfObjectInAir(NPC_0, ["EVENT_1591_action_queue_3_SUBSCRIPT_pause_8"]),
		A_PlaySound(sound=SO109_BIG_SHELL_HIT, channel=4),
		A_JumpToHeight(64),
		A_WalkEastPixels(14),
		A_EndLoop(),
		A_StartLoopNTimes(2),
		A_Pause(1, identifier="EVENT_1591_action_queue_3_SUBSCRIPT_pause_15"),
		A_JmpIfObjectInAir(NPC_0, ["EVENT_1591_action_queue_3_SUBSCRIPT_pause_15"]),
		A_PlaySound(sound=SO109_BIG_SHELL_HIT, channel=4),
		A_JumpToHeight(40),
		A_WalkEastPixels(6),
		A_EndLoop()
	]),
	SetBit(LANDS_END_GROTTO_BARREL_FLIPPED),
	Return(identifier="EVENT_1591_ret_5")
])
