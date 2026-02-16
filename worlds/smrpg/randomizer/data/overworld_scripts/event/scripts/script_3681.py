# E3681_BIRDY_BECOMES_PLATFORM
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
	StartBattleAtBattlefield(PACK092_BIRDY_PACK_1, BF02_BEAN_VALLEY_BEANSTALKS),
	SetBit(TEMP_704A_2),
	RunEventAsSubroutine(E1011_POST_MINES_BOSS_CHECK_IF_WON),
	ClearBit(TEMP_704A_2),
	FadeInFromBlack(sync=False),
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 379, ["EVENT_3681_jmp_to_subroutine_8"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 380, ["EVENT_3681_jmp_to_subroutine_14"]),
	JmpToSubroutine(["EVENT_3681_action_queue_20"], identifier="EVENT_3681_jmp_to_subroutine_8"),
	PlaySound(sound=SO014_FLOWER, channel=6),
	RemoveObjectFromSpecificLevel(NPC_1, R379_BEAN_VALLEY_BEANSTALKS_AREA_02),
	RemoveObjectFromCurrentLevel(NPC_1),
	SummonObjectToCurrentLevel(NPC_2),
	Return(),
	JmpToSubroutine(["EVENT_3681_action_queue_20"], identifier="EVENT_3681_jmp_to_subroutine_14"),
	PlaySound(sound=SO014_FLOWER, channel=6),
	RemoveObjectFromSpecificLevel(NPC_0, R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02),
	RemoveObjectFromCurrentLevel(NPC_0),
	SummonObjectToCurrentLevel(NPC_1),
	Return(),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_StartLoopNTimes(2),
		A_VisibilityOff(),
		A_Pause(2),
		A_VisibilityOn(),
		A_Pause(8),
		A_EndLoop(),
		A_StartLoopNTimes(7),
		A_VisibilityOff(),
		A_Pause(4),
		A_VisibilityOn(),
		A_Pause(4),
		A_EndLoop(),
		A_StartLoopNTimes(7),
		A_VisibilityOff(),
		A_Pause(2),
		A_VisibilityOn(),
		A_Pause(2),
		A_EndLoop(),
		A_StartLoopNTimes(7),
		A_VisibilityOn(),
		A_Pause(1),
		A_VisibilityOff(),
		A_Pause(1),
		A_EndLoop()
	], identifier="EVENT_3681_action_queue_20"),
	Return()
])
