# E2278_BALCONY_LOADER_AFTER_NIMBUS_CASTLE
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
	ActionQueueSync(target=MARIO, subscript=[
		A_TransferToXYZF(x=7, y=14, z=0, direction=EAST),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetPriority(3),
		A_TransferToXYZF(x=4, y=23, z=0, direction=EAST),
		A_VisibilityOn(),
		A_WalkSouthwestPixels(8),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetPriority(3),
		A_TransferToXYZF(x=5, y=22, z=0, direction=EAST),
		A_VisibilityOn(),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetPriority(3),
		A_TransferToXYZF(x=5, y=21, z=0, direction=EAST),
		A_VisibilityOn(),
		A_WalkNortheastPixels(8),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetPriority(3),
		A_TransferToXYZF(x=5, y=17, z=0, direction=EAST),
		A_VisibilityOn(),
		A_FaceSouthwest(),
		A_ResetProperties()
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_ShiftToXYCoords(x=4, y=20),
		A_FaceSoutheast(),
		A_SequenceLoopingOn(),
		A_VisibilityOn()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceSoutheast(),
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FaceSoutheast(),
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FaceSoutheast(),
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=4, y=16, z=0, direction=EAST),
		A_FaceNorthwest(),
		A_ResetProperties()
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_TransferToXYZF(x=3, y=17, z=0, direction=EAST),
		A_FaceNorthwest(),
		A_ResetProperties(),
		A_SequenceLoopingOff()
	]),
	RunEventAsSubroutine(E0794_TOWER_BALCONY_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	JmpToEvent(E1927_TOWER_BALCONY_JUMP_OFF)
])
