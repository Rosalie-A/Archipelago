# E0613_MARRYMORE_SUITE_LOADER
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
	ActionQueueAsync(target=NPC_3, subscript=[
		A_TransferXYZFPixels(x=0, y=248, z=0, direction=EAST),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	JmpIfBitSet(BELLHOP_CALLED, ["EVENT_613_action_queue_27"]),
	JmpIfBitSet(TEMP_7042_4, ["EVENT_257_fade_in_from_black_async_0"]),
	JmpIfBitSet(TEMP_7042_3, ["EVENT_613_action_queue_6"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=4, y=19, z=0, direction=EAST)
	]),
	Jmp(["EVENT_613_jmp_if_bit_set_7"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=4, y=20, z=0, direction=EAST),
		A_FaceSouthwest()
	], identifier="EVENT_613_action_queue_6"),
	JmpIfBitSet(TEMP_7042_3, ["EVENT_257_fade_in_from_black_async_0"], identifier="EVENT_613_jmp_if_bit_set_7"),
	SetSyncActionScript(NPC_0, A0320_BELLHOP_SET_POSITION),
	FadeInFromBlack(sync=False),
	UnsyncActionScript(NPC_0),
	CopyVarToVar(from_var=MARRYMORE_SUITE_LEGAL_COUNT, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_613_set_action_script_15"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestSteps(2),
		A_SetSequenceSpeed(SLOW)
	]),
	Jmp(["EVENT_613_set_action_script_23"]),
	SetAsyncActionScript(MARIO, A0670_NOD_YES, identifier="EVENT_613_set_action_script_15"),
	Pause(10),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(FAST),
		A_WalkSouthwestSteps(1),
		A_WalkNorthwestSteps(3),
		A_SetSequenceSpeed(SLOW),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(60),
		A_FaceNorth()
	]),
	RememberLastObject(),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(48),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(FAST),
		A_WalkSoutheastSteps(3),
		A_WalkSouthwestSteps(1),
		A_SetSequenceSpeed(SLOW)
	]),
	Pause(10),
	SetSyncActionScript(NPC_0, A0321_BELLHOP_FACE_PLAYER, identifier="EVENT_613_set_action_script_23"),
	SetBit(BELLHOP_UNKNOWN),
	SetBit(TEMP_7042_3),
	Return(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=5, y=21, z=0, direction=EAST)
	], identifier="EVENT_613_action_queue_27"),
	SetSyncActionScript(NPC_0, A0978_RANDOMLY_FACE_SOUTHWEST),
	FadeInFromBlack(sync=False),
	Return()
])
