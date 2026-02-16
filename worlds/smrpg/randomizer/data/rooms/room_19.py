# R019_MUSHROOM_KINGDOM_CASTLE_STAIR_ROOM_TO_TOADSTOOLS_ROOM
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
    music=M0002_MUSHROOMKINGDOM,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    exits=[
        RoomExit(
            x=27,
            y=30,
            z=0,
            f=EdgeDirection.SOUTHEAST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL,
            show_message=False,
            dst_x=4,
            dst_y=23,
            dst_z=2,
            dst_z_half=False,
            dst_f=SOUTHEAST,
            x_bit_7=False),
        RoomExit(
            x=26,
            y=19,
            z=3,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R032_MUSHROOM_KINGDOM_CASTLE_ENTRANCE_TO_TOADSTOOLS_ROOM,
            show_message=False,
            dst_x=11,
            dst_y=98,
            dst_z=1,
            dst_z_half=False,
            dst_f=NORTHEAST,
            x_bit_7=False),
    ])
