# E3593_GET_ITEM_FROM_CHAPEL_HENCHMAN_3
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
	JmpToSubroutine(["EVENT_3593_pause_13"]),
	FreezeAllNPCsUntilReturn(),
	JmpIfBitSet(CHAPEL_ITEM_3_RETRIEVED, ["EVENT_3593_jmp_to_subroutine_8"]),
	SetVarToConst(PRIMARY_TEMP_7000, 2),
	RunEventAsSubroutine(E0180_NPC_QUEST_3_CONTAINER),
	UnfreezeAllNPCs(),
	SetBit(CHAPEL_ITEM_3_RETRIEVED),
	Return(),
	JmpToSubroutine(["EVENT_3593_pause_13"], identifier="EVENT_3593_jmp_to_subroutine_8"),
	FreezeAllNPCsUntilReturn(),
	SetVarToConst(PRIMARY_TEMP_7000, 2),
	RunDialog(dialog_id=DI2496_WHERES_THE_CROWN, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	Pause(1, identifier="EVENT_3593_pause_13"),
	JmpIfBitSet(TEMP_7044_6, ["EVENT_3593_pause_13"]),
	JmpIfBitSet(TEMP_7044_5, ["EVENT_3593_pause_13"]),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_3593_pause_13"]),
	Return()
])
