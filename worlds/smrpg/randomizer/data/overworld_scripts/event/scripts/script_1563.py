# E1563_LANDS_END_MARIO_OOB
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
	Set7016701BToObjectXYZ(target=NPC_0, bit_7=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_PlaySound(sound=SO058_INSERT, channel=4),
		A_Pause(30),
		A_SetSequenceSpeed(SLOW),
		A_SetSpriteSequence(index=8, is_sequence=True, looping=True, mirror_sprite=True),
		A_PlaySound(sound=SO034_SQUIRM_WRITHE, channel=4),
		A_Pause(30),
		A_PlaySound(sound=SO034_SQUIRM_WRITHE, channel=4),
		A_Pause(30),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_PlaySound(sound=SO034_SQUIRM_WRITHE, channel=4),
		A_Pause(40),
		A_ResetProperties(),
		A_Pause(20),
		A_PlaySound(sound=SO034_SQUIRM_WRITHE, channel=4),
		A_StartLoopNTimes(3),
		A_TurnClockwise45DegreesNTimes(7),
		A_Pause(3),
		A_EndLoop(),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True),
		A_StartLoopNTimes(4),
		A_PlaySound(sound=SO043_POP_UP_FROM_WATER, channel=6),
		A_Pause(10),
		A_EndLoop(),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_PlaySound(sound=SO024_TAPPING_FEET, channel=4),
		A_Pause(50),
		A_SetSequenceSpeed(NORMAL),
		A_ResetProperties(),
		A_JumpToHeight(112),
		A_WalkTo70167018(),
		A_SetAllSpeeds(NORMAL)
	]),
	Return()
])
