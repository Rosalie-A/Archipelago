# R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM
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
        extra_sprite_buffer_size=2,
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
                buffer_type=BufferType.THREE_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            )
        ],
        full_palette_buffer=True
    ),
    music=M0000_CURRENT,
    entrance_event=E0786_MINES_LONG_ROOM_IN_MINIBOSS_PATH_LOADER,
    exits=[
        RoomExit(
            x=10,
            y=30,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE,
            show_message=False,
            dst_x=10,
            dst_y=49,
            dst_z=0,
            dst_z_half=False,
            dst_f=SOUTHWEST,
            x_bit_7=False),
        RoomExit(
            x=2,
            y=17,
            z=0,
            f=EdgeDirection.SOUTHEAST,
            length=1,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R279_MOLEVILLE_MINES_AREA_08_CROCOS_BOMBED_ROOM,
            show_message=False,
            dst_x=18,
            dst_y=121,
            dst_z=0,
            dst_z_half=False,
            dst_f=NORTHWEST,
            x_bit_7=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.CROCO_OVERWORLD_NPC,
            initiator=EventInitiator.ANYTHING_EXCEPT_PRESS_A,
            event_script=E3201_MINES_1ST_BOSS_FIGHT,
            action_script=A0731_MINES_CROCO,
            visible=True,
            x=4,
            y=20,
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
            cant_pass_npcs=True,
            byte3_bit5=True,
            cant_walk_through=True,
            byte3_bit7=True,
            slidable_along_walls=False,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        RegularNPC( # 1
            npc=npcs.CROOK_NPC,
            initiator=EventInitiator.ANYTHING_EXCEPT_PRESS_A,
            event_script=E3193_MINES_RIGHT_HENCHMAN,
            action_script=A0618_MINES_RIGHT_CROOK,
            visible=True,
            x=9,
            y=20,
            z=0,
            z_half=False,
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
            byte3_bit5=True,
            cant_walk_through=True,
            byte3_bit7=True,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        BattlePackNPC( # 2
            npc=npcs.MAGMITE_NPC,
            initiator=EventInitiator.ANYTHING_EXCEPT_PRESS_A,
            after_battle=PostBattleBehaviour.REMOVE_PERMANENTLY,
            battle_pack=40,
            action_script=A0727_MAGMITES,
            visible=True,
            x=13,
            y=25,
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
            cant_pass_walls=True,
            cant_jump_through=False,
            cant_pass_npcs=True,
            byte3_bit5=True,
            cant_walk_through=True,
            byte3_bit7=True,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        BattlePackClone( # 3
            npc=npcs.MAGMITE_NPC,
            battle_pack=40,
            action_script=A0727_MAGMITES,
            visible=True,
            x=8,
            y=17,
            z=0,
            z_half=False,
            direction=SOUTHEAST),
    ]
)
