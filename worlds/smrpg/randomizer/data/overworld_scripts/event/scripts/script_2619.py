# E2619_ENDING_CREDITS_SUNSET
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
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkToXYCoords(x=0, y=3),
		A_WalkNorthSteps(8)
	]),
	RunEventAsSubroutine(E1191_ENDING_CREDITS_CLIFF_SHUFFLED_NPC_ANIMATION_LOADER),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=11, is_sequence=True, looping=True, identifier="ending_credits_sunset_npc_0_sequence"),
	], identifier="ending_credits_sunset_npc_0_sequence_setup"),
	RemoveObjectFromCurrentLevel(MARIO),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthSteps(4),
		A_WalkSouthPixels(8)
	]),
	StarMaskExpandFromScreenCenter(),
	Pause(384),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthSteps(4)
	]),
	StarMaskShrinkToScreenCenter(),
	PauseScriptUntilEffectDone(),
	StopEmbeddedActionScript(SCREEN_FOCUS),
	JmpToEvent(E3799_ENDING_CREDITS_PURPLE_STAR),
	Return()
])
