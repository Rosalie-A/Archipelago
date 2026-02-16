# E2317_GARDENER_CLOUD_LOADER
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
	FreezeCamera(),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkToXYCoords(x=0, y=76),
		A_WalkNorthPixels(8),
		A_WalkEastPixels(17)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_ShiftToXYCoords(x=4, y=111),
		A_OverwriteSolidity(),
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZDownSteps(8),
		A_SetSpriteSequence(index=7, sprite_offset=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetPriority(2),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_WalkWestPixels(5),
		A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True)
	]),
	SetBit(TEMP_GARDENER_EXTERIOR_1),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_UnknownCommand(bytearray(b' \x01')),
		A_UnknownCommand(bytearray(b'$\x1c\x00\x00\x00')),
		A_ShiftZUpSteps(6),
		A_BPL262728(),
		A_SetSpriteSequence(index=14, sprite_offset=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(16),
		A_SetSpriteSequence(index=4, sprite_offset=1, is_sequence=True, looping=True),
		A_FaceNorthwest(),
		A_JumpToHeight(160),
		A_WalkNorthwestSteps(2),
		A_OverwriteSolidity(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkNorthwestPixels(8)
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	UnfreezeCamera(),
	Return()
])
