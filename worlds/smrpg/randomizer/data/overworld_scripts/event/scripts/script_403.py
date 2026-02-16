# E0403_SHYSTER_HARASSING_WALLET_GUY
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
	RunEventAsSubroutine(E1190_HENCHMAN_BATTLE_PACK_SELECTOR),
	SetBit(TEMP_704A_2),
	SetVarToConst(TEMP_70A9, 26),
	RunEventAsSubroutine(E1010_SHYSTER_SUBROUTINE),
	ActionQueueSync(target=NPC_6, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	PauseActionScript(NPC_7),
	ActionQueueSync(target=MARIO, subscript=[
		A_TransferToXYZF(x=14, y=119, z=0, direction=EAST),
		A_FaceSouthwest()
	]),
	StartAsyncEmbeddedActionScript(target=NPC_7, prefix=0xF1, subscript=[
		A_TransferToXYZF(x=14, y=120, z=0, direction=EAST),
		A_FaceNortheast(),
		A_SetSolidityBits(cant_walk_through=True),
		A_SetSolidityBits(bit_0=True)
	]),
	RememberLastObject(),
	FadeInFromBlack(sync=False),
	Pause(30),
	RunDialog(dialog_id=DI0668_THAT_WAS_TOO_DARN_CLOSE, above_object=NPC_7, closable=True, sync=False, multiline=True, use_background=True),
	UnsyncDialog(),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6])
	]),
	SetSyncActionScript(NPC_7, A0128_WALK_RANDOM_DIRECTIONS),
	Return()
])
