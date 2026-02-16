# R006_MARRYMORE_INN_2F
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
                buffer_type=BufferType.FOUR_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.FOUR_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            )
        ],
        full_palette_buffer=True
    ),
    music=M0039_MARRYMORE,
    entrance_event=E0612_MARRYMORE_INN_2F_HALLWAY_LOADER,
    exits=[
        RoomExit(
            x=14,
            y=53,
            z=0,
            f=EdgeDirection.SOUTHEAST,
            length=1,
            height=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=True,
            byte_2_bit_2=False,
            destination=R007_MARRYMORE_INN_1F,
            show_message=False,
            dst_x=7,
            dst_y=60,
            dst_z=0,
            dst_z_half=True,
            dst_f=SOUTHWEST,
            x_bit_7=False),
        RoomExit(
            x=16,
            y=43,
            z=2,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R009_MARRYMORE_INN_REGULAR_ROOM,
            show_message=False,
            dst_x=14,
            dst_y=20,
            dst_z=0,
            dst_z_half=False,
            dst_f=NORTHEAST,
            x_bit_7=False),
        RoomExit(
            x=13,
            y=41,
            z=3,
            f=EdgeDirection.SOUTHEAST,
            length=1,
            height=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=True,
            byte_2_bit_2=False,
            destination=R011_MARRYMORE_INN_3F,
            show_message=False,
            dst_x=12,
            dst_y=73,
            dst_z=1,
            dst_z_half=True,
            dst_f=NORTHEAST,
            x_bit_7=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.MARRYMORE_KID_PURPLE_NPC,
            initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
            event_script=E0603_MARRYMORE_BELLHOP_LOBBY_WHILE_GUEST,
            action_script=A0119_SLOW_SEQUENCE_LOOP,
            visible=True,
            x=16,
            y=76,
            z=0,
            z_half=False,
            direction=NORTHWEST,
            face_on_trigger=True,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=True,
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
        RegularNPC( # 1
            npc=npcs.OLD_WOMAN_GREEN_GREY_NPC,
            initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
            event_script=E0621_MARRYMORE_INN_ELDERLY_GUEST,
            action_script=A0119_SLOW_SEQUENCE_LOOP,
            visible=True,
            x=16,
            y=76,
            z=0,
            z_half=False,
            direction=NORTHWEST,
            face_on_trigger=True,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=True,
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
        RegularClone( # 2
            npc=npcs.MARRYMORE_BRIGHT_CARD_BUYER_BROWN_GREY_NPC,
            event_script=E0621_MARRYMORE_INN_ELDERLY_GUEST,
            action_script=A0119_SLOW_SEQUENCE_LOOP,
            visible=True,
            x=16,
            y=76,
            z=0,
            z_half=False,
            direction=NORTHWEST),
    ],
    extra_sprite_actions=[
        SpriteAnimationState.DOWN_PIPE,
    ]
)
