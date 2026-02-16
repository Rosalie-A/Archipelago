# E1282_TOWER_BALCONY_LOADER_AFTER_MARRYMORE
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
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetPriority(3),
		A_WalkNortheastPixels(10),
		A_WalkNorthPixels(2),
		A_WalkWestPixels(2),
		A_FaceSouthwest()
	]),
	JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_1282_jmp_to_event_10"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetPriority(3),
		A_TransferToXYZF(x=5, y=16, z=0, direction=EAST),
		A_VisibilityOn(),
		A_FaceSouthwest(),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetPriority(3),
		A_TransferToXYZF(x=6, y=18, z=0, direction=EAST),
		A_VisibilityOn(),
		A_FaceSouthwest(),
		A_SequenceLoopingOn()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetPriority(3),
		A_TransferToXYZF(x=7, y=20, z=0, direction=EAST),
		A_VisibilityOn(),
		A_FaceSouthwest(),
		A_SequenceLoopingOn()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetPriority(3),
		A_TransferToXYZF(x=4, y=21, z=0, direction=EAST),
		A_VisibilityOn(),
		A_FaceSouthwest(),
		A_SetSpriteSequence(index=6, is_mold=True, looping=True, identifier="chapel_stare_up_4"),
	], identifier="chapel_stare_up_queue_4"),
	RunEventAsSubroutine(E0794_TOWER_BALCONY_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	JmpToEvent(E1927_TOWER_BALCONY_JUMP_OFF),
	JmpToEvent(E2278_BALCONY_LOADER_AFTER_NIMBUS_CASTLE, identifier="EVENT_1282_jmp_to_event_10"),
	Return()
])
