# E0225_CHECK_VOUCHER_UNLOCK
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
    JmpIfBitSet(VOUCHER_CHECK_DONE, ["voucher_subroutine_exit"]),
    JmpIfBitClear(POST_MINES_LEVEL_MODS_COMPLETED, ["voucher_subroutine_exit"]),
    JmpIfBitClear(MARRYMORE_LIBERATED, ["voucher_subroutine_exit"]),
    JmpIfBitClear(TOWER_BOSS_1_STAR_PIECE, ["voucher_subroutine_exit"]),
    JmpIfBitClear(TEMPLE_BOSS_DEFEATED, ["voucher_subroutine_exit"]),
    JmpIfBitClear(MONSTRO_MIDDLE_DOOR_COMPLETED, ["voucher_subroutine_exit"]),
    JmpIfBitClear(DOJO_BOSS_4_DEFEATED, ["voucher_subroutine_exit"]),
    JmpIfBitClear(SHIP_LIBERATED, ["voucher_subroutine_exit"]),
    SummonObjectToSpecificLevel(NPC_3, R189_MARIOS_PIPEHOUSE),
    Return(identifier="voucher_subroutine_exit")
])
