# E1672_LANDS_END_2_SUMMON_INVISIBLE_PLATFORM
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
	RunEventAsSubroutine(E1840_PLATFORM_SUBROUTINE),
	JmpIfBitSet(TEMP_7043_2, ["EVENT_1672_jmp_fork_mario_on_object_8"]),
	JmpIfMarioOnAnObjectOrNot(['EVENT_1672_ret_3', 'EVENT_1672_play_sound_4']),
	Return(identifier="EVENT_1672_ret_3"),
	PlaySound(sound=SO014_FLOWER, channel=6, identifier="EVENT_1672_play_sound_4"),
	ActionQueueSync(target=NPC_4, subscript=[
		A_VisibilityOn(),
		A_FixedFCoordOn(),
		A_ShiftZUpPixels(12),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	SetBit(TEMP_7043_2),
	Return(),
	JmpIfMarioOnAnObjectOrNot(['EVENT_1672_jmp_if_bit_set_10', 'EVENT_1672_ret_3'], identifier="EVENT_1672_jmp_fork_mario_on_object_8"),
	Jmp(["EVENT_1672_ret_3"]),
	JmpIfBitSet(TEMP_7043_4, ["EVENT_1672_ret_3"], identifier="EVENT_1672_jmp_if_bit_set_10"),
	SetBit(TEMP_7043_4),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTER),
		A_WalkNorthSteps(3),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Walk1StepSoutheast(),
		A_WalkNortheastSteps(4),
		A_WalkSouthwestSteps(4),
		A_Walk1StepNorthwest()
	]),
	Return()
])
