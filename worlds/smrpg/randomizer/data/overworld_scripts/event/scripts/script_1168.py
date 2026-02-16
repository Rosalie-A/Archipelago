# E1168_SEASIDE_LIBERATED_INNKEEPER
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
	RunDialog(dialog_id=DI2916_SEASIDE_INNKEEPER, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_1168_run_dialog_14"]),
	StoreCoinCountTo7000(),
	CompareVarToConst(PRIMARY_TEMP_7000, 15),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1168_set_var_to_const_10"]),
	RunDialog(dialog_id=DI2918_SEASIDE_INNKEEPER_INSUFFICIENT_COINS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	StoreCoinCountTo7000(),
	Dec7000FromCoins(),
	SetBit(LIBERATED_SEASIDE_INN),
	Jmp(["EVENT_273_fade_out_music_to_volume_17"]),
	SetVarToConst(PRIMARY_TEMP_7000, 15, identifier="EVENT_1168_set_var_to_const_10"),
	Dec7000FromCoins(),
	SetBit(LIBERATED_SEASIDE_INN),
	Jmp(["EVENT_273_fade_out_music_to_volume_17"]),
	RunDialog(dialog_id=DI2917_SEASIDE_INNKEEPER_DECLINE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1168_run_dialog_14"),
	Return()
])
