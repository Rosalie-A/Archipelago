# E3930_MARRYMORE_GEAR_PRELOADER
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
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=16, y=84, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=19, y=78, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_TransferToXYZF(x=13, y=90, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_TransferToXYZF(x=22, y=72, z=2, direction=EAST),
		A_FaceNortheast(),
		A_SetSpriteSequence(index=14, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_TransferToXYZF(x=22, y=73, z=2, direction=EAST),
		A_WalkSoutheastPixels(5),
		A_FaceNortheast()
	]),
	JmpIfObjectInSpecificLevel(NPC_5, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER, ["EVENT_3930_pause_7"]),
	Jmp(["EVENT_3930_pause_9"]),
	Pause(1, identifier="EVENT_3930_pause_7"),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_TransferToObjectXYZ(NPC_7),
		A_ShiftZUpSteps(2),
		A_SetSolidityBits(cant_jump_through=True, bit_4=True, cant_walk_through=True)
	]),
	Pause(30, identifier="EVENT_3930_pause_9"),
	Jmp(["EVENT_3809_set_action_script_133"])
])
