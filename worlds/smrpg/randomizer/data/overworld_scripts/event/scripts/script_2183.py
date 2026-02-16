# E2183_KEEP_CHEWY_BATTLE_ROOM_SUMMON_3RD_BATTLE
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
	JmpIfBitSet(TEMP_7043_3, ["EVENT_2183_ret_25"]),
	SetBit(TEMP_7043_3),
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=16, y=38, z=0, direction=EAST),
		A_FaceSouthwest(),
		A_ResetProperties()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=14, y=41, z=0, direction=EAST),
		A_FaceSouthwest()
	]),
	JmpIfBitSet(KEEP_BOSS_1_DEFEATED, ["EVENT_2183_create_packet_at_npc_coords_6"]),
	RunEventAsSubroutine(E0941_KEEP_FIRST_BOSS_SET_SCRIPT),
	CreatePacketAtObjectCoords(packet=P034_GREY_EXPLOSION_SFX, target_npc=NPC_3, destinations=["EVENT_2183_create_packet_at_npc_coords_6"], identifier="EVENT_2183_create_packet_at_npc_coords_6"),
	SetSyncActionScript(NPC_0, A1005_KEEP_BATTLE_ROOM_SUMMON_ENEMY),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(5),
		A_FaceSouthwest7D(arg=0x17)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_Pause(40),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=False),
		A_Pause(70)
	]),
	StartBattleAtBattlefield(PACK242_OBSTACLE_AMANITA, BF07_BOWSERS_KEEP),
	JmpIfBitClear(GAME_OVER, ["EVENT_2183_action_queue_16"]),
	RestoreAllHP(),
	RestoreAllFP(),
	JmpToEvent(E3356_KEEP_RESPAWN_IN_LOBBY_UPON_FAILURE),
	Return(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=13, y=39, z=0, direction=EAST),
		A_VisibilityOff()
	], identifier="EVENT_2183_action_queue_16"),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=15, y=43, z=0, direction=EAST),
		A_VisibilityOff()
	]),
	ApplyTileModToLevel(use_alternate=True, room_id=R376_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2B_1ST_FIGHT_CHEWY, mod_id=36),
	ApplySolidityModToLevel(permanent=True, room_id=R376_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2B_1ST_FIGHT_CHEWY, mod_id=4),
	ApplyTileModToLevel(use_alternate=True, room_id=R376_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2B_1ST_FIGHT_CHEWY, mod_id=37),
	ApplySolidityModToLevel(permanent=True, room_id=R376_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2B_1ST_FIGHT_CHEWY, mod_id=5),
	FadeInFromBlack(sync=False),
	CreatePacketAtObjectCoords(packet=P034_GREY_EXPLOSION_SFX, target_npc=NPC_0, destinations=["EVENT_2183_create_packet_at_npc_coords_23"], identifier="EVENT_2183_create_packet_at_npc_coords_23"),
	CreatePacketAtObjectCoords(packet=P034_GREY_EXPLOSION_SFX, target_npc=NPC_3, destinations=["EVENT_2183_create_packet_at_npc_coords_23"]),
	Return(identifier="EVENT_2183_ret_25")
])
