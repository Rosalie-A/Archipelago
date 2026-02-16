# E1675_MARIO_BUMPED_OFF_CANNON
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
	Set7016701BToObjectXYZ(target=MEM_70A8, bit_7=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetAllSpeeds(FAST),
		A_FloatingOff(),
		A_WalkTo70167018(),
		A_PlaySound(sound=SO066_KICK_BALL_SHELL, channel=4),
		A_JumpToHeight(height=96, silent=True),
		A_FloatingOn(),
		A_SetSpriteSequence(index=7, sprite_offset=3, is_sequence=True, looping=True),
		A_Pause(1)
	]),
	ResumeActionScript(MEM_70A8),
	MoveScriptToBackgroundThread2(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkNorthwestSteps(5)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSoutheastPixels(4),
		A_WalkNorthwestPixels(8),
		A_WalkSoutheastPixels(8),
		A_WalkNorthwestPixels(4),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
		A_JumpToHeight(height=80, silent=True),
		A_Walk1StepSouth(),
		A_SetAllSpeeds(NORMAL),
		A_SetSpriteSequence(index=7, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(60),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
		A_SetSpriteSequence(index=8, sprite_offset=2, is_sequence=True, looping=True)
	]),
	Pause(1, identifier="EVENT_1675_pause_7"),
	Set7000ToTappedButton(),
	JmpIf7000AnyBitsSet(bits=[7], destinations=["EVENT_1675_action_queue_11"]),
	Jmp(["EVENT_1675_pause_7"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_FaceSouth(),
		A_JumpToHeight(108)
	], identifier="EVENT_1675_action_queue_11"),
	MoveScriptToMainThread(),
	Return()
])
