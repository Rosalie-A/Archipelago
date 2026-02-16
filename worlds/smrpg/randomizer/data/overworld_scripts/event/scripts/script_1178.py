# E1178_SEASIDE_GRANT_SHED_ITEM
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
	Pause(1, identifier="EVENT_1178_pause_0"),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceSouthwest(),
		A_Pause(1),
		A_JumpToHeight(height=96, silent=True),
		A_Pause(1)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FaceSouthwest(),
		A_Pause(1),
		A_JumpToHeight(height=96, silent=True),
		A_Pause(1)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FaceSoutheast(),
		A_Pause(1),
		A_JumpToHeight(height=48, silent=True),
		A_Pause(1)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_FaceSouthwest(),
		A_Pause(1),
		A_JumpToHeight(height=80, silent=True),
		A_Pause(1)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_FaceSoutheast(),
		A_Pause(1),
		A_JumpToHeight(height=48, silent=True),
		A_Pause(1)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_FaceNorthwest(),
		A_Pause(1),
		A_JumpToHeight(height=85, silent=True),
		A_Pause(1)
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_FaceSoutheast(),
		A_Pause(1),
		A_JumpToHeight(height=112, silent=True),
		A_Pause(1)
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_BounceToXYWithHeight(x=4, y=19, height=0),
		A_FaceSouthwest(),
		A_SetSequenceSpeed(NORMAL)
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkSoutheastSteps(1),
		A_WalkSouthwestSteps(2),
		A_VisibilityOff()
	]),
	Pause(1),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_BounceToXYWithHeight(x=4, y=19, height=0),
		A_FaceSouthwest(),
		A_SetSequenceSpeed(NORMAL)
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkSoutheastSteps(1),
		A_WalkSouthwestSteps(2),
		A_VisibilityOff()
	]),
	Pause(1),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_BounceToXYWithHeight(x=4, y=19, height=0),
		A_FaceSouthwest(),
		A_SetSequenceSpeed(NORMAL)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkSoutheastSteps(1),
		A_WalkSouthwestSteps(2),
		A_VisibilityOff()
	]),
	Pause(1),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_BounceToXYWithHeight(x=4, y=19, height=0),
		A_FaceSouthwest(),
		A_SetSequenceSpeed(FAST)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_BounceToXYWithHeight(x=5, y=20, height=0),
		A_FaceSouthwest(),
		A_SetSequenceSpeed(FAST)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkSoutheastSteps(1),
		A_WalkSouthwestSteps(2),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkSouthwestSteps(2),
		A_VisibilityOff()
	]),
	Pause(5),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_WalkSoutheastSteps(4),
		A_WalkSouthwestSteps(1),
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_WalkSoutheastSteps(1),
		A_WalkSouthwestSteps(2),
		A_VisibilityOff()
	]),
	Pause(1),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_WalkSoutheastSteps(4),
		A_WalkSouthwestSteps(2),
		A_FaceSouthwest()
	]),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_WalkSoutheastSteps(1),
		A_WalkSouthwestSteps(2),
		A_VisibilityOff()
	]),
	SetBit(SEASIDE_SHED_EMPTIED),
	Pause(1),
	RemoveObjectFromSpecificLevel(NPC_5, R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE),
	RemoveOneOfItemFromInventory(ShedKeyItem),
	Return()
])
