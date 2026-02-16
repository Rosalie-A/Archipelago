# R362_VOLCANO_AREA_07_STOMPING_CORKPEDITE
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
    music=M0062_BARRELVOLCANO,
    entrance_event=E3336_CORKPEDITE_ROOM_LOADER,
    exits=[
        RoomExit(
            x=1,
            y=24,
            z=5,
            f=EdgeDirection.SOUTHEAST,
            length=2,
            height=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R356_VOLCANO_AREA_08,
            show_message=False,
            dst_x=17,
            dst_y=23,
            dst_z=0,
            dst_z_half=False,
            dst_f=NORTHWEST,
            x_bit_7=False),
        RoomExit(
            x=6,
            y=27,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R385_VOLCANO_AREA_06,
            show_message=False,
            dst_x=26,
            dst_y=83,
            dst_z=0,
            dst_z_half=False,
            dst_f=NORTHEAST,
            x_bit_7=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.CORKPEDITE_NPC,
            initiator=EventInitiator.ANYTHING_EXCEPT_PRESS_A,
            event_script=E3335_CORKPEDITE_COLLISION,
            action_script=A0934_CORKPEDITE,
            visible=True,
            x=6,
            y=26,
            z=5,
            z_half=False,
            direction=SOUTHEAST,
            face_on_trigger=False,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=False,
            cant_float=False,
            cant_walk_up_stairs=False,
            cant_walk_under=False,
            cant_pass_walls=True,
            cant_jump_through=False,
            cant_pass_npcs=True,
            byte3_bit5=True,
            cant_walk_through=True,
            byte3_bit7=True,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        RegularNPC( # 1
            npc=npcs.OERLIKON_NPC,
            initiator=EventInitiator.ANYTHING_EXCEPT_PRESS_A,
            event_script=E3318_SET_OERLIKON_PACK,
            action_script=A0727_MAGMITES,
            visible=False,
            x=6,
            y=25,
            z=5,
            z_half=False,
            direction=SOUTHEAST,
            face_on_trigger=False,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=True,
            cant_walk_up_stairs=False,
            cant_walk_under=False,
            cant_pass_walls=True,
            cant_jump_through=False,
            cant_pass_npcs=True,
            byte3_bit5=True,
            cant_walk_through=True,
            byte3_bit7=True,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        RegularClone( # 2
            npc=npcs.OERLIKON_NPC,
            event_script=E3318_SET_OERLIKON_PACK,
            action_script=A0727_MAGMITES,
            visible=False,
            x=6,
            y=25,
            z=5,
            z_half=False,
            direction=SOUTHEAST),
        RegularClone( # 3
            npc=npcs.OERLIKON_NPC,
            event_script=E3318_SET_OERLIKON_PACK,
            action_script=A0727_MAGMITES,
            visible=False,
            x=6,
            y=25,
            z=5,
            z_half=False,
            direction=SOUTHEAST),
        RegularClone( # 4
            npc=npcs.OERLIKON_NPC,
            event_script=E3318_SET_OERLIKON_PACK,
            action_script=A0727_MAGMITES,
            visible=False,
            x=6,
            y=25,
            z=5,
            z_half=False,
            direction=SOUTHEAST),
    ]
)
