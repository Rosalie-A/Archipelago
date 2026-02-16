# R152_MARRYMORE_CHAPEL_MAIN_HALL
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
    music=M0039_MARRYMORE,
    entrance_event=E0729_SEVERAL_MARRYMORE_ROOM_LOADERS,
    events=[
        Event(
            event=E0633_MARRYMORE_CHAPEL_LOBBY_EXIT_TO_EXTERIOR,
            x=3,
            y=37,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            height=2,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=True,
            byte_8_bit_4=False),
        Event(
            event=E0673_MARRYMORE_CHAPEL_LOBBY_EXIT_TO_ANTECHAMBER,
            x=7,
            y=25,
            z=4,
            f=EdgeDirection.SOUTHWEST,
            height=0,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
    ],
    exits=[
        RoomExit(
            x=11,
            y=42,
            z=0,
            f=EdgeDirection.SOUTHEAST,
            length=1,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=True,
            byte_2_bit_2=False,
            destination=R155_MARRYMORE_CHAPEL_KITCHEN,
            show_message=False,
            dst_x=5,
            dst_y=14,
            dst_z=0,
            dst_z_half=True,
            dst_f=SOUTHEAST,
            x_bit_7=False),
    ])
