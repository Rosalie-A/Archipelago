# E1627_DYNA_HOUSE_LOADER
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
	FadeOutMusicToVolume(duration=1, volume=96),
	JmpIfBitClear(MINECART_CLEARED, ["EVENT_1627_jmp_if_bit_clear_9"]),
	JmpIfBitClear(TEMP_7042_1, ["EVENT_1627_summon_to_current_level_5"]),
	SummonObjectToCurrentLevel(NPC_1),
	SetSyncActionScript(NPC_1, A0160_SEQUENCE_LOOPING_ON),
	SummonObjectToCurrentLevel(NPC_2, identifier="EVENT_1627_summon_to_current_level_5"),
	SetSyncActionScript(NPC_2, A0160_SEQUENCE_LOOPING_ON),
	FadeInFromBlack(sync=False),
	Return(),
	JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["EVENT_1627_fade_in_from_black_async_12"], identifier="EVENT_1627_jmp_if_bit_clear_9"),
	SummonObjectToCurrentLevel(NPC_1),
	SetSyncActionScript(NPC_1, A0160_SEQUENCE_LOOPING_ON),
	FadeInFromBlack(sync=False, identifier="EVENT_1627_fade_in_from_black_async_12"),
	Return()
])
