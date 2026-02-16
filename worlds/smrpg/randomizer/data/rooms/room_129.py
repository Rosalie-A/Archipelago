# R129_PIPE_VAULT_AREA_05
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
                buffer_type=BufferType.FOUR_SPRITES_PER_ROW,
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
    music=M0007_PIPEVAULT,
    entrance_event=E0467_PIPE_VAULT_PLATFORMING_ROOM_LOADER,
    events=[
        Event(
            event=E0422_PIPE_VAULT_PLATFORMING_ROOM_ENTRANCE_PIPE,
            x=12,
            y=126,
            z=2,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
        Event(
            event=E0423_PIPE_VAULT_PLATFORMING_ROOM_EXIT_PIPE,
            x=25,
            y=100,
            z=2,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
        Event(
            event=E0492_PIPE_VAULT_PIRANHA_TIMER_1,
            x=21,
            y=108,
            z=2,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=True,
            byte_8_bit_4=False),
        Event(
            event=E0493_PIPE_VAULT_PIRANHA_BIT,
            x=20,
            y=109,
            z=0,
            f=EdgeDirection.SOUTHEAST,
            height=7,
            length=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
        Event(
            event=E0493_PIPE_VAULT_PIRANHA_BIT,
            x=20,
            y=109,
            z=3,
            f=EdgeDirection.SOUTHEAST,
            height=7,
            length=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=True,
            byte_8_bit_4=False),
        Event(
            event=E0493_PIPE_VAULT_PIRANHA_BIT,
            x=21,
            y=107,
            z=0,
            f=EdgeDirection.SOUTHEAST,
            height=7,
            length=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
        Event(
            event=E0493_PIPE_VAULT_PIRANHA_BIT,
            x=21,
            y=107,
            z=3,
            f=EdgeDirection.SOUTHEAST,
            height=7,
            length=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=True,
            byte_8_bit_4=False),
    ],
    objects=[
        BattlePackNPC( # 0
            npc=npcs.PIRANHA_PLANT_NPC,
            initiator=EventInitiator.ANYTHING_EXCEPT_PRESS_A,
            after_battle=PostBattleBehaviour.REMOVE_PERMANENTLY,
            battle_pack=35,
            action_script=A0665_PIPE_VAULT_PIRANHA,
            visible=True,
            x=21,
            y=108,
            z=0,
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
        BattlePackNPC( # 1
            npc=npcs.GOOMBA_NPC_3,
            initiator=EventInitiator.ANYTHING_EXCEPT_PRESS_A,
            after_battle=PostBattleBehaviour.REMOVE_PERMANENTLY,
            battle_pack=7,
            action_script=A0673_PIPE_VAULT_FINAL_ROOM_GOOMBA,
            visible=True,
            x=15,
            y=120,
            z=1,
            z_half=False,
            direction=NORTHEAST,
            face_on_trigger=True,
            cant_enter_doors=False,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=False,
            cant_walk_up_stairs=False,
            cant_walk_under=True,
            cant_pass_walls=True,
            cant_jump_through=False,
            cant_pass_npcs=True,
            byte3_bit5=True,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=False,
            byte7_upper2=3),
        BattlePackClone( # 2
            npc=npcs.GOOMBA_NPC_3,
            battle_pack=7,
            action_script=A0673_PIPE_VAULT_FINAL_ROOM_GOOMBA,
            visible=True,
            x=17,
            y=116,
            z=1,
            z_half=False,
            direction=SOUTHWEST),
        BattlePackClone( # 3
            npc=npcs.GOOMBA_NPC_3,
            battle_pack=7,
            action_script=A0673_PIPE_VAULT_FINAL_ROOM_GOOMBA,
            visible=True,
            x=21,
            y=107,
            z=0,
            z_half=False,
            direction=SOUTHWEST),
    ]
)
