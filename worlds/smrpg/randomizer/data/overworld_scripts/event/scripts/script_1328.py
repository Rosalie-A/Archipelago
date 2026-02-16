# E1328_TOWER_EXTERIOR_LOADER
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
	RunEventAsSubroutine(E1605_TOWER_EXTERIOR_CANCEL_EXP_STAR),
	PlayMusicAtDefaultVolume(M0013_ROADISFULLOFDANGERS),
	RunEventAsSubroutine(E0878_TOWER_EXTERIOR_SHUFFLED_NPC_ANIMATION_LOADER),
	JmpIfBitSet(TOWER_OPENED, ["EVENT_1328_remove_from_current_level_7"]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_WalkSoutheastPixels(2),
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetPriority(0),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_WalkNortheastPixels(8)
	]),
	Jmp(["EVENT_1328_fade_in_from_black_async_11"]),
	RemoveObjectFromCurrentLevel(NPC_1, identifier="EVENT_1328_remove_from_current_level_7"),
	RemoveObjectFromCurrentLevel(NPC_2),
	ApplySolidityModToLevel(permanent=True, room_id=R202_BOOSTER_TOWER_ENTRANCE, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R202_BOOSTER_TOWER_ENTRANCE, mod_id=32),
	FadeInFromBlack(sync=False, identifier="EVENT_1328_fade_in_from_black_async_11"),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_1328_jmp_if_bit_clear_16"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1328_jmp_if_bit_clear_16"]),
	RunEventAsSubroutine(E3899_BOOSTER_TOWER_STAR_PIECE_SIGNAL),
	JmpIfBitClear(STAR_PIECE_GRANT_DIRECTIONAL_BIT, ["EVENT_1328_ret_18"], identifier="EVENT_1328_jmp_if_bit_clear_16"),
	RunEventAsSubroutine(E1203_TOWER_BALCONY_BOSS_UNLOCKS),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
	Return(identifier="EVENT_1328_ret_18")
])
