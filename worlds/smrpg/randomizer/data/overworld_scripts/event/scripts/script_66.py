# E0066_PIPE_DOWN_SUBROUTINE
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
	JmpIfBitClear(TEMP_707C_0, ["EVENT_66_end_all_11"]),
	Set7000ToTappedButton(),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_66_end_all_11"]),
	Set7000ToPressedButton(),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_66_end_all_11"]),
	CompareVarToConst(X_COORD_2, 256),
	JmpIfComparisonResultIsLesser(["EVENT_66_set_action_script_9"]),
	CopyVarToVar(from_var=X_COORD_2, to_var=Y_COORD_2),
	VarShiftLeft(X_COORD_2, 8),
	SetAsyncActionScript(MARIO, A0011_GO_DOWN_PIPE, identifier="EVENT_66_set_action_script_9"),
	Return(),
	ReturnAll(identifier="EVENT_66_end_all_11")
])
