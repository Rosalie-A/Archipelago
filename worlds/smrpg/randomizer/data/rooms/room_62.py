# R062_KERO_SEWERS_AREA_01_WATER_ROOM_WSAVE
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
                buffer_type=BufferType.THREE_SPRITES_PER_ROW,
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
        full_palette_buffer=False
    ),
    music=M0027_DUNGEONISFULLOFMONSTERS,
    entrance_event=E3135_SEWERS_GENERIC_LOADER,
    events=[
        Event(
            event=E3163_SEWERS_TUTORIAL_ROOM_EXIT_TO_EXTERIOR,
            x=5,
            y=90,
            z=5,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
        Event(
            event=E3164_SEWERS_TUTORIAL_ROOM_PIPE_TO_FIRST_WATER_ROOM,
            x=14,
            y=90,
            z=5,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.SAVE_POINT_NPC_3,
            initiator=EventInitiator.JUMP_ON,
            event_script=E0080_SAVE_BLOCK_SUBROUTINE,
            action_script=A0120_EMBEDDED_ROUTINE,
            visible=True,
            x=6,
            y=87,
            z=4,
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
            cant_pass_npcs=True,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=False,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        RegularNPC( # 1
            npc=npcs.YELLOW_LETTER_NPC,
            initiator=EventInitiator.PRESS_A_FROM_FRONT,
            event_script=E3130_SEWER_TUTORIAL_NOTE,
            action_script=A0919_SHIP_FIRST_NOTE,
            visible=True,
            x=12,
            y=88,
            z=4,
            z_half=True,
            direction=SOUTHEAST,
            face_on_trigger=False,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=False,
            cant_float=False,
            cant_walk_up_stairs=False,
            cant_walk_under=False,
            cant_pass_walls=False,
            cant_jump_through=False,
            cant_pass_npcs=True,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=False,
            byte7_upper2=3),
    ],
    extra_sprite_actions=[
        SpriteAnimationState.DOWN_PIPE,
        SpriteAnimationState.SWIM,
    ]
)
