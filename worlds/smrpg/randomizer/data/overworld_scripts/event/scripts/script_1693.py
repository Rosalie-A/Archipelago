# E1693_TEMPLE_FINAL_FORTUNE_HEAD
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
	JmpIfBitSet(TEMP_7044_0, ["EVENT_1693_ret_21"]),
	Set7000ToTappedButton(),
	JmpIf7000AllBitsClear(bits=[7], destinations=["EVENT_1693_ret_21"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_JumpToHeight(height=64, silent=True)
	]),
	PlaySound(sound=SO154_BIG_SQUISH, channel=6),
	Pause(2),
	Store02To0248(),
	ApplyTileModToLevel(use_alternate=True, room_id=R423_BELOME_TEMPLE_AREA_06_BELOMES_FORTUNE_ROOM_WELEVATING_PLATFORM, mod_id=32),
	Store00To0248(),
	Pause(1),
    JmpIfBitSet(TEMPLE_BOSS_GATED, ["EVENT_1693_clear_bit_18"]),
	Inc(UNKNOWN_70AD),
	CopyVarToVar(from_var=UNKNOWN_70AD, to_var=PRIMARY_TEMP_7000),
	AddConstToVar(PRIMARY_TEMP_7000, 5),
	SetVarToRandom(TEMP_702A, 20),
	Compare7000ToVar(TEMP_702A),
	JmpIfComparisonResultIsLesser(["EVENT_1693_clear_bit_18"]),
	SetBit(TEMPLE_BOSS_ACCESS_FORTUNE),
	Jmp(["EVENT_1693_set_bit_19"]),
	ClearBit(TEMPLE_BOSS_ACCESS_FORTUNE, identifier="EVENT_1693_clear_bit_18"),
	SetBit(TEMP_7044_0, identifier="EVENT_1693_set_bit_19"),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_IncPaletteRowBy(1),
		A_FloatingOff(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSoutheastPixels(4),
		A_JumpToHeight(64),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_VisibilityOn(),
		A_SetWalkingSpeed(FAST),
		A_WalkSoutheastSteps(2),
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	Return(identifier="EVENT_1693_ret_21")
])
