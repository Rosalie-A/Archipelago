# E2361_ABYSS_AMEBOID_BUTTON_ROOM_LOADER
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
	SummonObjectToSpecificLevel(NPC_10, R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS),
	SummonObjectToSpecificLevel(NPC_11, R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS),
	SummonObjectToSpecificLevel(NPC_12, R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS),
	SummonObjectToSpecificLevel(NPC_13, R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS),
	SummonObjectToSpecificLevel(NPC_14, R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS),
	SummonObjectToSpecificLevel(NPC_15, R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS),
	JmpIfBitClear(ABYSS_GREEN_BUTTON, ["EVENT_2361_set_action_script_8"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True)
	]),
	SetSyncActionScript(NPC_1, A0456_FACTORY_SWITCH_ROOM_AMEBOID_INIT, identifier="EVENT_2361_set_action_script_8"),
	SetSyncActionScript(NPC_2, A0456_FACTORY_SWITCH_ROOM_AMEBOID_INIT),
	SetSyncActionScript(NPC_3, A0456_FACTORY_SWITCH_ROOM_AMEBOID_INIT),
	SetSyncActionScript(NPC_4, A0456_FACTORY_SWITCH_ROOM_AMEBOID_INIT),
	SetAsyncActionScript(NPC_5, A0456_FACTORY_SWITCH_ROOM_AMEBOID_INIT),
	SetSyncActionScript(NPC_1, A0457_FACTORY_SWITCH_ROOM_AMEBOID),
	SetSyncActionScript(NPC_2, A0459_FACTORY_SWITCH_ROOM_AMEBOID),
	SetSyncActionScript(NPC_3, A0461_FACTORY_SWITCH_ROOM_AMEBOID),
	SetSyncActionScript(NPC_4, A0463_FACTORY_SWITCH_ROOM_AMEBOID),
	SetSyncActionScript(NPC_5, A0481_FACTORY_SWITCH_ROOM_AMEBOID),
	FadeInFromBlack(sync=False),
	Return()
])
