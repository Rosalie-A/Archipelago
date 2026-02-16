# R120_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_DURING_VALENTINA
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
                buffer_type=BufferType.FOUR_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            )
        ],
        full_palette_buffer=True
    ),
    music=M0000_CURRENT,
    entrance_event=E3729_NIMBUS_CASTLE_OCCUPIED_THRONE_ROOM_LOADER,
    events=[
        Event(
            event=E3739_NIMBUS_CASTLE_THRONE_ROOM_EXIT_TO_ANTECHAMBER,
            x=1,
            y=64,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            height=0,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
    ],
    exits=[
        RoomExit(
            x=7,
            y=46,
            z=2,
            f=EdgeDirection.SOUTHEAST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R411_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_1ST,
            show_message=False,
            dst_x=12,
            dst_y=123,
            dst_z=0,
            dst_z_half=False,
            dst_f=NORTHWEST,
            x_bit_7=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.VALENTINA_STATUE_NPC,
            initiator=EventInitiator.NONE,
            event_script=E0470_GREEN_YOSHI,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=2,
            y=60,
            z=1,
            z_half=False,
            direction=SOUTHEAST,
            face_on_trigger=True,
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
            slidable_along_walls=False,
            cant_move_if_in_air=False,
            byte7_upper2=3),
        RegularNPC( # 1
            npc=npcs.VALENTINA_STATUE_NPC,
            initiator=EventInitiator.NONE,
            event_script=E0470_GREEN_YOSHI,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=3,
            y=63,
            z=1,
            z_half=False,
            direction=NORTHWEST,
            face_on_trigger=True,
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
            slidable_along_walls=False,
            cant_move_if_in_air=False,
            byte7_upper2=3),
    ]
)
