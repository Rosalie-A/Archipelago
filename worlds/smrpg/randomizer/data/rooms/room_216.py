# R216_SEASIDE_TOWN_DURING_YARIDOVICH_MUSHROOM_BOY_SHOP_MIDDLE
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
    music=M0015_HERE_SSOMEWEAPONS,
    entrance_event=E1128_SEASIDE_OCCUPIED_MUSHROOM_BOY_SHOP_LOADER,
    exits=[
        RoomExit(
            x=23,
            y=41,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
            show_message=False,
            dst_x=24,
            dst_y=42,
            dst_z=1,
            dst_z_half=False,
            dst_f=SOUTHWEST,
            x_bit_7=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.SEASIDE_TOWN_FAKE_GREEN_NPC,
            initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
            event_script=E1135_SEASIDE_OCCUPIED_MUSHROOM_BOY_SHOP_OCCUPANT_1,
            action_script=A0147_SEASIDE_HENCHMAN,
            visible=True,
            x=24,
            y=39,
            z=0,
            z_half=False,
            direction=NORTHEAST,
            face_on_trigger=True,
            cant_enter_doors=True,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=True,
            cant_walk_up_stairs=True,
            cant_walk_under=True,
            cant_pass_walls=True,
            cant_jump_through=False,
            cant_pass_npcs=False,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        RegularNPC( # 1
            npc=npcs.SEASIDE_TOWN_FAKE_GREEN_NPC,
            initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
            event_script=E1136_SEASIDE_OCCUPIED_MUSHROOM_BOY_SHOP_OCCUPANT_2,
            action_script=A0147_SEASIDE_HENCHMAN,
            visible=True,
            x=24,
            y=35,
            z=0,
            z_half=False,
            direction=SOUTHWEST,
            face_on_trigger=True,
            cant_enter_doors=True,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=True,
            cant_walk_up_stairs=True,
            cant_walk_under=True,
            cant_pass_walls=True,
            cant_jump_through=False,
            cant_pass_npcs=False,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3),
    ]
)
