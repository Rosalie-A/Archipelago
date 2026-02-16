# R123_PIPE_VAULT_AREA_01
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
                buffer_type=BufferType.THREE_SPRITES_PER_ROW,
                main_buffer_space=BufferSpace.BYTES_0,
                index_in_main_buffer=True
            )
        ],
        full_palette_buffer=True
    ),
    music=M0007_PIPEVAULT,
    entrance_event=E0435_PIPE_VAULT_ROOM_1_LOADER,
    events=[
        Event(
            event=E0415_PIPE_VAULT_ROOM_1_EXIT,
            x=11,
            y=7,
            z=1,
            f=EdgeDirection.SOUTHEAST,
            height=0,
            length=1,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.EMPTY_NPC_3,
            initiator=EventInitiator.NONE,
            event_script=E0499_PIPE_VAULT_ENTRANCE_TRAMPOLINE,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=2,
            y=26,
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
            cant_walk_through=False,
            byte3_bit7=False,
            slidable_along_walls=False,
            cant_move_if_in_air=False,
            byte7_upper2=3),
        RegularNPC( # 1
            npc=npcs.FIREBALL_SURFACE_FROM_LAVA_NPC,
            initiator=EventInitiator.ANYTHING_EXCEPT_PRESS_A,
            event_script=E0436_PIPE_VAULT_FIREBALL_1,
            action_script=A0509_PIPE_VAULT_FIREBALL,
            visible=True,
            x=5,
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
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=False,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        RegularClone( # 2
            npc=npcs.FIREBALL_SURFACE_FROM_LAVA_NPC,
            event_script=E0437_PIPE_VAULT_FIREBALL_2,
            action_script=A0508_PIPE_VAULT_FIREBALL,
            visible=True,
            x=6,
            y=17,
            z=0,
            z_half=False,
            direction=SOUTHWEST),
        RegularClone( # 3
            npc=npcs.FIREBALL_SURFACE_FROM_LAVA_NPC,
            event_script=E0438_PIPE_VAULT_FIREBALL_3,
            action_script=A0509_PIPE_VAULT_FIREBALL,
            visible=True,
            x=8,
            y=14,
            z=0,
            z_half=False,
            direction=SOUTHWEST),
        RegularClone( # 4
            npc=npcs.FIREBALL_SURFACE_FROM_LAVA_NPC,
            event_script=E0439_PIPE_VAULT_FIREBALL_4,
            action_script=A0508_PIPE_VAULT_FIREBALL,
            visible=True,
            x=9,
            y=11,
            z=0,
            z_half=False,
            direction=SOUTHWEST),
        RegularNPC( # 5
            npc=npcs.TRAMPOLINE_JUMP_NPC,
            initiator=EventInitiator.JUMP_ON,
            event_script=E0499_PIPE_VAULT_ENTRANCE_TRAMPOLINE,
            action_script=A0015_DO_NOTHING,
            visible=True,
            x=2,
            y=26,
            z=1,
            z_half=False,
            direction=SOUTHWEST,
            face_on_trigger=False,
            cant_enter_doors=True,
            byte2_bit5=False,
            set_sequence_playback=True,
            cant_float=True,
            cant_walk_up_stairs=False,
            cant_walk_under=True,
            cant_pass_walls=True,
            cant_jump_through=False,
            cant_pass_npcs=True,
            byte3_bit5=True,
            cant_walk_through=True,
            byte3_bit7=True,
            slidable_along_walls=False,
            cant_move_if_in_air=False,
            byte7_upper2=3),
    ]
)
