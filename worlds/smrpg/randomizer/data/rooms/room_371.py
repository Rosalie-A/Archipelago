# R371_NIMBUS_LAND_FALL_FROM_PLATFORM_1ST
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
                buffer_type=BufferType.FOUR_SPRITES_PER_ROW,
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
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=[
        Event(
            event=E3764_NIMBUS_FIRST_FALL_ROOM_LOAD_2ND_ROOM,
            x=27,
            y=30,
            z=2,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=True,
            byte_8_bit_4=False),
        Event(
            event=E3764_NIMBUS_FIRST_FALL_ROOM_LOAD_2ND_ROOM,
            x=27,
            y=31,
            z=2,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=True,
            byte_8_bit_4=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.EMPTY_NPC_3,
            initiator=EventInitiator.NONE,
            event_script=E0346_TOADSTOOLS_ROOM_ITEM,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=27,
            y=67,
            z=4,
            z_half=False,
            direction=NORTHEAST,
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
            cant_walk_through=False,
            byte3_bit7=False,
            slidable_along_walls=False,
            cant_move_if_in_air=False,
            byte7_upper2=3),
    ],
    extra_sprite_actions=[
        SpriteAnimationState.PRAISE_FRONT,
    ]
)
