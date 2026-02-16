from randomizer.types.physical_objects import SpriteAnimation
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (
    EventScript,
)
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
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.classes import UsableActionScriptCommand
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ...data.variables.action_script_names import *
from ...data.variables.battlefield_names import *
from ...data.variables.dialog_names import *
from ...data.variables.event_script_names import *
from ...data.variables.music_names import *
from ...data.variables.overworld_area_names import *
from ...data.variables.overworld_sfx_names import *
from ...data.variables.pack_names import *
from ...data.variables.room_names import *
from ...data.variables.shop_names import *
from ...data.variables.variable_names import *
from ...data.items import *
from ...data.packets import *
from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite


def gen_peck_left_subroutine(animation: SpriteAnimation) -> EventScript:
    peck_duration = 0
    assert animation.contact_frame is not None and animation.contact_frame < 19
    peck_duration = animation.contact_frame
    return EventScript(
        [
            ActionQueueAsync(
                target=NPC_3,
                subscript=[
                    A_SequencePlaybackOn(),
                    A_SetAllSpeeds(NORMAL),
                    A_Pause(3),
                    A_FaceSouthwest(),
                    A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True),
                    A_Pause(31 - peck_duration),
                    A_SequenceLoopingOn(),
                    *(
                        []
                        if animation.speed == NORMAL
                        else [A_SetSequenceSpeed(animation.speed)]
                    ),
                    A_SetSpriteSequence(
                        index=animation.sequence_id, looping=False
                    ),
                    A_Pause(peck_duration + 3),
		            A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, mirror_sprite=True),
                    A_FaceSoutheast()
                ],
            ),
            Return(),
        ]
    )

def gen_peck_middle_subroutine(animation: SpriteAnimation) -> EventScript:
    peck_duration = 0
    assert animation.contact_frame is not None and animation.contact_frame < 19
    peck_duration = animation.contact_frame
    assert peck_duration <= 19
    wait = max(16 - peck_duration, 0)
    return EventScript(
        [
            ActionQueueAsync(
                target=NPC_3,
                subscript=[
                    A_SequencePlaybackOn(),
                    A_SequenceLoopingOn(),
                    A_SetAllSpeeds(NORMAL),
                    *(
                        [A_Pause(wait)]
                        if wait > 0
                        else []
                    ),
                    *(
                        []
                        if animation.speed == NORMAL
                        else [A_SetSequenceSpeed(animation.speed)]
                    ),
                    A_SetSpriteSequence(
                        index=animation.sequence_id, is_sequence=True
                    ),
                    A_FaceSouthwest(),
                    A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True),
                    A_Pause(31 - peck_duration),
                    A_SetSpriteSequence(
                        index=animation.sequence_id, looping=False
                    ),
                    A_Pause(20 - wait),
                    A_SequenceLoopingOff(),
                ],
            ),
            Return(),
        ]
    )

def gen_start_battle(sprite: CompleteSprite, animation: SpriteAnimation) -> list[UsableActionScriptCommand]:
    assert animation.contact_frame is not None
    f = animation.contact_frame
    seq = animation.sequence_id

    spr_seq = sprite.animation.properties.sequences[seq]
    frames = spr_seq.frames
    frame_ctr = 0
    initial_pause = 0
    leadup_frames: list[int] = []
    for i, fr in enumerate(frames):
        frame_ctr += fr.duration
        if frame_ctr > f:
            if i > 3:
                leadup_frames.append(frames[i-4].mold_id)
            else:
                initial_pause += 40
            if i > 2:
                leadup_frames.append(frames[i-3].mold_id)
            else:
                initial_pause += 40
            if i > 1:
                leadup_frames.append(frames[i-2].mold_id)
            else:
                initial_pause += 40
            if i > 0:
                leadup_frames.append(frames[i-1].mold_id)
            else:
                initial_pause += 40
            break

    output: list[UsableActionScriptCommand] = [A_FaceSouthwest()]
    if initial_pause > 0:
        output.append(A_Pause(initial_pause))
    for mold_id in leadup_frames:
        output.append(A_SetSpriteSequence(index=mold_id, is_mold=True))
        output.append(A_Pause(40))
    return output
