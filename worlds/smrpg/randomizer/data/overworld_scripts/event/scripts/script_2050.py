# E2050_MONSTRO_THWOMP
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
	Inc(MONSTRO_THWOMP_COUNTER),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_Pause(1),
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(6),
		A_SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True),
		A_Pause(15),
		A_SetWalkingSpeed(FAST),
		A_ShiftZUpSteps(3),
		A_SetWalkingSpeed(FASTER),
		A_ShiftZUpSteps(1),
		A_SetWalkingSpeed(VERY_FAST),
		A_ShiftZUpSteps(1),
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZDownSteps(3),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_ShiftZDownSteps(2)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_JumpToHeight(height=108, silent=True)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_JumpToHeight(height=108, silent=True)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_JumpToHeight(height=108, silent=True)
	]),
	PlaySound(sound=SO073_THWOMP_STOMP, channel=6),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkSouthPixels(22),
		A_WalkNorthPixels(22),
		A_WalkSouthPixels(14),
		A_WalkNorthPixels(14),
		A_WalkSouthPixels(8),
		A_WalkNorthPixels(8)
	]),
	JmpIfVarEqualsConst(MONSTRO_THWOMP_COUNTER, 7, ["EVENT_2050_run_dialog_9"]),
	Return(),
	RunDialog(dialog_id=DI2963_THWOMP_MAXED, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2050_run_dialog_9"),
	SetBit(MONSTRO_LEDGE_ITEM_KNOCKED_DOWN),
	Return()
])
