# R428_BELOME_TEMPLE_AREA_01_WWARP_TRAMPOLINE
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
    music=M0027_DUNGEONISFULLOFMONSTERS,
    entrance_event=E1778_TEMPLE_GENERIC_PIPE_ROOM_LOADER,
    exits=[
        RoomExit(
            x=16,
            y=118,
            z=4,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS,
            show_message=False,
            dst_x=15,
            dst_y=18,
            dst_z=0,
            dst_z_half=False,
            dst_f=SOUTHWEST,
            x_bit_7=False),
        RoomExit(
            x=27,
            y=111,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM,
            show_message=False,
            dst_x=1,
            dst_y=47,
            dst_z=1,
            dst_z_half=False,
            dst_f=NORTHEAST,
            x_bit_7=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.SHAMAN_NPC,
            initiator=EventInitiator.TOUCH_ANY_SIDE,
            event_script=E1682_TRAMPOLINE_SHAMAN,
            action_script=A0160_SEQUENCE_LOOPING_ON,
            visible=True,
            x=24,
            y=118,
            z=2,
            z_half=False,
            direction=SOUTHWEST,
            face_on_trigger=True,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=True,
            cant_walk_up_stairs=False,
            cant_walk_under=False,
            cant_pass_walls=False,
            cant_jump_through=False,
            cant_pass_npcs=False,
            byte3_bit5=True,
            cant_walk_through=True,
            byte3_bit7=True,
            slidable_along_walls=True,
            cant_move_if_in_air=False,
            byte7_upper2=3),
        RegularNPC( # 1
            npc=npcs.TRAMPOLINE_WARP_NPC,
            initiator=EventInitiator.JUMP_ON,
            event_script=E1683_TEMPLE_EXIT_WARP_TRAMPOLINE,
            action_script=A0161_SEQUENCE_LOOPING_OFF,
            visible=True,
            x=24,
            y=118,
            z=0,
            z_half=False,
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
            byte3_bit5=True,
            cant_walk_through=True,
            byte3_bit7=True,
            slidable_along_walls=True,
            cant_move_if_in_air=False,
            byte7_upper2=3),
    ]
)
