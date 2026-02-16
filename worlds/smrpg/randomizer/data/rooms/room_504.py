# R504_NIMBUS_LAND_DREAM_CUSHION_DREAM_TORTES_ARE_SEASONING_MARIO
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
    music=M0000_CURRENT,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    objects=[
        RegularNPC( # 0
            npc=npcs.TORTE_NPC,
            initiator=EventInitiator.NONE,
            event_script=E0630_MARRYMORE_KITCHEN_CHEF_1,
            action_script=A0983_DREAM_CUSHION_CHEF,
            visible=True,
            x=28,
            y=82,
            z=0,
            z_half=False,
            direction=NORTHEAST,
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
            cant_move_if_in_air=False,
            byte7_upper2=3),
        RegularClone( # 1
            npc=npcs.TORTE_NPC,
            event_script=E0631_MARRYMORE_KITCHEN_CHEF_2,
            action_script=A0984_DREAM_CUSHION_CHEF,
            visible=True,
            x=25,
            y=84,
            z=0,
            z_half=False,
            direction=SOUTHEAST),
        RegularClone( # 2
            npc=npcs.TORTE_NPC,
            event_script=E0631_MARRYMORE_KITCHEN_CHEF_2,
            action_script=A0985_DREAM_CUSHION_CHEF,
            visible=True,
            x=23,
            y=88,
            z=0,
            z_half=False,
            direction=SOUTHWEST),
        RegularNPC( # 3
            npc=npcs.TORTE_NPC_2,
            initiator=EventInitiator.NONE,
            event_script=E0630_MARRYMORE_KITCHEN_CHEF_1,
            action_script=A0982_DREAM_CUSHION_CHEF,
            visible=True,
            x=26,
            y=78,
            z=0,
            z_half=False,
            direction=NORTHEAST,
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
            cant_move_if_in_air=False,
            byte7_upper2=3),
        RegularNPC( # 4
            npc=npcs.TORTE_NPC_2,
            initiator=EventInitiator.NONE,
            event_script=E0631_MARRYMORE_KITCHEN_CHEF_2,
            action_script=A0986_DREAM_CUSHION_CHEF,
            visible=True,
            x=28,
            y=90,
            z=0,
            z_half=False,
            direction=NORTHEAST,
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
            cant_move_if_in_air=False,
            byte7_upper2=3),
        RegularNPC( # 5
            npc=npcs.TORTE_NPC_2,
            initiator=EventInitiator.NONE,
            event_script=E0631_MARRYMORE_KITCHEN_CHEF_2,
            action_script=A0119_SLOW_SEQUENCE_LOOP,
            visible=True,
            x=25,
            y=87,
            z=0,
            z_half=False,
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
            cant_move_if_in_air=False,
            byte7_upper2=3),
    ],
    extra_sprite_actions=[
        SpriteAnimationState.SLEEP,
    ]
)
