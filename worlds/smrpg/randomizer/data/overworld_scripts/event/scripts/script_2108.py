# E2108_NIMBUS_CASTLE_STATUE_POLISHER_BOSS_FIGHT_ROOM_LOADER
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
	ActionQueueAsync(target=NPC_2, subscript=[
		A_WalkSouthPixels(7)
	]),
	PaletteSet(palette_set=84, row=1, bit_0=True, bit_1=True, bit_2=True, bit_3=True),
	JmpIfBitClear(STATUE_KEEPER_FIGHT_PRESENT, ["EVENT_2108_jmp_if_bit_set_4"]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_WalkNortheastPixels(8),
		A_FaceSoutheast(),
		A_VisibilityOn()
	]),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_2108_jmp_to_subroutine_8"], identifier="EVENT_2108_jmp_if_bit_set_4"),
	RunEventAsSubroutine(E0818_NIMBUS_CASTLE_STATUE_POLISHER_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	Return(),
	JmpToSubroutine(["EVENT_2108_jmp_if_bit_set_15"], identifier="EVENT_2108_jmp_to_subroutine_8"),
	RunEventAsSubroutine(E0818_NIMBUS_CASTLE_STATUE_POLISHER_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
	RunEventAsSubroutine(E0081_MARIO_LANDS_SUBROUTINE),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2108_ret_14"]),
	RunEventAsSubroutine(E3912_NIMBUS_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_2108_ret_14"),
	JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_2108_play_music_default_volume_18"], identifier="EVENT_2108_jmp_if_bit_set_15"),
	PlayMusicAtDefaultVolume(M0061_VALENTINA),
	Return(),
	PlayMusicAtDefaultVolume(M0050_NIMBUSLAND, identifier="EVENT_2108_play_music_default_volume_18"),
	Return()
])
