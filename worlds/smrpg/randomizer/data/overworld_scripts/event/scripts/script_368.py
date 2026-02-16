# E0368_MUSHROOM_KINGDOM_OCCUPIED_THRONE_ROOM_LOADER
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
	Set0158Bit7Offset(0x015C),
	Set0158Bit7Offset(0x015E),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShadowOn(),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthPixels(6),
		A_WalkNorthwestPixels(2)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetPriority(2)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetPriority(2)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_VisibilityOff()
	]),
	FreezeCamera(),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_BounceToXYWithHeight(x=10, y=19, height=6),
		A_TransferXYZFPixels(x=0, y=252, z=0, direction=EAST)
	]),
	RunEventAsSubroutine(E0761_MUSHROOM_KINGDOM_OCCUPIED_THRONE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	SetBit(TEMP_7043_5),
	Pause(30),
	ClearBit(TEMP_7043_5),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_SetSolidityBits(bit_4=True)
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetSolidityBits(bit_4=True)
	]),
	SetBit(TEMP_7043_6),
	SetSyncActionScript(NPC_4, A0101_MK_THRONE_HENCHMAN_BOUNCE),
	SetSyncActionScript(NPC_5, A0102_MK_THRONE_HENCHMAN_BOUNCE),
	SetSyncActionScript(NPC_8, A0101_MK_THRONE_HENCHMAN_BOUNCE),
	SetSyncActionScript(NPC_9, A0102_MK_THRONE_HENCHMAN_BOUNCE),
	SetSyncActionScript(NPC_6, A0101_MK_THRONE_HENCHMAN_BOUNCE),
	SetSyncActionScript(NPC_7, A0102_MK_THRONE_HENCHMAN_BOUNCE),
	Pause(60),
	SetBit(TEMP_7049_2),
	RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
	UnfreezeCamera(),
	Return()
])
