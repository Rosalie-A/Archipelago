# E1904_ABYSS_MACHINE_YARID_UPPER
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
	SetVarToConst(BATTLE_PACK_ID, 213),
	StartBattleWithPackAt700E(),
	JmpIfBitSet(RUN_AWAY, ["EVENT_1904_fade_in_from_black_sync_15"]),
	JmpIfBitSet(GAME_OVER, ["EVENT_1695_reset_and_choose_game_12"]),
	RemoveObjectFromCurrentLevel(MEM_70A8),
	FadeInFromBlack(sync=False),
	JmpIfBitSet(UNKNOWN_DIRECTIONAL_BIT_2, ["EVENT_1904_ret_14"]),
	Pause(1, identifier="EVENT_1904_pause_7"),
	CreatePacketAtObjectCoords(packet=P024_REGULAR_SOUND_EXPLOSION, target_npc=NPC_0, destinations=["EVENT_1904_pause_7"]),
	RemoveObjectFromCurrentLevel(NPC_0),
	RemoveObjectFromSpecificLevel(NPC_0, R474_SMITHY_FACTORY_AREA_15_FALLING_YARIDOVICHS),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_SetSpriteSequence(index=7, sprite_offset=3, is_sequence=True, looping=True),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(height=128, silent=True),
		A_WalkSouthSteps(3),
		A_SetAllSpeeds(NORMAL),
		A_ResetProperties(),
		A_FloatingOn()
	]),
	SetBit(UNKNOWN_DIRECTIONAL_BIT_2),
	ApplySolidityModToLevel(permanent=True, room_id=R474_SMITHY_FACTORY_AREA_15_FALLING_YARIDOVICHS, mod_id=1),
	Return(identifier="EVENT_1904_ret_14"),
	FadeInFromBlack(sync=True, identifier="EVENT_1904_fade_in_from_black_sync_15"),
	DisableObjectTrigger(MEM_70A8),
	ResumeActionScript(MEM_70A8),
	Return()
])
