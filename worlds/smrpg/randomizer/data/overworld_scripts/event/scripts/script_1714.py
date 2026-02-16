# E1714_BANDITS_WAY_1_LOADER
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
	ActionQueueSync(target=NPC_0, subscript=[
		A_WalkWestPixels(4)
	]),
	RunEventAsSubroutine(E0757_BANDITS_WAY_AREA_01_SHUFFLED_NPC_ANIMATION_LOADER),
	JmpIfBitClear(BANDITS_WAY_CUTSCENE_1_VIEWED, ["EVENT_1714_set_bit_5"]),
	RunEventAsSubroutine(E0014_STANDARD_ROOM_LOADER),
	Jmp(["EVENT_1714_jmp_if_bit_clear_12"]),
	SetBit(BANDITS_WAY_CUTSCENE_1_VIEWED, identifier="EVENT_1714_set_bit_5"),
	FadeInFromBlack(sync=True),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_VisibilityOn(),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True, identifier="bway_distracted_1"),
		A_Pause(135),
		A_ResetProperties()
	], identifier="bway_aqueue_1"),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_JumpToHeight(96),
		A_Pause(8),
		A_FaceSouthwest(),
		A_Pause(8),
		A_FaceNorthwest(),
		A_SequenceLoopingOn()
	]),
	Pause(10),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetPriority(3),
		A_SetAllSpeeds(FAST),
		A_Walk1StepSouthwest(),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_JumpToHeight(96),
		A_WalkSouthSteps(4),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_JumpToHeight(108),
		A_WalkSoutheastSteps(6),
		A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
		A_SetAllSpeeds(FASTER),
		A_WalkEastSteps(6),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkSouthSteps(4),
		A_SetAllSpeeds(FASTER),
		A_WalkSoutheastSteps(6),
		A_Pause(30),
		A_WalkNorthwestSteps(6),
		A_SetWalkingSpeed(FAST),
		A_WalkNorthSteps(4),
		A_SetWalkingSpeed(NORMAL)
	]),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_1714_ret_16"], identifier="EVENT_1714_jmp_if_bit_clear_12"),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1714_ret_16"]),
	RunEventAsSubroutine(E3890_BANDITS_WAY_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_1714_ret_16")
])
