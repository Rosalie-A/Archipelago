# E2405_STAR_HILL_FINAL_AREA_LOADER
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
	SummonObjectToSpecificLevel(NPC_5, R158_STAR_HILL_AREA_02),
	SummonObjectToSpecificLevel(NPC_6, R158_STAR_HILL_AREA_02),
	SummonObjectToSpecificLevel(NPC_7, R158_STAR_HILL_AREA_02),
	SummonObjectToSpecificLevel(NPC_8, R158_STAR_HILL_AREA_02),
	SummonObjectToSpecificLevel(NPC_6, R157_STAR_HILL_AREA_03),
	SummonObjectToSpecificLevel(NPC_7, R157_STAR_HILL_AREA_03),
	SummonObjectToSpecificLevel(NPC_8, R157_STAR_HILL_AREA_03),
	SummonObjectToSpecificLevel(NPC_9, R157_STAR_HILL_AREA_03),
	SummonObjectToSpecificLevel(NPC_0, R159_STAR_HILL_AREA_04),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthPixels(12),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_ShadowOn()
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_WalkWestPixels(7)
	]),
	ActionQueueSync(target=NPC_13, subscript=[
		A_WalkEastPixels(8)
	]),
	ActionQueueSync(target=NPC_14, subscript=[
		A_WalkWestPixels(8)
	]),
	FreezeCamera(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ShiftToXYCoords(x=27, y=108),
		A_OverwriteSolidity(),
		A_FloatingOff(),
		A_ShadowOn()
	]),
	FadeInFromBlack(sync=False),
	Pause(16),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R159_STAR_HILL_AREA_04, mod_id=0),
	PlaySound(sound=SO126_EMERGE_DEEP_WATER, channel=6),
	Pause(16),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSequenceSpeed(FAST),
		A_WalkSouthwestSteps(2)
	]),
	Pause(16),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	ApplyTileModToLevel(use_alternate=True, room_id=R159_STAR_HILL_AREA_04, mod_id=13),
	PlaySound(sound=SO125_ENTER_DEEP_WATER, channel=6),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	UnfreezeCamera(),
	Return()
])
