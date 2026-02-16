#A0348_SHIP_BOSS
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.event_script_names import *
from ....variables.overworld_sfx_names import *
from ....variables.room_names import *
from ....variables.variable_names import *
from ....packets import *
from ....items import *

script = ActionScript([
	A_SetPriority(3),
	A_SetSpriteSequence(index=10, is_sequence=True, looping=True, identifier="ship_boss_idle_sequence"),
	A_SequenceLoopingOn(identifier="ship_boss_idle_sequence_loop"),
	A_Pause(1, identifier="ACTION_348_pause_3"),
	A_JmpIfBitClear(TEMP_7044_7, ["ACTION_348_pause_3"]),
	A_ResetProperties(),
	A_SequenceLoopingOff(),
	A_ReturnQueue()
])
