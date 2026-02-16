# E2586_BOOSTER_PASS_APPRENTICE_FIGHT
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
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetPriority(3)
	]),
	RunEventAsSubroutine(E1186_HENCHMAN_BATTLE_PACK_SELECTOR),
	JmpIfBitSet(RUN_AWAY, ["EVENT_2586_set_temp_action_script_7"]),
	JmpIfBitSet(GAME_OVER, ["EVENT_2586_stop_music_FD9F_10"]),
	FadeInFromBlack(sync=False),
	SetAsyncActionScript(NPC_9, A0851_BOOSTER_PASS_APPRENTICE_AFTER_FIGHT),
	Return(),
	SetTempSyncActionScript(NPC_9, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES, identifier="EVENT_2586_set_temp_action_script_7"),
	FadeInFromBlack(sync=False),
	Return(),
	StopMusicFD9F(identifier="EVENT_2586_stop_music_FD9F_10"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=8, sprite_offset=2, is_sequence=True, looping=True),
		A_FaceSouthwest()
	]),
	FadeInFromBlack(sync=False),
	SetAsyncActionScript(NPC_9, A0851_BOOSTER_PASS_APPRENTICE_AFTER_FIGHT),
	Pause(16),
	SetAsyncActionScript(MARIO, A0384_PLAYER_LOOK_DOWN_SHAKE_HEAD),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return()
])
