# E2362_ABYSS_FOUR_BOLT_ROOM_LOADER
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
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True, bit_7=True),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 19, ["EVENT_2362_set_var_to_const_21"]),
	SetVarToConst(FACTORY_FALL_1, 222),
	SetVarToConst(FACTORY_FALL_2, 0),
	SetVarToConst(FACTORY_FALL_3, 0),
	SetVarToConst(FACTORY_FALL_4, 0),
	SetVarToConst(FACTORY_FALL_5, 0),
	SetVarToConst(FACTORY_FALL_6, 0),
	RunBackgroundEvent(event_id=E2385_ABYSS_FOUR_BOLT_ROOM_BACKGROUND, return_on_level_exit=True),
	ActionQueueSync(target=NPC_0, subscript=[
		A_WalkSouthwestPixels(4),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_WalkSouthwestPixels(10),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_WalkSouthwestPixels(4),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_WalkSouthwestPixels(10),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_WalkSouthwestPixels(4),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_WalkSouthwestPixels(10),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(7),
		A_ShiftZDownPixels(15)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(13),
		A_ShiftZDownPixels(15)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(7),
		A_ShiftZDownPixels(15)
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(13),
		A_ShiftZDownPixels(15)
	]),
	FadeInFromBlack(sync=False),
	Return(),
	SetVarToConst(FACTORY_FALL_1, 222, identifier="EVENT_2362_set_var_to_const_21"),
	SetVarToConst(FACTORY_FALL_2, 24),
	SetVarToConst(FACTORY_FALL_3, 30),
	SetVarToConst(FACTORY_FALL_4, 24),
	SetVarToConst(FACTORY_FALL_5, 16),
	SetVarToConst(FACTORY_FALL_6, 16),
	RunBackgroundEvent(event_id=E2385_ABYSS_FOUR_BOLT_ROOM_BACKGROUND, return_on_level_exit=True),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShiftToXYCoords(x=7, y=116),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=6, y=117),
		A_WalkNortheastPixels(6),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ShiftToXYCoords(x=13, y=104),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_ShiftToXYCoords(x=12, y=105),
		A_WalkNortheastPixels(6),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_ShiftToXYCoords(x=18, y=114),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_ShiftToXYCoords(x=17, y=115),
		A_WalkNortheastPixels(6),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_ShiftToXYCoords(x=11, y=118),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(2),
		A_ShiftZDownPixels(15)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_ShiftToXYCoords(x=11, y=119),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(8),
		A_ShiftZDownPixels(15)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_ShiftToXYCoords(x=17, y=107),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(5),
		A_ShiftZDownPixels(15)
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_ShiftToXYCoords(x=17, y=106),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkSoutheastPixels(2),
		A_ShiftZDownPixels(15)
	]),
	FadeInFromBlack(sync=False),
	Return(),
	SetVarToConst(FACTORY_FALL_1, 222, identifier="EVENT_2362_set_var_to_const_40"),
	SetVarToConst(FACTORY_FALL_2, 0),
	SetVarToConst(FACTORY_FALL_3, 0),
	SetVarToConst(FACTORY_FALL_4, 0),
	SetVarToConst(FACTORY_FALL_5, 0),
	SetVarToConst(FACTORY_FALL_6, 0),
	ActionQueueSync(target=NPC_0, subscript=[
		A_WalkSouthwestPixels(4),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_WalkSouthwestPixels(10),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_WalkSouthwestPixels(4),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_WalkSouthwestPixels(10),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_WalkSouthwestPixels(4),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_WalkSouthwestPixels(10),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(7),
		A_ShiftZDownPixels(15)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(13),
		A_ShiftZDownPixels(15)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(7),
		A_ShiftZDownPixels(15)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(13),
		A_ShiftZDownPixels(15)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_OverwriteSolidity(),
		A_TransferToXYZF(x=7, y=130, z=0, direction=EAST)
	]),
	FreezeCamera(),
	FadeInFromBlack(sync=False),
	SetAsyncActionScript(MARIO, A0414_PLAYER_ENTER_ANGLED_JUMPING_POSE),
	SetAsyncActionScript(MARIO, A0399_JUMPING_FALLING_STATE_IN_FACTORY),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	RunBackgroundEvent(event_id=E2385_ABYSS_FOUR_BOLT_ROOM_BACKGROUND, return_on_level_exit=True),
	UnfreezeCamera(),
	ClearBit(DIRECTIONAL_7045_7),
	Return(),
	SetVarToConst(FACTORY_FALL_1, 222, identifier="EVENT_2362_set_var_to_const_66"),
	SetVarToConst(FACTORY_FALL_2, 0),
	SetVarToConst(FACTORY_FALL_3, 30),
	SetVarToConst(FACTORY_FALL_4, 0),
	SetVarToConst(FACTORY_FALL_5, 0),
	SetVarToConst(FACTORY_FALL_6, 0),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShiftToXYCoords(x=7, y=116),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=6, y=117),
		A_WalkNortheastPixels(6),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_WalkSouthwestPixels(4),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_WalkSouthwestPixels(10),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_WalkSouthwestPixels(4),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_WalkSouthwestPixels(10),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(7),
		A_ShiftZDownPixels(15)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(13),
		A_ShiftZDownPixels(15)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(7),
		A_ShiftZDownPixels(15)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(13),
		A_ShiftZDownPixels(15)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_OverwriteSolidity(),
		A_TransferToXYZF(x=12, y=118, z=0, direction=EAST)
	]),
	FreezeCamera(),
	FadeInFromBlack(sync=False),
	SetAsyncActionScript(MARIO, A0414_PLAYER_ENTER_ANGLED_JUMPING_POSE),
	SetAsyncActionScript(MARIO, A0399_JUMPING_FALLING_STATE_IN_FACTORY),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	RunBackgroundEvent(event_id=E2385_ABYSS_FOUR_BOLT_ROOM_BACKGROUND, return_on_level_exit=True),
	UnfreezeCamera(),
	ClearBit(DIRECTIONAL_7045_7),
	Return(),
	SetVarToConst(FACTORY_FALL_1, 222, identifier="EVENT_2362_set_var_to_const_92"),
	SetVarToConst(FACTORY_FALL_2, 0),
	SetVarToConst(FACTORY_FALL_3, 30),
	SetVarToConst(FACTORY_FALL_4, 0),
	SetVarToConst(FACTORY_FALL_5, 16),
	SetVarToConst(FACTORY_FALL_6, 0),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShiftToXYCoords(x=7, y=116),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=6, y=117),
		A_WalkNortheastPixels(6),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_WalkSouthwestPixels(4),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_WalkSouthwestPixels(10),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_WalkSouthwestPixels(4),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_WalkSouthwestPixels(10),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_ShiftToXYCoords(x=11, y=118),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(2),
		A_ShiftZDownPixels(15)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_ShiftToXYCoords(x=11, y=119),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(8),
		A_ShiftZDownPixels(15)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(7),
		A_ShiftZDownPixels(15)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(13),
		A_ShiftZDownPixels(15)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_OverwriteSolidity(),
		A_TransferToXYZF(x=16, y=127, z=0, direction=EAST)
	]),
	FreezeCamera(),
	FadeInFromBlack(sync=False),
	SetAsyncActionScript(MARIO, A0414_PLAYER_ENTER_ANGLED_JUMPING_POSE),
	SetAsyncActionScript(MARIO, A0399_JUMPING_FALLING_STATE_IN_FACTORY),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	RunBackgroundEvent(event_id=E2385_ABYSS_FOUR_BOLT_ROOM_BACKGROUND, return_on_level_exit=True),
	UnfreezeCamera(),
	ClearBit(DIRECTIONAL_7045_7),
	Return(),
	SetVarToConst(FACTORY_FALL_1, 222, identifier="EVENT_2362_set_var_to_const_118"),
	SetVarToConst(FACTORY_FALL_2, 24),
	SetVarToConst(FACTORY_FALL_3, 30),
	SetVarToConst(FACTORY_FALL_4, 0),
	SetVarToConst(FACTORY_FALL_5, 0),
	SetVarToConst(FACTORY_FALL_6, 0),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShiftToXYCoords(x=7, y=116),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=6, y=117),
		A_WalkNortheastPixels(6),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ShiftToXYCoords(x=13, y=104),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_ShiftToXYCoords(x=12, y=105),
		A_WalkNortheastPixels(6),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_WalkSouthwestPixels(4),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_WalkSouthwestPixels(10),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(7),
		A_ShiftZDownPixels(15)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(13),
		A_ShiftZDownPixels(15)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(7),
		A_ShiftZDownPixels(15)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(13),
		A_ShiftZDownPixels(15)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_OverwriteSolidity(),
		A_TransferToXYZF(x=18, y=106, z=0, direction=EAST)
	]),
	FreezeCamera(),
	FadeInFromBlack(sync=False),
	SetAsyncActionScript(MARIO, A0414_PLAYER_ENTER_ANGLED_JUMPING_POSE),
	SetAsyncActionScript(MARIO, A0399_JUMPING_FALLING_STATE_IN_FACTORY),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	RunBackgroundEvent(event_id=E2385_ABYSS_FOUR_BOLT_ROOM_BACKGROUND, return_on_level_exit=True),
	UnfreezeCamera(),
	ClearBit(DIRECTIONAL_7045_7),
	Return(),
	SetVarToConst(FACTORY_FALL_1, 222, identifier="EVENT_2362_set_var_to_const_144"),
	SetVarToConst(FACTORY_FALL_2, 24),
	SetVarToConst(FACTORY_FALL_3, 30),
	SetVarToConst(FACTORY_FALL_4, 24),
	SetVarToConst(FACTORY_FALL_5, 16),
	SetVarToConst(FACTORY_FALL_6, 16),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShiftToXYCoords(x=7, y=116),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=6, y=117),
		A_WalkNortheastPixels(6),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ShiftToXYCoords(x=13, y=104),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_ShiftToXYCoords(x=12, y=105),
		A_WalkNortheastPixels(6),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_ShiftToXYCoords(x=18, y=114),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_ShiftToXYCoords(x=17, y=115),
		A_WalkNortheastPixels(6),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_ShiftToXYCoords(x=11, y=118),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(2),
		A_ShiftZDownPixels(15)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_ShiftToXYCoords(x=11, y=119),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(8),
		A_ShiftZDownPixels(15)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_ShiftToXYCoords(x=17, y=107),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(5),
		A_ShiftZDownPixels(15)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_ShiftToXYCoords(x=17, y=106),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkSoutheastPixels(2),
		A_ShiftZDownPixels(15)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_OverwriteSolidity(),
		A_TransferToXYZF(x=17, y=117, z=0, direction=EAST)
	]),
	FreezeCamera(),
	FadeInFromBlack(sync=False),
	SetAsyncActionScript(MARIO, A0415_PLAYER_ENTER_ANGLED_JUMPING_POSE),
	SetAsyncActionScript(MARIO, A0399_JUMPING_FALLING_STATE_IN_FACTORY),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	RunBackgroundEvent(event_id=E2385_ABYSS_FOUR_BOLT_ROOM_BACKGROUND, return_on_level_exit=True),
	UnfreezeCamera(),
	ClearBit(DIRECTIONAL_7045_7),
	Return()
])
