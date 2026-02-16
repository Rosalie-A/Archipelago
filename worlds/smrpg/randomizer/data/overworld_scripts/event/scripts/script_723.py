# E0723_MUSHROOM_KINGDOM_UNOCCUPIED_EXTERIOR_LOADER
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
	Set0158Bit7Offset(0x0158),
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 10),
	PlaySound(sound=SO000_SILENCE, channel=4),
	FadeOutMusicToVolume(duration=1, volume=127),
	JmpIfBitClear(MUSHROOM_KINGDOM_LIBERATED, ["EVENT_723_run_event_as_subroutine_20"]),
    JmpIfBitSet(KINGDOM_BOUNCER_FREED, ["EVENT_723_run_event_as_subroutine_20"]),
    ActionQueueAsync(NPC_9, subscript=[
        A_TransferToXYZF(16, 113, 2, NORTHWEST)
	]),
    SummonObjectToCurrentLevel(NPC_10),
    SetSyncActionScript(NPC_10, A0130_HENCHMAN_TERRORIZING_EAST_GUARD),
	SetSyncActionScript(NPC_9, A0131_EAST_GUARD_OCCUPIED),
	FadeInFromBlack(sync=False, identifier="EVENT_723_run_event_as_subroutine_20"),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_723_ret_9"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_723_ret_9"]),
	RunEventAsSubroutine(E3889_MUSHROOM_KINGDOM_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_723_ret_9")
])
