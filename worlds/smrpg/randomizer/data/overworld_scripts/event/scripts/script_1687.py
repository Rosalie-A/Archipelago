# E1687_TEMPLE_FORTUNE_HEAD_3
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
	JmpIfBitClear(BELOME_FORTUNE_1, ["EVENT_1687_ret_30"]),
	Set7000ToTappedButton(),
	JmpIf7000AllBitsClear(bits=[7], destinations=["EVENT_1687_ret_30"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_JumpToHeight(64)
	]),
	JmpIfBitSet(BELOME_HEAD_3, ["EVENT_1687_ret_30"]),
	Pause(1, identifier="EVENT_1687_pause_5"),
	JmpIfMarioInAir(["EVENT_1687_pause_5"]),
	PlaySound(sound=SO154_BIG_SQUISH, channel=6),
	Pause(2),
	Store02To0248(),
	ApplyTileModToLevel(use_alternate=True, room_id=R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM, mod_id=34),
	Store00To0248(),
	Pause(1),
	SetBit(BELOME_HEAD_3),
	JmpIfVarNotEqualsConst(SECONDARY_TEMP_7024, 0, ["EVENT_1687_jmp_if_var_not_equals_const_20"]),
	SetVarToConst(SECONDARY_TEMP_7024, 3),
	CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
	AddConstToVar(PRIMARY_TEMP_7000, 64),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AC),
	Jmp(["EVENT_1685_copy_var_to_var_39"]),
	JmpIfVarNotEqualsConst(TEMP_7026, 0, ["EVENT_1687_copy_var_to_var_26"], identifier="EVENT_1687_jmp_if_var_not_equals_const_20"),
	SetVarToConst(TEMP_7026, 12),
	CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
	AddConstToVar(PRIMARY_TEMP_7000, 64),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AC),
	Jmp(["EVENT_1685_copy_var_to_var_39"]),
	CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000, identifier="EVENT_1687_copy_var_to_var_26"),
	AddConstToVar(PRIMARY_TEMP_7000, 64),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AC),
	Jmp(["EVENT_1685_set_var_to_const_29"]),
	Return(identifier="EVENT_1687_ret_30")
])
