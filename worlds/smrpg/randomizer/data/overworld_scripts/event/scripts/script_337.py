# E0337_MUSHROOM_KINGDOM_SHOP_BOOKSHELF
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
	JmpIfBitSet(TEMP_7043_0, ["EVENT_256_ret_0"]),
	SetBit(TEMP_7043_0),
	SetVarToConst(TEMP_70A9, 0),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_StartLoopNTimes(9),
		A_TurnClockwise45DegreesNTimes(1),
		A_Pause(2),
		A_EndLoop(),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=10, sprite_offset=2, is_sequence=True, looping=False),
		A_Pause(30),
		A_SetSequenceSpeed(VERY_SLOW),
		A_Pause(40),
		A_FaceSouth(),
		A_ResetProperties()
	]),
	Pause(30),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSouthwest(),
		A_Pause(20),
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True),
		A_JumpToHeight(height=64, silent=True)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FaceNortheast(),
		A_SetWalkingSpeed(VERY_FAST),
		A_AddZCoord1Step(),
		A_DecZCoord1Step(),
		A_SetWalkingSpeed(NORMAL)
	]),
	RunDialog(dialog_id=DI0608_SHOPKEEPER_YELLS_AT_YOU_ON_SHELF, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	RememberLastObject(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_JumpToHeight(64),
		A_Walk1StepSouthwest()
	]),
	RunEventAsSubroutine(E0278_UNKNOWN),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FaceSouthwest()
	]),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	UnsyncActionScript(MARIO),
	Return()
])
