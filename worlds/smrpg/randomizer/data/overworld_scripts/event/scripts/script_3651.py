# E3651_NIMBUS_NORTHEAST_HOUSE_CROCO
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
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_PlaySound(sound=SO030_SURPRISED_MONSTER, channel=4),
		A_StartLoopNTimes(2),
		A_ShiftZUpPixels(8),
		A_ShiftZDownPixels(8),
		A_EndLoop()
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_FaceSoutheast(),
		A_SetSequenceSpeed(FAST),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetWalkingSpeed(SLOW),
		A_AddZCoord1Step(),
		A_SetAllSpeeds(VERY_FAST),
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
		A_DecZCoord1Step(),
		A_WalkSoutheastSteps(6)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_TransferToXYZF(x=17, y=54, z=1, direction=EAST),
		A_JumpToHeight(height=108, silent=True),
		A_WalkNorthwestSteps(2),
		A_WalkNorthwestPixels(6)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSoutheastPixels(2),
		A_StartLoopNTimes(3),
		A_WalkNorthwestPixels(4),
		A_WalkSoutheastPixels(4),
		A_EndLoop(),
		A_WalkNorthwestPixels(2)
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(32),
		A_ResetProperties(),
		A_SetSequenceSpeed(VERY_FAST),
		A_Walk1StepSouthwest(),
		A_WalkSoutheastSteps(2),
		A_VisibilityOff()
	]),
	RemoveObjectFromCurrentLevel(NPC_4),
	RemoveObjectFromSpecificLevel(NPC_4, R345_NIMBUS_LAND_TOPRIGHT_HOUSE_CROCO_DROPS_SIGNAL_RING),
	SetBit(NIMBUS_HOUSE_ITEM_SUMMONED),
	Return()
])
