# E0405_TABLE_SHYSTER
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
	RunEventAsSubroutine(E1187_HENCHMAN_BATTLE_PACK_SELECTOR),
	RunEventAsSubroutine(E1010_SHYSTER_SUBROUTINE),
	JmpIfObjectInSpecificLevel(NPC_3, R480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F, ["EVENT_405_fade_in_from_black_async_24"]),
	PauseActionScript(NPC_0, identifier="EVENT_405_pause_action_script_6"),
	PauseActionScript(NPC_1),
	PauseActionScript(NPC_2),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FixedFCoordOff(),
		A_TransferToXYZF(x=5, y=20, z=4, direction=EAST),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FixedFCoordOff(),
		A_TransferToXYZF(x=4, y=21, z=4, direction=EAST),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FixedFCoordOff(),
		A_TransferToXYZF(x=5, y=22, z=4, direction=EAST),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferToXYZF(x=5, y=19, z=4, direction=EAST),
		A_FaceSouthwest()
	]),
	RememberLastObject(),
	SetBit(TEMP_7049_6),
	RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
	FadeInFromBlack(sync=False),
	JmpIfObjectNotInSpecificLevel(NPC_1, R481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F, ["EVENT_405_fade_in_from_black_async_26"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_Pause(60),
		A_FaceSouthwest()
	]),
	UnsyncDialog(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_AddZCoord1Step(),
		A_DecZCoord1Step()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_Walk1StepNorthwest(),
		A_WalkSouthwestSteps(3),
		A_WalkNorthwestSteps(1),
		A_WalkNortheastSteps(2),
		A_VisibilityOff()
	]),
	SetBit(OCCUPIED_MUSHROOM_KINGDOM_HOUSE_SHYSTER_1_DEFEATED),
	Return(),
	FadeInFromBlack(sync=False, identifier="EVENT_405_fade_in_from_black_async_24"),
	Return(),
	FadeInFromBlack(sync=False, identifier="EVENT_405_fade_in_from_black_async_26"),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	Return()
])
