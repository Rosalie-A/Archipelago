# E3730_NIMBUS_CASTLE_OCCUPIED_4_PATH_ROOM_LOADER
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
	RemoveObjectFromSpecificLevel(NPC_13, R416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA),
	RemoveObjectFromSpecificLevel(NPC_14, R416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA),
	JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_3730_run_event_as_subroutine_14"]),
	JmpIfBitSet(UNKNOWN_STATUE_ROOM_7090_1, ["EVENT_3730_run_event_as_subroutine_14"]),
	JmpIfBitSet(STATUE_GAME_DONE, ["EVENT_3730_palette_set_6"]),
	Jmp(["EVENT_3730_run_event_as_subroutine_14"]),
	PaletteSet(palette_set=84, row=1, bit_0=True, bit_1=True, bit_2=True, bit_3=True, identifier="EVENT_3730_palette_set_6"),
	PauseActionScript(NPC_4),
	PauseActionScript(NPC_5),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromSpecificLevel(NPC_1, R115_NIMBUS_CASTLE_AREA_03_4WAY_PATH_DURING_VALENTINA),
	ActionQueueSync(target=NPC_4, subscript=[
		A_TransferToXYZF(x=25, y=21, z=3, direction=EAST),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_TransferToXYZF(x=26, y=22, z=3, direction=EAST),
		A_VisibilityOff()
	]),
	RememberLastObject(),
	RunEventAsSubroutine(E0824_NIMBUS_CASTLE_OCCUPIED_4WAY_PATH_SHUFFLED_NPC_ANIMATION_LOADER, identifier="EVENT_3730_run_event_as_subroutine_14"),
	FadeInFromBlack(sync=False),
	Return()
])
