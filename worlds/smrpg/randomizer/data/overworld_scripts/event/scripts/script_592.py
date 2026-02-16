# E0592_MINES_BOSS_ROOM_LOADER_BEFORE_DEFEAT
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
	JmpIfBitSet(POST_MINES_LEVEL_MODS_COMPLETED, ["EVENT_257_fade_in_from_black_async_0"]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetPriority(2)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetPriority(2)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetPriority(2)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetPriority(3),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetPriority(3),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetPriority(3),
		A_VisibilityOff()
	]),
	JmpIfBitSet(MINES_BOSS_2_DEFEATED, ["EVENT_257_fade_in_from_black_async_0"]),
	RunBackgroundEvent(event_id=E0596_MINES_BOSS_ROOM_BACKGROUND_EXPLOSIONS, return_on_level_exit=True),
	FadeInFromBlack(sync=False),
	RunEventAsSubroutine(E0788_MINES_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
	Return()
])
