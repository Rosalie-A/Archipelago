# R155_MARRYMORE_CHAPEL_KITCHEN
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
        ally_sprite_buffer_size=2,
        allow_extra_sprite_buffer=False,
        extra_sprite_buffer_size=0,
        buffers = [
            Buffer(
                buffer_type=BufferType.THREE_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            ),
            Buffer(
                buffer_type=BufferType.FOUR_SPRITES_PER_ROW,
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
    music=M0039_MARRYMORE,
    entrance_event=E0628_MARRYMORE_KITCHEN_LOADER,
    exits=[
        RoomExit(
            x=4,
            y=13,
            z=1,
            f=EdgeDirection.SOUTHEAST,
            length=1,
            height=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=True,
            byte_2_bit_2=False,
            destination=R152_MARRYMORE_CHAPEL_MAIN_HALL,
            show_message=False,
            dst_x=10,
            dst_y=41,
            dst_z=1,
            dst_z_half=True,
            dst_f=NORTHWEST,
            x_bit_7=False),
        RoomExit(
            x=9,
            y=15,
            z=1,
            f=EdgeDirection.SOUTHEAST,
            length=1,
            height=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=True,
            byte_2_bit_2=False,
            destination=R156_MARRYMORE_CHAPEL_KITCHEN_NO_SPRITESEXITS_UNUSED,
            show_message=False,
            dst_x=2,
            dst_y=91,
            dst_z=1,
            dst_z_half=True,
            dst_f=NORTHEAST,
            x_bit_7=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.BUNDT_OBJECT_NPC,
            initiator=EventInitiator.JUMP_ON,
            event_script=E0256_RETURN,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=4,
            y=23,
            z=1,
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
            slidable_along_walls=False,
            cant_move_if_in_air=False,
            byte7_upper2=3),
        RegularNPC( # 1
            npc=npcs.TORTE_NPC,
            initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
            event_script=E0630_MARRYMORE_KITCHEN_CHEF_1,
            action_script=A0330_MARRYMORE_HEAD_CHEF,
            visible=True,
            x=3,
            y=17,
            z=0,
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
        RegularNPC( # 2
            npc=npcs.TORTE_NPC,
            initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
            event_script=E0631_MARRYMORE_KITCHEN_CHEF_2,
            action_script=A0331_MARRYMORE_2ND_CHEF,
            visible=True,
            x=4,
            y=20,
            z=0,
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
    ]
)
