# E1119_SEASIDE_OCCUPIED_EXTERIOR_LOADER
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
	JmpIfBitSet(SEASIDE_SHED_EMPTIED, ["EVENT_1119_jmp_if_bit_set_3"]),
	SummonObjectToCurrentLevel(NPC_6),
	SummonObjectToSpecificLevel(NPC_6, R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE),
	JmpIfBitSet(SEASIDE_LIBERATED, ["EVENT_1119_play_music_default_volume_7"], identifier="EVENT_1119_jmp_if_bit_set_3"),
	PlayMusicAtDefaultVolume(M0015_HERE_SSOMEWEAPONS),
	Jmp(["EVENT_1119_jmp_if_present_in_current_level_10"]),
	Return(),
	PlayMusicAtDefaultVolume(M0005_SEASIDETOWN, identifier="EVENT_1119_play_music_default_volume_7"),
	Jmp(["EVENT_1119_jmp_if_present_in_current_level_10"]),
	Return(),
	JmpIfObjectInCurrentLevel(NPC_6, ["EVENT_1119_apply_solidity_mod_13"], identifier="EVENT_1119_jmp_if_present_in_current_level_10"),
	Jmp(["EVENT_1119_jmp_if_bit_clear_23"]),
	Return(),
	ApplySolidityModToLevel(permanent=True, room_id=R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, mod_id=0, identifier="EVENT_1119_apply_solidity_mod_13"),
	Jmp(["EVENT_1119_jmp_if_bit_clear_23"]),
	Return(),
	RunEventAsSubroutine(E0806_SEASIDE_OCCUPIED_EXTERIOR_SHUFFLED_NPC_ANIMATION_LOADER, identifier="EVENT_1119_run_event_as_subroutine_16"),
	FadeInFromBlack(sync=True),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_1119_ret_22"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1119_ret_22"]),
	RunEventAsSubroutine(E3904_SEASIDE_TOWN_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_1119_ret_22"),
	JmpIfBitClear(SEASIDE_BOSS_AVAILABLE, ["EVENT_1119_run_event_as_subroutine_16"], identifier="EVENT_1119_jmp_if_bit_clear_23"),
	JmpIfBitSet(SEASIDE_BOSS_SET, ["EVENT_1119_run_event_as_subroutine_16"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=13, y=56, z=2, direction=EAST),
		A_WalkSouthwestSteps(1),
		A_WalkSoutheastSteps(1),
		A_FaceSouthwest(),
		A_VisibilityOn()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=13, y=57, z=2, direction=EAST),
		A_WalkSouthwestSteps(1),
		A_WalkSoutheastSteps(1),
		A_FaceSouthwest(),
		A_VisibilityOn()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_TransferToXYZF(x=14, y=59, z=2, direction=EAST),
		A_WalkSouthwestSteps(1),
		A_WalkSoutheastSteps(1),
		A_FaceSouthwest(),
		A_VisibilityOn()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=15, y=60, z=2, direction=EAST),
		A_WalkSouthwestSteps(1),
		A_WalkSoutheastSteps(1),
		A_FaceSouthwest(),
		A_VisibilityOn()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_TransferToXYZF(x=14, y=58, z=2, direction=EAST),
		A_OverwriteSolidity(),
		A_WalkSouthwestSteps(1),
		A_WalkSoutheastSteps(1),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferToXYZF(x=12, y=63, z=2, direction=EAST),
		A_WalkSouthwestSteps(1),
		A_FaceNortheast()
	]),
	SetSyncActionScript(NPC_0, A0147_SEASIDE_HENCHMAN),
	SetSyncActionScript(NPC_1, A0147_SEASIDE_HENCHMAN),
	SetSyncActionScript(NPC_2, A0147_SEASIDE_HENCHMAN),
	SetSyncActionScript(NPC_3, A0147_SEASIDE_HENCHMAN),
	SetSyncActionScript(NPC_4, A0147_SEASIDE_HENCHMAN),
	RunEventAsSubroutine(E0806_SEASIDE_OCCUPIED_EXTERIOR_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_1119_action_queue_42"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1119_action_queue_42"]),
	RunEventAsSubroutine(E3904_SEASIDE_TOWN_STAR_PIECE_SIGNAL),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(NORMAL),
		A_WalkNortheastSteps(1),
		A_SetSequenceSpeed(NORMAL),
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastPixels(8)
	], identifier="EVENT_1119_action_queue_42"),
	Pause(30),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestPixels(5)
	]),
	Pause(30),
	UnfreezeCamera(),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_ResetProperties()
	]),
	Pause(30),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSequenceSpeed(SLOW),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(15),
		A_ResetProperties(),
		A_SetAllSpeeds(NORMAL)
	]),
	Pause(30),
	PlaySound(sound=SO011_WHOOSH_AWAY, channel=6),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNorthwestSteps(30),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNorthwestSteps(30),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNorthwestSteps(30),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNorthwestSteps(30),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNorthwestSteps(30),
		A_VisibilityOff()
	]),
	RemoveObjectFromSpecificLevel(NPC_0, R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE),
	RemoveObjectFromSpecificLevel(NPC_1, R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE),
	RemoveObjectFromSpecificLevel(NPC_2, R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE),
	RemoveObjectFromSpecificLevel(NPC_3, R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE),
	RemoveObjectFromSpecificLevel(NPC_4, R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE),
	RemoveObjectFromSpecificLevel(NPC_0, R209_SEASIDE_TOWN_DURING_YARIDOVICH_INN_1F),
	RemoveObjectFromSpecificLevel(NPC_0, R210_SEASIDE_TOWN_DURING_YARIDOVICH_INN_2F),
	RemoveObjectFromSpecificLevel(NPC_0, R211_SEASIDE_TOWN_DURING_YARIDOVICH_ELDERS_HOUSE_1F),
	RemoveObjectFromSpecificLevel(NPC_0, R214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP),
	RemoveObjectFromSpecificLevel(NPC_1, R214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP),
	RemoveObjectFromSpecificLevel(NPC_0, R215_SEASIDE_TOWN_DURING_YARIDOVICH_HEALTH_FOOD_STORE_LEFTMOST),
	RemoveObjectFromSpecificLevel(NPC_0, R216_SEASIDE_TOWN_DURING_YARIDOVICH_MUSHROOM_BOY_SHOP_MIDDLE, identifier="EVENT_1119_remove_from_level_68"),
	RemoveObjectFromSpecificLevel(NPC_1, R216_SEASIDE_TOWN_DURING_YARIDOVICH_MUSHROOM_BOY_SHOP_MIDDLE),
	RemoveObjectFromSpecificLevel(NPC_0, R217_SEASIDE_TOWN_DURING_YARIDOVICH_ACCESSORY_SHOP_RIGHTMOST),
	RemoveObjectFromSpecificLevel(NPC_2, R214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP),
	RemoveObjectFromSpecificLevel(NPC_3, R214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP),
	SetBit(SEASIDE_BOSS_SET),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_SetAllSpeeds(NORMAL),
		A_WalkNortheastSteps(1),
		A_SetVRAMPriority(NORMAL_PRIORITY)
	]),
	Return()
])
