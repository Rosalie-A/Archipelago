# R253_BEAN_VALLEY_MAGIC_BRICK_TO_BEANSTALK_AREA
# pyright: reportWildcardImportFromLibrary=false
from smrpgpatchbuilder.datatypes.levels.classes import ObjectType, EventInitiator, PostBattleBehaviour, Direction, EdgeDirection, ExitType, BufferType, BufferSpace, VramStore, ShadowSize
from smrpgpatchbuilder.datatypes.levels.classes import Buffer, Partition, DestinationProps, RoomExit, MapExit, Event, BattlePackNPC, RegularNPC, ChestNPC, BattlePackClone, RegularClone, ChestClone
from ...types.room import Room
from ...types.ally import SpriteAnimationState
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from . import npcs
from ..variables.room_names import *
from ..variables.overworld_area_names import *
from ..variables.music_names import *
from ..variables.event_script_names import *
from ..variables.action_script_names import *
room = Room(
    partition=Partition(
        ally_sprite_buffer_size=1,
        allow_extra_sprite_buffer=False,
        extra_sprite_buffer_size=0,
        buffers = [
            Buffer(
                buffer_type=BufferType.EMPTY_3,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.THREE_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.EMPTY_3,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            )
        ],
        full_palette_buffer=True
    ),
    music=M0042_STILLTHEROADISFULLOFMONSTERS,
    entrance_event=E2478_BEAN_VALLEY_BEANSTALK_ROOM_LOADER,
    events=[
        Event(
            event=E2559_BEAN_VALLEY_BEANSTALK_ROOM_PIPE,
            x=26,
            y=22,
            z=1,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.GROWING_VINE_BEANSTALK_NPC,
            initiator=EventInitiator.NONE,
            event_script=E2304_BANK_1F_RETURN_EVENT_2,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=27,
            y=27,
            z=3,
            z_half=True,
            direction=SOUTHWEST,
            face_on_trigger=False,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=False,
            cant_walk_up_stairs=False,
            cant_walk_under=False,
            cant_pass_walls=False,
            cant_jump_through=False,
            cant_pass_npcs=False,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        RegularClone( # 1
            npc=npcs.GROWING_VINE_BEANSTALK_NPC,
            event_script=E2304_BANK_1F_RETURN_EVENT_2,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=27,
            y=27,
            z=7,
            z_half=True,
            direction=SOUTHEAST),
        RegularNPC( # 2
            npc=npcs.BRICK_BEANSTALK_BLOCK_NPC,
            initiator=EventInitiator.HIT_FROM_BELOW,
            event_script=E2563_REVEAL_BEAN_VALLEY_BEANSTALK,
            action_script=A0849_BEAN_VALLEY_BEANSTALK_BRICK,
            visible=True,
            x=27,
            y=27,
            z=2,
            z_half=True,
            direction=SOUTHWEST,
            face_on_trigger=False,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=False,
            cant_walk_up_stairs=False,
            cant_walk_under=False,
            cant_pass_walls=False,
            cant_jump_through=False,
            cant_pass_npcs=False,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3),
    ],
    extra_sprite_actions=[
        SpriteAnimationState.RECOIL,
        SpriteAnimationState.DOWN_PIPE,
        SpriteAnimationState.CLIMB,
    ]
)
