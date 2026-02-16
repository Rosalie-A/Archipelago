# E2075_MONSTRO_SEALED_DOOR
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
    JmpIfBitSet(MONSTRO_MIDDLE_DOOR_COMPLETED, ["EVENT_2075_ess"]),
	SetVarToConst(ITEM_ID, ShinyStoneItem),
	StoreItemAt70A7QuantityTo7000(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2075_run_dialog_10"]),
	Pause(15, identifier="open_monstro_town_door"),
	ApplySolidityModToLevel(permanent=True, room_id=R324_MONSTRO_TOWN_OUTSIDE, mod_id=0),
	PlaySound(sound=SO081_STAR, channel=6),
	Pause(15),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromSpecificLevel(NPC_2, R324_MONSTRO_TOWN_OUTSIDE),
	Return(),
	RunDialog(dialog_id=DI3335_DUPLICATE, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False, identifier="EVENT_2075_run_dialog_10"),
	Return(),
	SetVarToConst(ITEM_ID, ExtraShinyStoneItem, identifier="EVENT_2075_ess"),
	StoreItemAt70A7QuantityTo7000(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2075_run_dialog_10"]),
    Jmp(["open_monstro_town_door"]),
])
