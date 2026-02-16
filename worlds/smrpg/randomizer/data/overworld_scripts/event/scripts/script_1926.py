# E1926_TOWER_BALCONY_LOADER
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
	JmpIfBitSet(TOWER_BOSS_2_DEFEATED, ["EVENT_1926_jmp_if_bit_clear_22"]),
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	JmpIfBitClear(GAME_OVER, ["EVENT_1926_fade_out_music_to_volume_4"]),
	ResetAndChooseGame(),
	FadeOutMusicToVolume(duration=0, volume=0, identifier="EVENT_1926_fade_out_music_to_volume_4"),
	SummonObjectToSpecificLevel(NPC_0, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
	SummonObjectToSpecificLevel(NPC_1, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
	SummonObjectToSpecificLevel(NPC_2, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_3, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_4, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_5, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
	RemoveObjectFromSpecificLevel(NPC_6, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
	SetBit(UNKNOWN_TOWER_BOSS_2_FIGHT),
	SetBit(UNKNOWN_TOWER_BOSS_2_FIGHT_7089_2),
	EnterArea(room_id=R202_BOOSTER_TOWER_ENTRANCE, face_direction=SOUTHWEST, x=5, y=114, z=15),
	RestoreAllHP(),
	RestoreAllFP(),
	SetBit(TOWER_BOSS_2_DEFEATED),
	SetBit(STAR_PIECE_GRANT_DIRECTIONAL_BIT),
	JmpToEvent(E1328_TOWER_EXTERIOR_LOADER),
	Return(),
	JmpIfBitClear(MARRYMORE_LIBERATED, ["EVENT_1926_jmp_to_event_24"], identifier="EVENT_1926_jmp_if_bit_clear_22"),
	JmpToEvent(E1282_TOWER_BALCONY_LOADER_AFTER_MARRYMORE),
	JmpToEvent(E1283_TOWER_BALCONY_LOADER_BEFORE_MARRYMORE, identifier="EVENT_1926_jmp_to_event_24")
])
