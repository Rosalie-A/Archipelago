# E1697_BANDITS_WAY_CHEST_PLATFORMS_2
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
	CompareVarToConst(TEMP_702C, 27),
	JmpIfLoadedMemoryIs0(["EVENT_1696_jmp_if_bit_clear_10"]),
	SetVarToConst(TEMP_702C, 27),
	SetVarToConst(TEMP_70A9, 27),
	SetVarToConst(TEMP_70AA, 26),
	ActionQueueAsync(target=MEM_70A9, subscript=[
		A_BPL262728(),
		A_UnknownCommand(bytearray(b'\xfd$\x11\x12')),
		A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_702A)
	]),
	PauseActionScript(NPC_8),
	SetSyncActionScript(MEM_70AA, A0479_BANDITS_WAY_CHEST_PLATFORMS_ON_MOUNT),
	Pause(2),
	SetSyncActionScript(NPC_8, A0653_SLOW_ROTATING_PLATFORM),
	JmpIfBitClear(TEMP_707C_0, ["EVENT_1697_ret_13"]),
	RunEventAsSubroutine(E1840_PLATFORM_SUBROUTINE),
	ClearBit(TEMP_707C_0),
	Return(identifier="EVENT_1697_ret_13")
])
