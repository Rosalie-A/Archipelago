# R145_STAR_HILL_AREA_01
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
    music=M0034_STARHILL,
    entrance_event=E2793_STAR_HILL_ENTRANCE_LOADER,
    events=[
        Event(
            event=E2798_STAR_HILL_EXIT_TO_WORLD_MAP,
            x=12,
            y=20,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            height=7,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
        Event(
            event=E2799_STAR_HILL_ENTRANCE_TO_1ST_ROOM,
            x=4,
            y=12,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            height=7,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.EMPTY_NPC_2,
            initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
            event_script=E2794_STAR_HILL_MARRYMORE_EXIT_SIGN,
            action_script=A0015_DO_NOTHING,
            speed=4,
            visible=True,
            x=11,
            y=18,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
            face_on_trigger=False,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=False,
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
            npc=npcs.EMPTY_NPC_2,
            event_script=E2795_STAR_HILL_PROGRESS_SIGN,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=7,
            y=16,
            z=0,
            z_half=False,
            direction=SOUTHWEST),
        RegularClone( # 2
            npc=npcs.EMPTY_NPC_2,
            event_script=E2796_STAR_HILL_MARRYMORE_EXIT_FLOWER,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=12,
            y=29,
            z=0,
            z_half=False,
            direction=SOUTHWEST),
        RegularClone( # 3
            npc=npcs.EMPTY_NPC_2,
            event_script=E2797_STAR_HILL_PROGRESS_FLOWER,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=2,
            y=17,
            z=0,
            z_half=False,
            direction=SOUTHWEST),
    ]
)
