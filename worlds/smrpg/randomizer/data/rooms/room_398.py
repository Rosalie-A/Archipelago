# R398_MONSTRO_TOWN_WEAPON_AND_ARMOR_SHOP
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
    music=M0051_MONSTROTOWN,
    entrance_event=E2051_MONSTRO_SHOP_LOADER,
    exits=[
        RoomExit(
            x=13,
            y=24,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R324_MONSTRO_TOWN_OUTSIDE,
            show_message=False,
            dst_x=14,
            dst_y=68,
            dst_z=4,
            dst_z_half=False,
            dst_f=SOUTHWEST,
            x_bit_7=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.GOOMBETTE_LOWER_NPC,
            initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
            event_script=E2053_MONSTRO_GOOMBETTE_SHOP,
            action_script=A0878_MONSTRO_GOOMBETTE,
            visible=False,
            x=13,
            y=17,
            z=1,
            z_half=False,
            direction=SOUTHWEST,
            face_on_trigger=False,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=False,
            cant_walk_up_stairs=False,
            cant_walk_under=False,
            cant_pass_walls=True,
            cant_jump_through=False,
            cant_pass_npcs=False,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        RegularClone( # 1
            npc=npcs.GOOMBETTE_LOWER_NPC,
            event_script=E2053_MONSTRO_GOOMBETTE_SHOP,
            action_script=A0879_MONSTRO_GOOMBETTE,
            visible=False,
            x=14,
            y=18,
            z=1,
            z_half=False,
            direction=SOUTHWEST),
        RegularClone( # 2
            npc=npcs.GOOMBETTE_LOWER_NPC,
            event_script=E2053_MONSTRO_GOOMBETTE_SHOP,
            action_script=A0878_MONSTRO_GOOMBETTE,
            visible=False,
            x=14,
            y=19,
            z=1,
            z_half=False,
            direction=SOUTHWEST),
        RegularNPC( # 3
            npc=npcs.GOOMBA_NPC_2,
            initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
            event_script=E2054_MONSTRO_MAIN_SHOP,
            action_script=A0000_DO_NOTHING,
            visible=True,
            x=15,
            y=19,
            z=0,
            z_half=True,
            direction=SOUTHWEST,
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
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        RegularNPC( # 4
            npc=npcs.EMPTY_NPC,
            initiator=EventInitiator.PRESS_A_FROM_FRONT,
            event_script=E2054_MONSTRO_MAIN_SHOP,
            action_script=A0015_DO_NOTHING,
            speed=3,
            visible=True,
            x=15,
            y=21,
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
    ]
)
