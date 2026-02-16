# E2292_ENDING_CREDITS_TOADOFSKY
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
	EnterArea(room_id=R441_ENDING_CREDITS_TOADOFSKY_CONDUCTS_CHOIR, face_direction=NORTHEAST, x=3, y=17, z=0),
	FreezeCamera(),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_BounceToXYWithHeight(x=0, y=2, height=0)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_WalkNorthPixels(3)
	]),
	Set0158Bit7Offset(0x0158),
	StarMaskExpandFromScreenCenter(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(VERY_SLOW),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_WalkSouthwestPixels(8),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(15),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=False),
		A_Pause(45),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(50),
		A_SetSequenceSpeed(SLOW),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	SetSyncActionScript(NPC_2, A1015_END_CREDITS_FROGFUCIUS_RAISES),
	Pause(30),
	Clear0158Bit7Offset(0x0158),
	ActionQueueSync(target=NPC_3, subscript=[
		A_Pause(80),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(145),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_Pause(120),
		A_SetWalkingSpeed(VERY_SLOW),
		A_StartLoopNTimes(30),
		A_WalkNorthPixels(1),
		A_Pause(4),
		A_EndLoop()
	]),
	Pause(60),
	StarMaskShrinkToScreenCenter(),
	Pause(60),
	JmpToEvent(E3801_ENDING_CREDITS_RED_STAR),
	Return()
])
