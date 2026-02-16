# R052_MUSHROOM_KINGDOM_INN_2F
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
        allow_extra_sprite_buffer=True,
        extra_sprite_buffer_size=1,
        buffers = [
            Buffer(
                buffer_type=BufferType.TREASURE_CHEST,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.EMPTY_3,
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
    music=M0000_CURRENT,
    entrance_event=E0747_MUSHROOM_KINGDOM_INN_2F_LOADER,
    events=[
        Event(
            event=E0263_BOUNCE_ON_BED,
            x=5,
            y=119,
            z=3,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
        Event(
            event=E0263_BOUNCE_ON_BED,
            x=6,
            y=120,
            z=3,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
        Event(
            event=E0263_BOUNCE_ON_BED,
            x=7,
            y=122,
            z=3,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
        Event(
            event=E0263_BOUNCE_ON_BED,
            x=7,
            y=123,
            z=3,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
    ],
    exits=[
        RoomExit(
            x=1,
            y=122,
            z=0,
            f=EdgeDirection.SOUTHEAST,
            length=1,
            height=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R493_MUSHROOM_KINGDOM_INN_1F,
            show_message=False,
            dst_x=4,
            dst_y=84,
            dst_z=0,
            dst_z_half=True,
            dst_f=SOUTHWEST,
            x_bit_7=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.WALLET_GUY_ALSO_CASINO_ASSISTANTS_NPC_2,
            initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
            event_script=E0745_MUSHROOM_KINGDOM_INN_SLEEPING_GUY,
            action_script=A0223_BIG_TOAD_SLEEPING,
            visible=True,
            x=8,
            y=122,
            z=3,
            z_half=False,
            direction=NORTHWEST,
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
            byte3_bit7=True,
            slidable_along_walls=True,
            cant_move_if_in_air=False,
            byte7_upper2=3),
    ],
    extra_sprite_actions=[
        SpriteAnimationState.SLEEP,
    ]
)
