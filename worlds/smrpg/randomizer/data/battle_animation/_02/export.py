from smrpgpatchbuilder.datatypes.battle_animation_scripts.types import AnimationScriptBank
from .contents.script_0x02F455 import script as script_0x02F455
from .contents.script_0x02F461 import script as script_0x02F461
from .contents.script_0x02F4BF import script as script_0x02F4BF

bank = AnimationScriptBank(
	name = "0x02",
	scripts = [
		script_0x02F455,
		script_0x02F461,
		script_0x02F4BF,
	]
)
