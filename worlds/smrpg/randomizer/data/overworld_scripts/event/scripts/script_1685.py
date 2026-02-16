# E1685_TEMPLE_FORTUNE_HEAD_1
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
	JmpIfBitClear(BELOME_FORTUNE_1, ["EVENT_1685_ret_45"]),
	Set7000ToTappedButton(),
	JmpIf7000AllBitsClear(bits=[7], destinations=["EVENT_1685_ret_45"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_JumpToHeight(64)
	]),
	JmpIfBitSet(BELOME_HEAD_1, ["EVENT_1685_ret_45"]),
	Pause(1, identifier="EVENT_1685_pause_5"),
	JmpIfMarioInAir(["EVENT_1685_pause_5"]),
	PlaySound(sound=SO154_BIG_SQUISH, channel=6),
	Pause(2),
	Store02To0248(),
	ApplyTileModToLevel(use_alternate=True, room_id=R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM, mod_id=32),
	Store00To0248(),
	Pause(1),
	SetBit(BELOME_HEAD_1),
	JmpIfVarNotEqualsConst(SECONDARY_TEMP_7024, 0, ["EVENT_1685_jmp_if_var_not_equals_const_20"]),
	SetVarToConst(SECONDARY_TEMP_7024, 1),
	CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
	AddConstToVar(PRIMARY_TEMP_7000, 16),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AC),
	Jmp(["EVENT_1685_copy_var_to_var_39"]),
	JmpIfVarNotEqualsConst(TEMP_7026, 0, ["EVENT_1685_copy_var_to_var_26"], identifier="EVENT_1685_jmp_if_var_not_equals_const_20"),
	SetVarToConst(TEMP_7026, 4),
	CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
	AddConstToVar(PRIMARY_TEMP_7000, 16),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AC),
	Jmp(["EVENT_1685_copy_var_to_var_39"]),
	CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000, identifier="EVENT_1685_copy_var_to_var_26"),
	AddConstToVar(PRIMARY_TEMP_7000, 16),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AC),
	SetVarToConst(TEMP_70AB, 24, identifier="EVENT_1685_set_var_to_const_29"),
	RunEventAsSubroutine(E1739_REFOCUS_CAMERA),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_FixedFCoordOff(),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_FixedFCoordOn(),
		A_WalkSouthPixels(4),
		A_FloatingOn(),
		A_JumpToHeight(0),
		A_Pause(1, identifier="EVENT_1685_action_queue_31_SUBSCRIPT_pause_8"),
		A_JmpIfObjectInAir(NPC_0, ["EVENT_1685_action_queue_31_SUBSCRIPT_pause_8"]),
		A_PlaySound(sound=SO109_BIG_SHELL_HIT, channel=4),
		A_WalkNorthPixels(8)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_FixedFCoordOff(),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_FixedFCoordOn(),
		A_WalkSouthPixels(4),
		A_FloatingOn(),
		A_JumpToHeight(0),
		A_Pause(1, identifier="EVENT_1685_action_queue_32_SUBSCRIPT_pause_8"),
		A_JmpIfObjectInAir(NPC_1, ["EVENT_1685_action_queue_32_SUBSCRIPT_pause_8"]),
		A_PlaySound(sound=SO109_BIG_SHELL_HIT, channel=4),
		A_WalkNorthPixels(8)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_IncPaletteRowBy(1),
		A_VisibilityOn(),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_FloatingOn(),
		A_JumpToHeight(0)
	]),
	SetVarToConst(TEMP_70AB, 0),
	RunEventAsSubroutine(E1739_REFOCUS_CAMERA),
	SetBit(UNKNOWN_BELOME_TEMPLE),
	SetBit(UNKNOWN_BELOME_FORTUNE),
	ClearBit(HAS_A_PRIZE_FORTUNE),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000, identifier="EVENT_1685_copy_var_to_var_39"),
	AddVarTo7000(TEMP_7026),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7028),
	CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
	Mem7000OrVar(TEMP_7028),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AC),
	Return(identifier="EVENT_1685_ret_45")
])
