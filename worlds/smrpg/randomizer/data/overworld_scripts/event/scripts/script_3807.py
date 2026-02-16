# E3807_ENDING_CREDITS_RACE_LOADER
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
	EnterArea(room_id=R505_ENDING_CREDITS_YOSTER_ISLE_CROCO_RACING_YOSHI, face_direction=SOUTH, x=4, y=16, z=0),
	ActionQueueSync(target=MARIO, subscript=[
		A_VisibilityOff(),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	SetTempSyncActionScript(NPC_3, A0803_INC_PALETTE_ROW),
	SetTempAsyncActionScript(NPC_2, A0803_INC_PALETTE_ROW),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetPriority(3),
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(1),
		A_SetSpriteSequence(index=15, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetPaletteRow(row=12)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_TransferXYZFPixels(x=248, y=4, z=0, direction=EAST)
	]),
	RememberLastObject(),
	JmpToEvent(E3806_ENDING_CREDITS_RACE_NPCS)
])
