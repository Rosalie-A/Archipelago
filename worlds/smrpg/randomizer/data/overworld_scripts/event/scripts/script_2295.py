# E2295_ENDING_CREDITS_WEDDING_LOGIC
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
	EnterArea(room_id=R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA, face_direction=NORTHEAST, x=22, y=74, z=0),
	FreezeCamera(),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_BounceToXYWithHeight(x=18, y=55, height=0),
		A_WalkNorthwestPixels(8)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_FixedFCoordOn(),
		A_WalkNorthwestPixels(1)
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_FixedFCoordOn(),
		A_WalkSoutheastPixels(1)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_WalkSoutheastPixels(4),
		A_FaceSouthwest(),
		A_SequenceLoopingOn()
	]),
	RunEventAsSubroutine(E0795_ENDING_CREDITS_CHAPEL_SHUFFLED_NPC_ANIMATION_LOADER),
	StarMaskExpandFromScreenCenter(),
	Pause(95),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSoutheastPixels(8)
	]),
	Pause(20),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetWalkingSpeed(SLOW),
		A_WalkSoutheastPixels(8)
	]),
	Pause(20),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_FixedFCoordOff(),
		A_FaceSoutheast(),
		A_Pause(30),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_Pause(25),
		A_WalkSoutheastPixels(8)
	]),
	Pause(5),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetAllSpeeds(FAST),
		A_FaceNortheast(),
		A_FixedFCoordOn(),
		A_WalkSoutheastPixels(8),
		A_FixedFCoordOff(),
		A_WalkNortheastSteps(3),
		A_WalkNortheastSteps(1),
		A_WalkNorthwestSteps(3),
		A_WalkSouthwestSteps(4),
		A_WalkSoutheastSteps(1),
		A_WalkSoutheastPixels(8),
		A_WalkSouthwestSteps(10)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(30),
		A_FixedFCoordOff(),
		A_FaceSoutheast(),
		A_Pause(15),
		A_SetAllSpeeds(FAST),
		A_WalkSoutheastSteps(1),
		A_WalkSoutheastPixels(4),
		A_WalkNortheastSteps(2),
		A_WalkNortheastSteps(2),
		A_WalkNorthwestSteps(3),
		A_WalkSouthwestSteps(4),
		A_WalkSoutheastSteps(1),
		A_WalkSoutheastPixels(8),
		A_WalkSouthwestSteps(10)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_Pause(100),
		A_Pause(60),
		A_SequenceLoopingOff()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(85),
		A_SequenceLoopingOn(),
		A_JumpToHeight(height=64, silent=True),
		A_Pause(60),
		A_FaceSoutheast(),
		A_Pause(65),
		A_SetAllSpeeds(FAST),
		A_WalkSoutheastSteps(4),
		A_WalkSouthwestSteps(7)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Pause(85),
		A_SequenceLoopingOn(),
		A_JumpToHeight(height=64, silent=True),
		A_Pause(60),
		A_FaceSoutheast(),
		A_Pause(65),
		A_SetAllSpeeds(FAST),
		A_WalkSoutheastSteps(2),
		A_WalkSouthwestSteps(7)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Pause(85),
		A_SequenceLoopingOn(),
		A_JumpToHeight(height=64, silent=True),
		A_Pause(60),
		A_FaceNorthwest(),
		A_Pause(65),
		A_SetAllSpeeds(FAST),
		A_WalkNorthwestSteps(2),
		A_WalkSouthwestSteps(7)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(85),
		A_SequenceLoopingOn(),
		A_JumpToHeight(height=64, silent=True),
		A_Pause(60),
		A_FaceNorthwest(),
		A_Pause(65),
		A_SetAllSpeeds(FAST),
		A_WalkNorthwestSteps(4),
		A_WalkSouthwestSteps(7)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_VisibilityOff(),
		A_Pause(85),
		A_Pause(60),
		A_FaceNorthwest(),
		A_Pause(65),
		A_Pause(60),
		A_VisibilityOn(),
		A_SetAllSpeeds(FAST),
		A_WalkSoutheastSteps(4),
		A_WalkSouthwestSteps(7)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_VisibilityOff(),
		A_Pause(85),
		A_SequenceLoopingOn(),
		A_Pause(60),
		A_FaceNorthwest(),
		A_Pause(65),
		A_Pause(60),
		A_VisibilityOn(),
		A_SetAllSpeeds(FAST),
		A_WalkSoutheastSteps(2),
		A_WalkSouthwestSteps(7)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_Pause(85),
		A_SequenceLoopingOn(),
		A_JumpToHeight(height=64, silent=True),
		A_Pause(60),
		A_FaceNorthwest(),
		A_Pause(65),
		A_Pause(60),
		A_SetAllSpeeds(FAST),
		A_WalkNorthwestSteps(2),
		A_WalkSouthwestSteps(7)
	]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_Pause(85),
		A_SequenceLoopingOn(),
		A_JumpToHeight(height=64, silent=True),
		A_Pause(60),
		A_FaceNorthwest(),
		A_Pause(65),
		A_Pause(60),
		A_SetAllSpeeds(FAST),
		A_WalkNorthwestSteps(4),
		A_WalkSouthwestSteps(7)
	]),
	Pause(15),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True, identifier="wedding_ending_shift"),
		A_Pause(45)
	], identifier="wedding_ending_aq"),
	StarMaskShrinkToScreenCenter(),
	Pause(60),
	JmpToEvent(E3802_ENDING_CREDITS_YELLOW_STAR),
	Return()
])
