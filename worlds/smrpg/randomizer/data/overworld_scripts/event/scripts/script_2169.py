# E2169_KEEP_ALLEY_RAT_BATTLE_ROOM_SUMMON_4TH_BATTLE
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
	JmpIfBitSet(TEMP_7043_4, ["EVENT_2169_ret_25"]),
	SetBit(TEMP_7043_4),
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=20, y=30, z=0, direction=EAST),
		A_FaceSouthwest(),
		A_ResetProperties()
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_TransferToXYZF(x=18, y=33, z=0, direction=EAST),
		A_FaceSouthwest()
	]),
	JmpIfBitSet(KEEP_BOSS_1_DEFEATED, ["EVENT_2169_create_packet_at_npc_coords_6"]),
	RunEventAsSubroutine(E0941_KEEP_FIRST_BOSS_SET_SCRIPT),
	CreatePacketAtObjectCoords(packet=P034_GREY_EXPLOSION_SFX, target_npc=NPC_4, destinations=["EVENT_2169_create_packet_at_npc_coords_6"], identifier="EVENT_2169_create_packet_at_npc_coords_6"),
	SetSyncActionScript(NPC_0, A1005_KEEP_BATTLE_ROOM_SUMMON_ENEMY),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(5),
		A_FaceSouthwest7D(arg=0x18)
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_Pause(40),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=False),
		A_Pause(65)
	]),
	StartBattleAtBattlefield(PACK231_OBSTACLE_GECKIT, BF07_BOWSERS_KEEP),
	JmpIfBitClear(GAME_OVER, ["EVENT_2169_action_queue_16"]),
	RestoreAllHP(),
	RestoreAllFP(),
	JmpToEvent(E3356_KEEP_RESPAWN_IN_LOBBY_UPON_FAILURE),
	Return(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=17, y=31, z=0, direction=EAST),
		A_VisibilityOff()
	], identifier="EVENT_2169_action_queue_16"),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_TransferToXYZF(x=19, y=35, z=0, direction=EAST),
		A_VisibilityOff()
	]),
	ApplyTileModToLevel(use_alternate=True, room_id=R460_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1B_1ST_FIGHT_ALLEY_RAT, mod_id=38),
	ApplySolidityModToLevel(permanent=True, room_id=R460_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1B_1ST_FIGHT_ALLEY_RAT, mod_id=6),
	ApplyTileModToLevel(use_alternate=True, room_id=R460_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1B_1ST_FIGHT_ALLEY_RAT, mod_id=39),
	ApplySolidityModToLevel(permanent=True, room_id=R460_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1B_1ST_FIGHT_ALLEY_RAT, mod_id=7),
	FadeInFromBlack(sync=False),
	CreatePacketAtObjectCoords(packet=P034_GREY_EXPLOSION_SFX, target_npc=NPC_0, destinations=["EVENT_2169_create_packet_at_npc_coords_23"], identifier="EVENT_2169_create_packet_at_npc_coords_23"),
	CreatePacketAtObjectCoords(packet=P034_GREY_EXPLOSION_SFX, target_npc=NPC_4, destinations=["EVENT_2169_create_packet_at_npc_coords_23"]),
	Return(identifier="EVENT_2169_ret_25")
])
