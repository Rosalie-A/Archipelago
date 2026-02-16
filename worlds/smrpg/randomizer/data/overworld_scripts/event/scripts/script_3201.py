# E3201_MINES_1ST_BOSS_FIGHT
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
	SetBit(TEMP_7043_0),
	SetVarToConst(PRIMARY_TEMP_7000, 518),
	RunEventAsSubroutine(E0353_BOSS_BATTLE),
	JmpIfBitSet(GAME_OVER, ["EVENT_3201_reset_and_choose_game_27"]),
	SetBit(MINES_BOSS_1_DEFEATED),
	RestoreAllHP(),
	RestoreAllFP(),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=MEM_70A8, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetAllSpeeds(VERY_FAST),
		A_SequenceLoopingOn(),
		A_JumpToHeight(56),
		A_Pause(32),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
		A_ReturnQueue()
	]),
	ResumeActionScript(MEM_70A8),
	RunEventAsSubroutine(E0253_NPC_QUEST_1_GRANT),
	RunEventAsSubroutine(E1199_OUTER_MNES_BOSS_UNLOCKS),
    SetVarToConst(PRIMARY_TEMP_7000, 518),
	JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE),
	Return(),
	ResetAndChooseGame(identifier="EVENT_3201_reset_and_choose_game_27")
])
