# E3229_SHIP_CLONE_TRANSFORM
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
	RunEventAsSubroutine(E1603_EXP_STAR_SUBROUTINE_CANCEL_TILE_EVENT),
	StopAllBackgroundEvents(),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_PlaySound(sound=SO044_GHOST_FLOAT, channel=4),
		A_TransferToObjectXY(NPC_0),
		A_Set700CToObjectCoord(target_npc=NPC_0, coord=COORD_F),
		A_FaceEast7C()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_StartLoopNTimes(3),
		A_VisibilityOff(),
		A_Pause(8),
		A_VisibilityOn(),
		A_Pause(8),
		A_EndLoop(),
		A_StartLoopNTimes(3),
		A_VisibilityOff(),
		A_Pause(4),
		A_VisibilityOn(),
		A_Pause(4),
		A_EndLoop(),
		A_StartLoopNTimes(3),
		A_VisibilityOff(),
		A_Pause(2),
		A_VisibilityOn(),
		A_Pause(2),
		A_EndLoop(),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_StartLoopNTimes(3),
		A_VisibilityOn(),
		A_Pause(8),
		A_VisibilityOff(),
		A_Pause(8),
		A_EndLoop(),
		A_StartLoopNTimes(3),
		A_VisibilityOn(),
		A_Pause(4),
		A_VisibilityOff(),
		A_Pause(4),
		A_EndLoop(),
		A_StartLoopNTimes(3),
		A_VisibilityOn(),
		A_Pause(2),
		A_VisibilityOff(),
		A_Pause(2),
		A_EndLoop(),
		A_VisibilityOn(),
		A_FaceMario(),
		A_Pause(2)
	]),
	ClearBit(TEMP_707C_5),
	SetBit(TEMP_707C_6),
	SetBit(TEMP_707C_7),
	SetVarToConst(BATTLE_PACK_ID, 77),
	RunEventAsSubroutine(E0016_FIGHT_REMOVE_PERMANENTLY),
	ActionQueueSync(target=NPC_0, subscript=[
		A_VisibilityOff(),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_UnknownCommand(bytearray(b'\xfd\xf2')),
		A_ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_VisibilityOff(),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_UnknownCommand(bytearray(b'\xfd\xf2')),
		A_ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	Return()
])
