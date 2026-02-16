# R466_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1C_WORD_PROBLEM
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
    music=M0066_BOWSER_SCASTLE_2NDTIME,
    entrance_event=E3364_KEEP_LOGIC_GAME_LOADER,
    events=[
        Event(
            event=E3350_KEEP_ALL_DOOR_PATHS_EXIT_TO_REWARD_ROOM,
            x=17,
            y=87,
            z=0,
            f=EdgeDirection.SOUTHWEST,
            height=6,
            length=2,
            nw_se_edge_active=True,
            ne_sw_edge_active=False,
            byte_8_bit_4=False),
    ],
    objects=[
        RegularNPC( # 0
            npc=npcs.DR_TOPPER_GREEN_NPC,
            initiator=EventInitiator.PRESS_A_FROM_FRONT,
            event_script=E3365_KEEP_LOGIC_GAME_FINALIZE_ANSWER,
            action_script=A0003_SEQUENCE_LOOPING_ON,
            visible=True,
            x=17,
            y=89,
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
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        RegularNPC( # 1
            npc=npcs.LI_XX_L_BOO_NPC,
            initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
            event_script=E3366_KEEP_LOGIC_GAME_BOO,
            action_script=A0003_SEQUENCE_LOOPING_ON,
            visible=True,
            x=12,
            y=93,
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
            cant_pass_walls=True,
            cant_jump_through=False,
            cant_pass_npcs=True,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        RegularClone( # 2
            npc=npcs.VOMER_NPC,
            event_script=E3368_KEEP_LOGIC_GAME_BONES,
            action_script=A0003_SEQUENCE_LOOPING_ON,
            visible=True,
            x=14,
            y=89,
            z=0,
            z_half=False,
            direction=SOUTHEAST),
        RegularNPC( # 3
            npc=npcs.GOOMBA_NPC_2,
            initiator=EventInitiator.PRESS_A_FROM_ANY_SIDE,
            event_script=E3367_KEEP_LOGIC_GAME_GOO,
            action_script=A0003_SEQUENCE_LOOPING_ON,
            visible=True,
            x=13,
            y=91,
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
            cant_pass_walls=True,
            cant_jump_through=False,
            cant_pass_npcs=True,
            byte3_bit5=False,
            cant_walk_through=True,
            byte3_bit7=False,
            slidable_along_walls=True,
            cant_move_if_in_air=True,
            byte7_upper2=3),
        RegularClone( # 4
            npc=npcs.GOBY_NPC,
            event_script=E3369_KEEP_LOGIC_GAME_KIPP,
            action_script=A0003_SEQUENCE_LOOPING_ON,
            visible=True,
            x=15,
            y=87,
            z=0,
            z_half=False,
            direction=SOUTHEAST),
    ],
    extra_sprite_actions=[
        SpriteAnimationState.MUTE,
    ]
)
