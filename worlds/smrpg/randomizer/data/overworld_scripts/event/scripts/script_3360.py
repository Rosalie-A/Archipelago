# E3360_KEEP_COIN_GAME_CHEST
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
	DisableObjectTrigger(NPC_2),
	PlaySound(sound=SO005_BLOCK_SWITCH, channel=6),
	Dec(ROSE_WAY_703C),
	JmpIfLoadedMemoryIsNot0(["EVENT_3360_set_temp_action_script_6"]),
	SetSyncActionScript(NPC_2, A0007_HIT_TREASURE_CHEST_CONTENTS_DEPLETED),
	Jmp(["EVENT_3360_set_7010_to_object_xyz_7"]),
	SetTempSyncActionScript(NPC_2, A0008_HIT_TREASURE_CHEST_CONTENTS_REMAINING, identifier="EVENT_3360_set_temp_action_script_6"),
	Set70107015ToObjectXYZ(target=NPC_2, identifier="EVENT_3360_set_7010_to_object_xyz_7"),
	CopyVarToVar(from_var=Z_COORD_1, to_var=PRIMARY_TEMP_7000),
	AddConstToVar(PRIMARY_TEMP_7000, 608),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Z_COORD_1),
	PlaySound(sound=SO013_COIN, channel=4),
	CreatePacketAt7010(packet=P016_BIG_COIN_BEING_COLLECTED, destinations=["EVENT_3360_ret_14"]),
	SetSyncActionScript(MEM_70A9, A0906_COIN_CHEST),
	Return(identifier="EVENT_3360_ret_14")
])
