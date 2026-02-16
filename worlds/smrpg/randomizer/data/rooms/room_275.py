# R275_MOLEVILLE_MINES_AREA_06_SMALL_ROOM_LEADING_TO_AREA_06
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
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    exits=[
        RoomExit(
            x=4,
            y=115,
            z=0,
            f=EdgeDirection.SOUTHEAST,
            length=1,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM,
            show_message=False,
            dst_x=22,
            dst_y=99,
            dst_z=0,
            dst_z_half=False,
            dst_f=NORTHEAST,
            x_bit_7=False),
        RoomExit(
            x=6,
            y=125,
            z=0,
            f=EdgeDirection.SOUTHEAST,
            length=2,
            height=0,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_2_bit_2=False,
            destination=R277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM,
            show_message=False,
            dst_x=16,
            dst_y=57,
            dst_z=2,
            dst_z_half=False,
            dst_f=SOUTHEAST,
            x_bit_7=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.CROCO_OVERWORLD_NPC,
            initiator=EventInitiator.ANYTHING_EXCEPT_PRESS_A,
            event_script=E3201_MINES_1ST_BOSS_FIGHT,
            action_script=A0734_MINES_CROCO,
            visible=True,
            x=7,
            y=49,
            z=1,
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
            byte3_bit5=True,
            cant_walk_through=True,
            byte3_bit7=True,
            slidable_along_walls=False,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        BattlePackNPC( # 1
            npc=npcs.MAGMITE_NPC,
            initiator=EventInitiator.ANYTHING_EXCEPT_PRESS_A,
            after_battle=PostBattleBehaviour.REMOVE_PERMANENTLY,
            battle_pack=40,
            action_script=A0727_MAGMITES,
            visible=True,
            x=4,
            y=121,
            z=0,
            z_half=False,
            direction=NORTHWEST,
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
        BattlePackClone( # 2
            npc=npcs.MAGMITE_NPC,
            battle_pack=40,
            action_script=A0727_MAGMITES,
            visible=True,
            x=1,
            y=119,
            z=0,
            z_half=False,
            direction=NORTHEAST),
        BattlePackNPC( # 3
            npc=npcs.SPARKY_NPC,
            initiator=EventInitiator.ANYTHING_EXCEPT_PRESS_A,
            after_battle=PostBattleBehaviour.REMOVE_PERMANENTLY_NO_IFRAME_COLLISION,
            battle_pack=38,
            action_script=A0726_MINES_FIREBALLS,
            visible=True,
            x=5,
            y=124,
            z=3,
            z_half=True,
            direction=SOUTHEAST,
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
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3),
    ]
)
