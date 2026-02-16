# E0596_MINES_BOSS_ROOM_BACKGROUND_EXPLOSIONS
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
	Pause(1, identifier="EVENT_596_pause_0"),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_596_pause_19"]),
	JmpIfObjectInCurrentLevel(NPC_2, ["EVENT_596_pause_4"]),
	Jmp(["EVENT_596_pause_0"]),
	Pause(34, identifier="EVENT_596_pause_4"),
	SetSyncActionScript(NPC_1, A0299_MINES_FINAL_BOSS_ROOM_TINY_HENCHMAN_EXPLODE),
	Pause(1, identifier="EVENT_596_pause_6"),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_596_pause_22"]),
	JmpIfObjectInCurrentLevel(NPC_3, ["EVENT_596_pause_10"]),
	Jmp(["EVENT_596_pause_6"]),
	Pause(34, identifier="EVENT_596_pause_10"),
	SetSyncActionScript(NPC_2, A0299_MINES_FINAL_BOSS_ROOM_TINY_HENCHMAN_EXPLODE),
	Pause(1, identifier="EVENT_596_pause_12"),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_596_pause_25"]),
	JmpIfObjectInCurrentLevel(NPC_1, ["EVENT_596_pause_16"]),
	Jmp(["EVENT_596_pause_12"]),
	Pause(34, identifier="EVENT_596_pause_16"),
	SetSyncActionScript(NPC_3, A0299_MINES_FINAL_BOSS_ROOM_TINY_HENCHMAN_EXPLODE),
	Jmp(["EVENT_596_pause_0"]),
	Pause(2, identifier="EVENT_596_pause_19"),
	CreatePacketAtObjectCoords(packet=P033_BOMB_EXPLOSION, target_npc=NPC_2, destinations=["EVENT_596_pause_19"]),
	Jmp(["EVENT_596_pause_6"]),
	Pause(2, identifier="EVENT_596_pause_22"),
	CreatePacketAtObjectCoords(packet=P033_BOMB_EXPLOSION, target_npc=NPC_3, destinations=["EVENT_596_pause_22"]),
	Jmp(["EVENT_596_pause_12"]),
	Pause(2, identifier="EVENT_596_pause_25"),
	CreatePacketAtObjectCoords(packet=P033_BOMB_EXPLOSION, target_npc=NPC_1, destinations=["EVENT_596_pause_25"]),
	Jmp(["EVENT_596_pause_0"])
])
