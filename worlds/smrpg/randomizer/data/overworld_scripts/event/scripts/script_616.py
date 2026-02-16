# E0616_MARRYMORE_INN_LOBBY_EXIT
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
	JmpIfBitSet(TEMP_7042_0, ["EVENT_616_jmp_if_bit_set_8"]),
	JmpIfBitSet(TEMP_704C_0, ["EVENT_256_ret_0"], identifier="EVENT_616_jmp_if_bit_set_1"),
	JmpIfBitSet(GUEST_DROPPED_OFF, ["EVENT_256_ret_0"]),
	JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_616_enter_area_6"]),
	EnterArea(room_id=R005_MARRYMORE_OUTSIDE_DURING_BOOSTER, face_direction=SOUTHEAST, x=5, y=73, z=4, run_entrance_event=True),
	Return(),
	EnterArea(room_id=R064_MARRYMORE_OUTSIDE, face_direction=SOUTHEAST, x=5, y=73, z=4, run_entrance_event=True, identifier="EVENT_616_enter_area_6"),
	Return(),
	JmpIfBitSet(TEMP_7042_5, ["EVENT_616_jmp_if_bit_set_1"], identifier="EVENT_616_jmp_if_bit_set_8"),
	JmpIfBitSet(TEMP_7042_6, ["EVENT_616_jmp_if_bit_set_1"]),
	RunDialog(dialog_id=DI0997_CAPS_LOCK_HONORIFIC, above_object=NPC_12, closable=False, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_JumpToHeight(height=64, silent=True),
		A_Pause(1, identifier="EVENT_616_action_queue_11_SUBSCRIPT_pause_2"),
		A_JmpIfMarioInAir(["EVENT_616_action_queue_11_SUBSCRIPT_pause_2"]),
		A_Pause(30),
		A_ResetProperties(),
		A_WalkToXYCoords(x=6, y=62),
		A_FaceNorthwest()
	]),
	RunDialog(dialog_id=DI0968_DUPLICATE, above_object=NPC_12, closable=False, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_616_set_action_script_18"]),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Pause(10),
	RunDialog(dialog_id=DI0974_ENJOY_YOUR_STAY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Return(),
	SetSyncActionScript(MARIO, A0670_NOD_YES, identifier="EVENT_616_set_action_script_18"),
	Pause(10),
	RunDialog(dialog_id=DI0996_DROP_BY_AGAIN, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(10),
	UnsyncDialog(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Walk1StepSoutheast()
	]),
	Jmp(["EVENT_616_jmp_if_bit_set_1"])
])
