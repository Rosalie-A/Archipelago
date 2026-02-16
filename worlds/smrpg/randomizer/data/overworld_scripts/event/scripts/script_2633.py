# E2633_CASINO_INTERIOR_LOADER
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
	JmpIfBitClear(CASINO_WARP_ENABLED, ["EVENT_2633_set_bit_2"]),
	RunEventAsSubroutine(E2645_CASINO_SUBROUTINE),
	SetBit(DIRECTIONAL_7046_1, identifier="EVENT_2633_set_bit_2"),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkWestPixels(5)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthPixels(8),
		A_SetSpriteSequence(index=10, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkWestPixels(16),
		A_SetSpriteSequence(index=10, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthwestPixels(3)
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthwestPixels(8),
		A_WalkSouthwestPixels(3)
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_VisibilityOn()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_VisibilityOff()
	]),
	FadeInFromBlack(sync=False),
	JmpIfBitClear(STAR_PIECE_GRANT_DIRECTIONAL_BIT, ["EVENT_2633_ret_16"]),
	SetVarToConst(PRIMARY_TEMP_7000, 523),
	JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE),
	Return(identifier="EVENT_2633_ret_16")
])
