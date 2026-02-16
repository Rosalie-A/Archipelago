# E3744_NIMBUS_EXTERIOR_SHY_AWAY
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
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_ResetProperties()
	]),
	Pause(20),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(30),
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_WalkSoutheastSteps(8),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	]),
	RemoveObjectFromSpecificLevel(NPC_9, R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA),
	RemoveObjectFromCurrentLevel(NPC_9),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouth()
	]),
	Return()
])
