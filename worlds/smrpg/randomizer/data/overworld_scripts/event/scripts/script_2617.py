# E2617_FACTORY_2ND_ROOM_LOADER
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
	JmpIfBitSet(INNER_FACTORY_ROOM_2_COMPLETED, ["EVENT_2617_run_event_as_subroutine_5"]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_SetPriority(3),
		A_WalkNorthwestPixels(8),
		A_WalkNortheastPixels(8),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_SetPriority(3),
		A_WalkNorthwestPixels(8),
		A_WalkNortheastPixels(4),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_14, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_SetPriority(3),
		A_WalkNorthwestPixels(8),
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=NPC_15, subscript=[
		A_SetPriority(3)
	]),
	RunEventAsSubroutine(E0856_INNER_FACTORY_2ND_ROOM_SHUFFLED_NPC_ANIMATION_LOADER, identifier="EVENT_2617_run_event_as_subroutine_5"),
	FadeInFromBlack(sync=False),
	Return()
])
