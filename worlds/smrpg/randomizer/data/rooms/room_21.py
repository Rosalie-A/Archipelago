# R021_MUSHROOM_KINGDOM_CASTLE_BRANCH_ROOM_TO_VAULTGUEST_ROOM
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
                buffer_type=BufferType.FOUR_SPRITES_PER_ROW,
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
    entrance_event=E0401_GUEST_ROOM_ANTECHAMBER_LOADER,
    exits=[
        RoomExit(
            x=12,
            y=62,
            z=2,
            f=EdgeDirection.SOUTHEAST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL,
            show_message=False,
            dst_x=8,
            dst_y=30,
            dst_z=2,
            dst_z_half=False,
            dst_f=NORTHWEST,
            x_bit_7=False),
        RoomExit(
            x=13,
            y=70,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R031_MUSHROOM_KINGDOM_CASTLE_VAULT,
            show_message=False,
            dst_x=6,
            dst_y=90,
            dst_z=2,
            dst_z_half=True,
            dst_f=SOUTHWEST,
            x_bit_7=False),
    ],
    events=[
        Event(
            event=E3103_ENTER_MK_GUEST_ROOM,
            x=17,
            y=61,
            z=3,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.TOAD_NPC,
            initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
            event_script=E0400_GUEST_ROOM_GUARD,
            action_script=A0015_DO_NOTHING,
            visible=False,
            x=16,
            y=62,
            z=3,
            z_half=False,
            direction=SOUTHWEST,
            face_on_trigger=True,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=False,
            cant_walk_up_stairs=False,
            cant_walk_under=False,
            cant_pass_walls=True,
            cant_jump_through=False,
            cant_pass_npcs=False,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=False,
            cant_move_if_in_air=False,
            byte7_upper2=3),
    ]
)
