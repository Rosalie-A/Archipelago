# E3293_SHIP_BULLET_COLLISION
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
	JmpIfMarioOnAnObjectOrNot(['EVENT_3293_pause_action_script_5', 'EVENT_3293_pause_action_script_8']),
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
	RunBackgroundEvent(event_id=E3294_SHIP_BULLET_COLLISION_BACKGROUND, return_on_level_exit=True),
	Return(),
	PauseActionScript(MEM_70A8, identifier="EVENT_3293_pause_action_script_5"),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_walk_through=True),
		A_PlaySound(sound=SO066_KICK_BALL_SHELL, channel=4),
		A_JumpToHeight(height=0, silent=True),
		A_FloatingOn(),
		A_Pause(20),
		A_VisibilityOff(),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	]),
	Return(),
	PauseActionScript(MEM_70A8, identifier="EVENT_3293_pause_action_script_8"),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_walk_through=True),
		A_PlaySound(sound=SO066_KICK_BALL_SHELL, channel=4),
		A_JumpToHeight(height=48, silent=True),
		A_FloatingOn(),
		A_Pause(30),
		A_VisibilityOff(),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	]),
	Return()
])
