# E2606_FACTORY_1ST_BOSS
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
		A_WalkToXYCoords(x=5, y=20)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNortheast(),
		A_WalkNortheastPixels(8)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_WalkToXYCoords(x=10, y=47),
		A_FaceNorthwest()
	]),
	StopEmbeddedActionScript(NPC_9),
	StopEmbeddedActionScript(SCREEN_FOCUS),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Walk1StepSouthwest(),
		A_WalkSouthwestPixels(4),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_WalkNorthwestPixels(12)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkSoutheastSteps(4)
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSequenceSpeed(VERY_FAST),
		A_WalkSoutheastSteps(4)
	]),
	RunEventAsSubroutine(E1186_HENCHMAN_BATTLE_PACK_SELECTOR),
	JmpIfBitClear(GAME_OVER, ["EVENT_2606_remove_from_current_level_13"]),
	ResetAndChooseGame(),
	RemoveObjectFromCurrentLevel(NPC_6, identifier="EVENT_2606_remove_from_current_level_13"),
	RemoveObjectFromCurrentLevel(NPC_7),
	RemoveObjectFromSpecificLevel(NPC_6, R469_FACTORY_GROUNDS_AREA_01),
	RemoveObjectFromSpecificLevel(NPC_7, R469_FACTORY_GROUNDS_AREA_01),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNorthwestPixels(1),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	FadeInFromBlack(sync=False),
	ActionQueueSync(target=NPC_8, subscript=[
		A_WalkSoutheastPixels(12)
	]),
	Pause(16),
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	JmpIfBitClear(GAME_OVER, ["EVENT_2606_restore_all_hp_24"]),
	ResetAndChooseGame(),
	RestoreAllHP(identifier="EVENT_2606_restore_all_hp_24"),
	RestoreAllFP(),
	RemoveObjectFromCurrentLevel(NPC_8),
	RemoveObjectFromSpecificLevel(NPC_8, R469_FACTORY_GROUNDS_AREA_01),
	SetBit(INNER_FACTORY_ROOM_1_COMPLETED),
	EnterArea(room_id=R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD, face_direction=NORTHWEST, x=9, y=43, z=5, run_entrance_event=True),
	RunEventAsSubroutine(E1241_INNER_FACTORY_1_BOSS_UNLOCKS),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
	Return()
])
