# E1894_ABYSS_BOSS_2
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
	Pause(8),
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	SetBit(TEMP_707C_5),
	ClearBit(TEMP_707C_6),
	ClearBit(TEMP_707C_7),
	RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
	ApplySolidityModToLevel(permanent=True, room_id=R103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM, mod_id=32),
	FadeInFromBlack(sync=False),
	RestoreAllHP(),
	RestoreAllFP(),
	SetBit(ABYSS_BOSS_2_DEFEATED),
	RunEventAsSubroutine(E1240_OUTER_FACTORY_2_BOSS_UNLOCKS),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
	Return()
])
