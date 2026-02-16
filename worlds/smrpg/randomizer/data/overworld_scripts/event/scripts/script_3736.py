# E3736_NIMBUS_CASTLE_FINAL_HALLWAY_LOADER
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
	JmpIfObjectNotInSpecificLevel(NPC_0, R437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD, ["EVENT_3736_fade_in_from_black_async_4"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferXYZFPixels(x=252, y=252, z=0, direction=EAST),
		A_FaceNortheast(),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True)
	]),
	RunBackgroundEvent(event_id=E3735_NIMBUS_CASTLE_FINAL_HALLWAY_APPLY_MOD, return_on_level_exit=True),
	RunEventAsSubroutine(E0820_NIMBUS_CASTLE_FINAL_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False, identifier="EVENT_3736_fade_in_from_black_async_4"),
	JmpIfBitClear(TEMP_7076_0, ["EVENT_3584_ret_0"]),
	JmpIfBitSet(EXP_STAR_BIT_5, ["EVENT_3584_ret_0"]),
	SetVarToConst(TIMER_7022, 70),
	ClearBit(EXP_STAR_BIT_6),
	CreatePacketAtObjectCoords(packet=P022_RECURSIVE_SPARKLES, target_npc=MARIO, destinations=["EVENT_3584_ret_0"]),
	Return()
])
