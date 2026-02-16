# E0393_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F_LOADER
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
	RunEventAsSubroutine(E0770_MUSHROOM_KINGDOM_OCCUPIED_JUMPING_KIDS_HOUSE_1F_SHUFFLED_NPC_ANIMATION_LOADER),
	JmpIfObjectInSpecificLevel(NPC_3, R480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F, ["EVENT_393_set_bit_17"]),
	JmpIfObjectInSpecificLevel(NPC_4, R480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F, ["EVENT_393_set_bit_17"]),
	JmpIfObjectNotInSpecificLevel(NPC_1, R481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F, ["EVENT_393_summon_to_current_level_5"]),
	JmpIfBitSet(OCCUPIED_MUSHROOM_KINGDOM_HOUSE_SHYSTER_1_DEFEATED, ["EVENT_393_jmp_if_object_not_in_level_28"]),
	SummonObjectToCurrentLevel(NPC_0, identifier="EVENT_393_summon_to_current_level_5"),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=7, y=22, z=4, direction=EAST),
		A_FaceNorthwest()
	]),
	PauseActionScript(NPC_0),
	SetSyncActionScript(NPC_0, A0119_SLOW_SEQUENCE_LOOP),
	ActionQueueSync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=7, y=16, z=4, direction=EAST),
		A_FaceNortheast()
	], identifier="EVENT_393_action_queue_9"),
	ActionQueueSync(target=NPC_2, subscript=[
		A_TransferToXYZF(x=5, y=18, z=4, direction=EAST),
		A_FaceSouthwest()
	]),
	RememberLastObject(),
	PauseActionScript(NPC_1),
	PauseActionScript(NPC_2),
	SetSyncActionScript(NPC_1, A0119_SLOW_SEQUENCE_LOOP),
	SetSyncActionScript(NPC_2, A0128_WALK_RANDOM_DIRECTIONS),
	Jmp(["EVENT_261_fade_out_music_to_volume_0"]),
	SetBit(TEMP_7043_3, identifier="EVENT_393_set_bit_17"),
	PauseActionScript(NPC_0),
	PauseActionScript(NPC_1),
	PauseActionScript(NPC_2),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FixedFCoordOn()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FixedFCoordOn()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FixedFCoordOn()
	]),
	SetSyncActionScript(NPC_0, A0113_HENCHMAN_BOUNCING_IN_PLACE),
	SetSyncActionScript(NPC_1, A0113_HENCHMAN_BOUNCING_IN_PLACE),
	SetSyncActionScript(NPC_2, A0113_HENCHMAN_BOUNCING_IN_PLACE),
	Jmp(["EVENT_261_fade_out_music_to_volume_0"]),
	JmpIfObjectNotInSpecificLevel(NPC_1, R481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F, ["EVENT_393_summon_to_current_level_5"], identifier="EVENT_393_jmp_if_object_not_in_level_28"),
	RemoveObjectFromCurrentLevel(NPC_0),
	Jmp(["EVENT_393_action_queue_9"])
])
