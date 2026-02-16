# E0410_BED_SHYSTER
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
	SetBit(TEMP_704A_2),
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
	RunEventAsSubroutine(E1186_HENCHMAN_BATTLE_PACK_SELECTOR),
	RunEventAsSubroutine(E1010_SHYSTER_SUBROUTINE),
	SetBit(OCCUPIED_MUSHROOM_KINGDOM_HOUSE_SHYSTER_1_DEFEATED),
	JmpIfObjectInCurrentLevel(NPC_2, ["EVENT_410_fade_in_from_black_async_28"]),
	SetBit(OCCUPIED_MUSHROOM_KINGDOM_HOUSE_SHYSTER_2_DEFEATED),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_TransferToXYZF(x=7, y=44, z=6, direction=EAST),
		A_FaceNorthwest()
	]),
	FadeInFromBlack(sync=False),
	PauseActionScript(NPC_2),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_FixedFCoordOff(),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSoutheastSteps(2)
	]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	Pause(10),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_WalkSouthwestSteps(2),
		A_WalkSoutheastSteps(2),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouthwest()
	]),
	PauseActionScript(NPC_0),
	SetVarToConst(TEMP_70A9, 20),
	RunEventAsSubroutine(E0278_UNKNOWN),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceSouthwest(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	Pause(30),
	SetSyncActionScript(NPC_0, A0023_FAST_REPEATED_JUMPING),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkNorthwestSteps(5),
		A_WalkSouthwestSteps(5),
		A_UnknownCommand(bytearray(b'\xfd\xf2')),
		A_VisibilityOff()
	]),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return(),
	FadeInFromBlack(sync=False, identifier="EVENT_410_fade_in_from_black_async_28"),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return()
])
