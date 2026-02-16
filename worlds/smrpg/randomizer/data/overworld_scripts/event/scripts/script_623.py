# E0623_MARRYMORE_INN_EMPLOYED_GUEST_LEAVES
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
	JmpIfRandom1of2(["EVENT_623_pause_2"]),
	Pause(90),
	Pause(60, identifier="EVENT_623_pause_2"),
	CopyVarToVar(from_var=TEMP_70B8, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_623_set_action_script_8"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_623_set_action_script_12"]),
	SetSyncActionScript(NPC_7, A0327_MARRYMORE_ELDERLY_GUEST_LEAVES),
	Jmp(["EVENT_623_pause_13"]),
	SetSyncActionScript(NPC_8, A0328_EMPTY, identifier="EVENT_623_set_action_script_8"),
	Pause(16),
	SetSyncActionScript(NPC_9, A0329_EMPTY),
	Jmp(["EVENT_623_pause_13"]),
	SetSyncActionScript(NPC_6, A0327_MARRYMORE_ELDERLY_GUEST_LEAVES, identifier="EVENT_623_set_action_script_12"),
	Pause(1, identifier="EVENT_623_pause_13"),
	JmpIfBitSet(TEMP_7044_3, ["EVENT_623_set_7000_to_object_coord_16"]),
	Jmp(["EVENT_623_pause_13"]),
	Set7000ToObjectCoord(target_npc=NPC_5, coord=COORD_Y, pixel=True, bit_7=True, identifier="EVENT_623_set_7000_to_object_coord_16"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 63, ["EVENT_623_unsync_action_script_19"]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_Walk1StepNortheast(),
		A_FaceNorthwest()
	]),
	UnsyncActionScript(NPC_9, identifier="EVENT_623_unsync_action_script_19"),
	UnsyncActionScript(NPC_8),
	UnsyncActionScript(NPC_6),
	UnsyncActionScript(NPC_7),
	ClearBit(GUEST_DROPPED_OFF),
	Return()
])
