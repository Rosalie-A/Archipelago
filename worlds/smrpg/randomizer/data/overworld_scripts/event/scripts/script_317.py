# E0317_MUSHROOM_KINGDOM_OCCUPIED_MOM
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
	JmpIfObjectInSpecificLevel(NPC_3, R480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F, ["EVENT_317_run_dialog_8"]),
	JmpIfObjectInSpecificLevel(NPC_4, R480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F, ["EVENT_317_run_dialog_8"]),
	JmpIfBitClear(OCCUPIED_MUSHROOM_KINGDOM_HOUSE_SHYSTER_2_DEFEATED, ["EVENT_317_jmp_if_object_not_in_level_5"]),
	RunDialog(dialog_id=DI0680_THANK_YOU, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_317_run_dialog_3"),
	Return(),
	JmpIfObjectNotInSpecificLevel(NPC_1, R481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F, ["EVENT_317_run_dialog_3"], identifier="EVENT_317_jmp_if_object_not_in_level_5"),
	RunDialog(dialog_id=DI0705_WORRIED_ABOUT_SON, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI0729_THINGS_IN_KITCHEN, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_317_run_dialog_8"),
	Return()
])
