# E1854_KEEP_DONKEY_ROOM_BACKGROUND
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
	SetVarToConst(TEMP_70A9, 22, identifier="EVENT_1854_set_var_to_const_0"),
	StartLoopNTimes(4),
	Pause(1, identifier="EVENT_1854_pause_2"),
	JmpIfObjectNotInSpecificLevel(MEM_70A9, R456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS, ["EVENT_1854_summon_to_level_5"]),
	Jmp(["EVENT_1854_pause_2"]),
	SummonObjectToSpecificLevel(MEM_70A9, R456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS, identifier="EVENT_1854_summon_to_level_5"),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=2, looping=False, mirror_sprite=True)
	]),
	SetSyncActionScript(MEM_70A9, A0824_KEEP_DONKEY_ROOM_BARRELS),
	Pause(68),
	Inc(TEMP_70A9),
	EndLoop(),
	Pause(20),
	Pause(1, identifier="EVENT_1854_pause_12"),
	JmpIfObjectInSpecificLevel(MEM_70A9, R456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS, ["EVENT_1854_pause_12"]),
	SummonObjectToSpecificLevel(MEM_70A9, R456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS),
	ClearBit(TEMP_7043_1),
	SetBit(TEMP_7043_0),
	Pause(2),
	ActionQueueSync(target=NPC_8, subscript=[
		A_PlaySound(sound=SO119_CZAR_DRAGON_ROAR, channel=4),
		A_SetSpriteSequence(index=2, looping=False, mirror_sprite=True)
	]),
	SetSyncActionScript(MEM_70A9, A0824_KEEP_DONKEY_ROOM_BARRELS),
	Pause(1, identifier="EVENT_1854_pause_20"),
	JmpIfObjectInSpecificLevel(MEM_70A9, R456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS, ["EVENT_1854_pause_20"]),
	SummonObjectToSpecificLevel(MEM_70A9, R456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS),
	SetBit(TEMP_7043_1),
	SetBit(TEMP_7043_0),
	Pause(2),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=2, looping=False, mirror_sprite=True)
	]),
	SetSyncActionScript(MEM_70A9, A0824_KEEP_DONKEY_ROOM_BARRELS),
	Pause(20),
	Jmp(["EVENT_1854_set_var_to_const_0"])
])
