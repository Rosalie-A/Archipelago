# E3184_MINES_FIRST_ROOM_LOADER
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
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 54),
	JmpIfBitSet(TEMP_7042_0, ["EVENT_3184_set_bit_3"]),
	JmpToSubroutine(["EVENT_3183_jmp_if_bit_set_4"]),
	SetBit(TEMP_7042_0, identifier="EVENT_3184_set_bit_3"),
	JmpIfBitSet(MINES_BOSS_2_DEFEATED, ["EVENT_3184_remove_from_current_level_10"]),
	PlayMusicAtDefaultVolume(M0027_DUNGEONISFULLOFMONSTERS),
	JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["EVENT_3184_remove_from_current_level_10"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[1]),
		A_WalkToXYCoords(x=19, y=27),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[1]),
		A_WalkToXYCoords(x=19, y=26),
		A_FaceNortheast()
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	RemoveObjectFromCurrentLevel(NPC_0, identifier="EVENT_3184_remove_from_current_level_10"),
	RemoveObjectFromCurrentLevel(NPC_1),
	DisableObjectTrigger(NPC_0),
	DisableObjectTrigger(NPC_1),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER)
])
