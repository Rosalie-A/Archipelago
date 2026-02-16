# E2556_BEAN_VALLEY_BOSS_FIGHT
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
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	JmpIfBitClear(GAME_OVER, ["EVENT_2556_restore_all_hp_3"]),
	ResetAndChooseGame(),
	RestoreAllHP(identifier="EVENT_2556_restore_all_hp_3"),
	RestoreAllFP(),
	SetBit(BEAN_VALLEY_BOSS_DEFEATED),
	RemoveObjectFromSpecificLevel(NPC_0, R254_BEAN_VALLEY_SMILAX_AREA),
	RemoveObjectFromSpecificLevel(NPC_1, R254_BEAN_VALLEY_SMILAX_AREA),
	RemoveObjectFromSpecificLevel(NPC_2, R254_BEAN_VALLEY_SMILAX_AREA),
	SummonObjectToSpecificLevel(NPC_3, R254_BEAN_VALLEY_SMILAX_AREA),
	RemoveObjectFromCurrentLevel(NPC_0),
	RemoveObjectFromCurrentLevel(NPC_1),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_WalkNorthSteps(4)
	]),
	Pause(16),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SequenceLoopingOff(),
		A_ResetProperties(),
		A_Pause(32),
		A_SetSpriteSequence(index=2, looping=False),
		A_Pause(16),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	Pause(40),
	Pause(24),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_ShadowOff(),
		A_WalkNorthwestSteps(16)
	]),
	SetSyncActionScript(NPC_3, A0689_BEAN_VALLEY_BOSS_PRIZE_DRIFTS_DOWN),
	RunEventAsSubroutine(E1229_BEAN_VALLEY_BOSS_UNLOCKS),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
	Return()
])
