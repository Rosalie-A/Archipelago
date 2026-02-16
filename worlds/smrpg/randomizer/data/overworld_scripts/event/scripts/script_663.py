# E0663_INITIATE_MARRYMORE_BOSS_FIGHT_IF_ALL_GEAR_COLLECTED
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
	ClearBit(TEMP_7042_0),
	ClearBit(TEMP_7042_1),
	ClearBit(TEMP_7042_2),
    JmpIfBitClear(CHAPEL_ITEM_1_RETRIEVED, ["EVENT_663_end_21"]),
    JmpIfBitClear(CHAPEL_ITEM_2_RETRIEVED, ["EVENT_663_end_21"]),
    JmpIfBitClear(CHAPEL_ITEM_3_RETRIEVED, ["EVENT_663_end_21"]),
    JmpIfObjectInSpecificLevel(NPC_5, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER, ["EVENT_663_end_21"]),
	CopyVarToVar(from_var=WEDDING_GEAR_COUNTER, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_663_adjust_music_tempo_12"]),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
	SetVarToConst(PRIMARY_TEMP_7000, 4),
	DecVarFrom7000(SECONDARY_TEMP_7024),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
	CopyVarToVar(from_var=WEDDING_GEAR_COUNTER, to_var=PRIMARY_TEMP_7000),
	RunDialog(dialog_id=DI2504_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(identifier="EVENT_663_end_21"),
	SlowDownMusicTempoBy(duration=0, change=0, identifier="EVENT_663_adjust_music_tempo_12"),
	StopBackgroundEvent(TIMER_701C),
	StopBackgroundEvent(TIMER_701E),
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=23, y=117, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=23, y=117, z=0, direction=EAST)
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_TransferToXYZF(x=23, y=117, z=0, direction=EAST)
	]),
	JmpToEvent(E0668_SUMMON_MARRYMORE_BOSS_TO_ROOM)
])
