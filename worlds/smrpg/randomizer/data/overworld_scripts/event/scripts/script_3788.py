# E3788_BEAN_VALLEY_WEST_VINE_ROOM_SUMMON_PLATFORM
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
	JmpIfObjectInSpecificLevel(NPC_0, R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02, ["EVENT_3584_ret_0"]),
	JmpIfMarioInAir(["EVENT_3584_ret_0"]),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	Set70107015ToObjectXYZ(target=MARIO, bit_7=True),
	JmpIfVarEqualsConst(Z_COORD_1, 40, ["EVENT_3788_pause_6"]),
	JmpToEvent(E3584_BANK_20_RETURN_EVENT),
	Pause(1, identifier="EVENT_3788_pause_6"),
	Set7000ToTappedButton(),
	JmpIf7000AnyBitsSet(bits=[0, 1, 2, 3], destinations=["EVENT_3584_ret_0"]),
	JmpIf7000AnyBitsSet(bits=[7], destinations=["EVENT_3788_set_7000_to_pressed_button_11"]),
	Jmp(["EVENT_3788_pause_6"]),
	Set7000ToPressedButton(identifier="EVENT_3788_set_7000_to_pressed_button_11"),
	JmpIf7000AnyBitsSet(bits=[0, 1, 2, 3], destinations=["EVENT_3584_ret_0"]),
	PlaySound(sound=SO014_FLOWER, channel=6),
	SummonObjectToCurrentLevel(NPC_0),
	SummonObjectToSpecificLevel(NPC_0, R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02),
	Return()
])
