# E0255_EXP_STAR_HIT
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
	DisableObjectTrigger(MEM_70A8),
	StartAsyncEmbeddedActionScript(target=MEM_70A8, prefix=0xF1, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[0, 1]),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	]),
	SetSyncActionScript(MEM_70A8, A1022_HIT_BY_EXP_STAR),
	IncEXPByPacket(identifier="inc_exp_by_packet"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_255_ret_13"]),
	SetBit(UNKNOWN_7064_4, identifier="EVENT_255_set_bit_5"),
	SetBit(EXP_STAR_BIT_6),
	UnfreezeAllNPCs(),
	Pause(3),
	CreatePacketAtObjectCoords(packet=P031_LEVELUP_TEXT, target_npc=MARIO, destinations=["EVENT_255_set_bit_5"]),
	PlaySound(sound=SO095_LEVEL_UP_WITH_STAR, channel=6),
	SetVarToConst(TIMER_701E, 64),
	RunBackgroundEventWithPauseReturnOnExit(event_id=E0254_EXP_STAR_HIT_SUBROUTINE, timer_var=TIMER_701E, bit_4=True, bit_5=True),
	Return(identifier="EVENT_255_ret_13")
])
