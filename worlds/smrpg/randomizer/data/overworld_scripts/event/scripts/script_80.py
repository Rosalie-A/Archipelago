# E0080_SAVE_BLOCK_SUBROUTINE
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
	PauseScriptIfMenuOpen(),
	JmpIfBitSet(TEMP_7076_0, ["EVENT_81_ret_9"]),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_256_ret_0"]),
	SetBit(MONSTRO_SAVE_HOLE),
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_70C6),
	EnableControlsUntilReturn([]),
	FreezeCamera(),
	UnfreezeAllNPCs(),
	PlaySound(sound=SO150_EXIT_TO_WORLD_MAP, channel=6),
	SetAsyncActionScript(MARIO, A0408_JUMP_ON_SAVE_BLOCK),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_SequencePlaybackOff(),
		A_SetPriority(3),
		A_SetWalkingSpeed(FASTEST),
		A_ShadowOn(),
		A_ShiftZUpSteps(14),
		A_CopyVarToVar(from_var=UNKNOWN_70C6, to_var=PRIMARY_TEMP_700C),
		A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_70A9),
		A_UnknownCommand(bytearray(b'\xc8\x91')),
		A_RunAwayShift(),
		A_ReturnQueue()
	]),
	FadeOutToBlack(sync=False),
	OpenSaveMenu()
])
