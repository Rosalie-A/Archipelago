from django.core.management.base import BaseCommand
import re
from pathlib import Path
from randomizer.data.rooms.rooms import rooms
from randomizer.types.battles.ids.pack_ids import *
from randomizer.types.overworld_scripts.constants.music_names import *
from randomizer.types.overworld_scripts.event_scripts.ids.script_ids import *
from randomizer.types.overworld_scripts.action_scripts.ids.script_ids import *
from randomizer.types.overworld_scripts.constants.overworld_names import *
from randomizer.types.overworld_scripts.constants.room_names import *
from randomizer.management.disassembler_common import (
    writeline,
)

DIRECTIONS = [
    "EAST",
    "SOUTHEAST",
    "SOUTH",
    "SOUTHWEST",
    "WEST",
    "NORTHWEST",
    "NORTH",
    "NORTHEAST",
]
AREA_OBJECTS = [
    "NPC_0",
    "NPC_1",
    "NPC_2",
    "NPC_3",
    "NPC_4",
    "NPC_5",
    "NPC_6",
    "NPC_7",
    "NPC_8",
    "NPC_9",
    "NPC_10",
    "NPC_11",
    "NPC_12",
    "NPC_13",
    "NPC_14",
    "NPC_15",
    "NPC_16",
    "NPC_17",
    "NPC_18",
    "NPC_19",
    "NPC_20",
    "NPC_21",
    "NPC_22",
    "NPC_23",
    "NPC_24",
    "NPC_25",
    "NPC_26",
    "NPC_27",
]

BUFFER_TYPES = [
    "_3_SPRITES_PER_ROW",
    "_4_SPRITES_PER_ROW",
    "TREASURE_CHEST",
    "EMPTY_TREASURE_CHEST",
    "COINS",
    "EMPTY_1",
    "EMPTY_2",
    "EMPTY_3",
]
BUFFER_SIZES = [
    "_0_BYTES",
    "_256_BYTES",
    "_512_BYTES",
    "_768_BYTES",
    "_1024_BYTES",
    "_1280_BYTES",
    "_1536_BYTES",
    "_1792_BYTES",
]
EVENT_INITIATORS = [
    "NONE",
    "PRESS_A_FROM_ANY_SIDE",
    "PRESS_A_FROM_FRONT",
    "ANYTHING_EXCEPT_TOUCH_SIDE",
    "PRESS_A_OR_TOUCH_ANY_SIDE",
    "PRESS_A_OR_TOUCH_FRONT",
    "DO_ANYTHING",
    "HIT_FROM_BELOW",
    "JUMP_ON",
    "JUMP_ON_OR_HIT_FROM_BELOW",
    "TOUCH_ANY_SIDE",
    "TOUCH_FROM_FRONT",
    "ANYTHING_EXCEPT_PRESS_A",
]
POST_BATTLE_BEHAVIOURS = [
    "REMOVE_PERMANENTLY",
    "REMOVE_UNTIL_RELOAD",
    "DO_NOT_REMOVE",
    "REMOVE_PERMANENTLY_NO_IFRAME_COLLISION",
    "REMOVE_UNTIL_RELOAD_NO_IFRAME_COLLISION",
    "",
    "",
    "",
    "UNKNOWN",
]
EDGE_DIRECTIONS = [
    "SOUTHEAST",
    "SOUTHWEST",
]
EXIT_TYPES = [
    "ROOM",
    "MAP_LOCATION",
]
SHADOW_SIZES = ["OVAL_SMALL", "OVAL_MED", "OVAL_BIG", "BLOCK"]
VRAM_SIZES = [
    "DIR0_SWSE_NWNE",
    "DIR1_SWSE_NWNE_S",
    "DIR2_SWSE",
    "DIR3_SWSE_NWNE",
    "DIR4_ALL_DIRECTIONS",
    "DIR5_UNKNOWN",
    "DIR6_UNKNOWN",
    "DIR7_ALL_DIRECTIONS",
]

searchable_vars = globals()

def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] == obj]

def get_var_name_string(id, prefix):
    candidates = namestr(id, searchable_vars)
    r = re.compile("^%s.*" % prefix)
    newlist = list(filter(r.match, candidates))
    if len(newlist) != 1:
        print("%s %r" % (prefix, id))
        raise Exception(newlist)
    return newlist[0]

def get_event_name(id):
    return get_var_name_string(id, "E")

def get_action_name(id):
    return get_var_name_string(id, "A")

def get_music_name(id):
    return get_var_name_string(id, "M")

def get_overworld_name(id):
    return get_var_name_string(id, "OW")

def get_room_name(id):
    return get_var_name_string(id, "R")

def get_pack_name(id):
    return get_var_name_string(id, "PACK")

class Command(BaseCommand):
    def handle(self, *args, **options):
        for i, room in enumerate(rooms[:510]):
            print(get_room_name(i))
            path = (
                "L:/PROJECTS/smrpg_web_randomizer2/randomizer/entities/rooms/rooms/room_%i"
                % i
            )
            Path(path).mkdir(parents=True, exist_ok=True)

            # partition
            partition_output = (
                "from randomizer.entities.rooms.partition_imports import *"
            )
            partition_output += """\n\nbuffers: list[Buffer] = ["""
            partition_output += "\n    Buffer("
            partition_output += (
                "\n        buffer_type = BufferType.%s,"
                % BUFFER_TYPES[room.partition.buffers[0].buffer_type]
            )
            partition_output += (
                "\n        main_buffer_space = BufferSpace.%s,"
                % BUFFER_SIZES[room.partition.buffers[0].main_buffer_space]
            )
            partition_output += "\n        index_in_main_buffer = %s" % (
                "True" if room.partition.buffers[0].index_in_main_buffer else "False"
            )
            partition_output += "\n    ),"
            partition_output += "\n    Buffer("
            partition_output += (
                "\n        buffer_type = BufferType.%s,"
                % BUFFER_TYPES[room.partition.buffers[1].buffer_type]
            )
            partition_output += (
                "\n        main_buffer_space = BufferSpace.%s,"
                % BUFFER_SIZES[room.partition.buffers[1].main_buffer_space]
            )
            partition_output += "\n        index_in_main_buffer = %s" % (
                "True" if room.partition.buffers[1].index_in_main_buffer else "False"
            )
            partition_output += "\n    ),"
            partition_output += "\n    Buffer("
            partition_output += (
                "\n        buffer_type = BufferType.%s,"
                % BUFFER_TYPES[room.partition.buffers[2].buffer_type]
            )
            partition_output += (
                "\n        main_buffer_space = BufferSpace.%s,"
                % BUFFER_SIZES[room.partition.buffers[2].main_buffer_space]
            )
            partition_output += "\n        index_in_main_buffer = %s" % (
                "True" if room.partition.buffers[2].index_in_main_buffer else "False"
            )
            partition_output += "\n    ),"
            partition_output += """]"""
            partition_output += "\n\npartition = Partition("
            partition_output += (
                "\n    ally_sprite_buffer_size=%i,"
                % room.partition.ally_sprite_buffer_size
            )
            partition_output += "\n    allow_extra_sprite_buffer=%s," % (
                "True" if room.partition.allow_extra_sprite_buffer else "False"
            )
            partition_output += (
                "\n    extra_sprite_buffer_size=%i,"
                % room.partition.extra_sprite_buffer_size
            )
            partition_output += "\n    buffers=buffers,"
            partition_output += "\n    full_palette_buffer=%s," % (
                "True" if room.partition.full_palette_buffer else "False"
            )
            partition_output += "\n)"
            partition_file = open("%s/room_%i_partition.py" % (path, i), "w")
            writeline(partition_file, partition_output)
            partition_file.close()

            # exits
            if len(room.exit_fields) > 0:
                exit_output = "from randomizer.entities.rooms.exit_imports import *"
                exit_output += "\n\nexits = ["
                for exit in room.exit_fields:
                    if exit.destination_type == 0:  # room
                        exit_output += "\n    RoomExit("
                    elif exit.destination_type == 1:  # ow
                        exit_output += "\n    MapExit("
                    exit_output += "\n        x=%i," % exit.x
                    exit_output += "\n        y=%i," % exit.y
                    exit_output += "\n        z=%i," % exit.z
                    exit_output += (
                        "\n        f=EdgeDirection.%s," % EDGE_DIRECTIONS[exit.f]
                    )
                    exit_output += "\n        length=%i," % exit.length
                    exit_output += "\n        height=%i," % exit.height
                    exit_output += "\n        nw_se_edge_active = %s," % (
                        "True" if exit.nw_se_edge_active else "False"
                    )
                    exit_output += "\n        ne_sw_edge_active = %s," % (
                        "True" if exit.ne_sw_edge_active else "False"
                    )
                    exit_output += "\n        byte_2_bit_2 = %s," % (
                        "True" if exit.byte_2_bit_2 else "False"
                    )
                    if exit.destination_type == 0:  # room
                        exit_output += "\n        destination = %s," % get_room_name(
                            exit.destination
                        )
                    elif exit.destination_type == 1:  # ow
                        exit_output += (
                            "\n        destination = %s,"
                            % get_overworld_name(exit.destination)
                        )
                    exit_output += "\n        show_message = %s," % (
                        "True" if exit.show_message else "False"
                    )
                    if exit.destination_type == 0:  # room
                        exit_output += (
                            "\n        dst_x = %i," % exit.destination_props.x
                        )
                        exit_output += (
                            "\n        dst_y = %i," % exit.destination_props.y
                        )
                        exit_output += (
                            "\n        dst_z = %i," % exit.destination_props.z
                        )
                        exit_output += "\n        dst_z_half = %s," % (
                            "True" if exit.destination_props.z_half else "False"
                        )
                        exit_output += (
                            "\n    dst_f = %s," % DIRECTIONS[exit.destination_props.f]
                        )
                        exit_output += "\n        x_bit_7 = %s," % (
                            "True" if exit.destination_props.x_bit_7 else "False"
                        )
                    elif exit.destination_type == 1:  # ow
                        exit_output += "\n        byte_2_bit_1 = %s," % (
                            "True" if exit.byte_2_bit_1 else "False"
                        )
                        exit_output += "\n        byte_2_bit_0 = %s," % (
                            "True" if exit.byte_2_bit_1 else "False"
                        )
                    exit_output += "\n    ),"
                exit_output += "\n]"
                exit_file = open("%s/room_%i_exits.py" % (path, i), "w")
                writeline(exit_file, exit_output)
                exit_file.close()

            # event tiles
            if len(room.event_tiles) > 0:
                event_output = "from randomizer.entities.rooms.event_imports import *"
                event_output += "\n\nevents = ["
                for event in room.event_tiles:
                    event_output += "\n    Event("
                    event_output += "\n        event=%s," % get_event_name(event.event)
                    event_output += "\n        x=%i," % event.x
                    event_output += "\n        y=%i," % event.y
                    event_output += "\n        z=%i," % event.z
                    event_output += (
                        "\n        f=EdgeDirection.%s," % EDGE_DIRECTIONS[event.f]
                    )
                    event_output += "\n        length=%i," % event.length
                    event_output += "\n        height=%i," % event.height
                    event_output += "\n        nw_se_edge_active = %s," % (
                        "True" if event.nw_se_edge_active else "False"
                    )
                    event_output += "\n        ne_sw_edge_active = %s," % (
                        "True" if event.ne_sw_edge_active else "False"
                    )
                    event_output += "\n        byte_8_bit_4 = %s," % (
                        "True" if event.byte_8_bit_4 else "False"
                    )
                    event_output += "\n    ),"
                event_output += "\n]"
                event_file = open("%s/room_%i_events.py" % (path, i), "w")
                writeline(event_file, event_output)
                event_file.close()

            # objects
            if len(room.objects) > 0:
                objects_output = (
                    "from randomizer.entities.rooms.object_imports import *"
                )
                objects_output += "\n\nobjects = ["
                for i_, o in enumerate(room.objects):
                    npc_type = o.__class__.__name__
                    npc_name = o.model.occupant.__name__
                    objects_output += "\n    # %s" % AREA_OBJECTS[i_]
                    objects_output += "\n    %s(" % npc_type
                    objects_output += "\n        occupant=%s," % npc_name
                    if npc_type in ["RegularNPC", "ChestNPC", "BattlePackNPC"]:
                        objects_output += (
                            "\n        initiator=EventInitiator.%s,"
                            % EVENT_INITIATORS[o.initiator]
                        )
                    if npc_type in ["RegularNPC", "ChestNPC", "RegularClone"]:
                        objects_output += "\n        event_script=%s," % get_event_name(
                            o.event_script
                        )
                    elif npc_type == "BattlePackNPC":
                        objects_output += (
                            "\n        after_battle=PostBattleBehaviour.%s,"
                            % POST_BATTLE_BEHAVIOURS[o.after_battle]
                        )
                    if npc_type == "BattlePackNPC" or npc_type == "BattlePackClone":
                        objects_output += "\n        battle_pack=%s," % get_pack_name(
                            o.battle_pack
                        )
                    if npc_type != "ChestClone":
                        objects_output += (
                            "\n        action_script=%s,"
                            % get_action_name(o.action_script)
                        )
                    if npc_type == "ChestNPC" or npc_type == "ChestClone":
                        objects_output += "\n        lower_70a7=%i," % o.lower_70a7
                        objects_output += "\n        upper_70a7=%i," % o.upper_70a7
                    if npc_type in ["RegularNPC", "ChestNPC", "BattlePackNPC"]:
                        objects_output += "\n        speed=%i," % o.speed
                    objects_output += "\n        visible=%s," % (
                        "True" if o.visible else "False"
                    )
                    objects_output += "\n        x=%i," % o.x
                    objects_output += "\n        y=%i," % o.y
                    objects_output += "\n        z=%i," % o.z
                    objects_output += "\n        z_half=%s," % (
                        "True" if o.z_half else "False"
                    )
                    objects_output += (
                        "\n        direction=%s," % DIRECTIONS[o.direction]
                    )
                    if npc_type in ["RegularNPC", "ChestNPC", "BattlePackNPC"]:
                        objects_output += "\n        face_on_trigger=%s," % (
                            "True" if o.face_on_trigger else "False"
                        )
                        objects_output += "\n        cant_enter_doors=%s," % (
                            "True" if o.cant_enter_doors else "False"
                        )
                        objects_output += "\n        byte2_bit5=%s," % (
                            "True" if o.byte2_bit5 else "False"
                        )
                        objects_output += "\n        set_sequence_playback=%s," % (
                            "True" if o.set_sequence_playback else "False"
                        )
                        objects_output += "\n        cant_float=%s," % (
                            "True" if o.cant_float else "False"
                        )
                        objects_output += "\n        cant_walk_up_stairs=%s," % (
                            "True" if o.cant_walk_up_stairs else "False"
                        )
                        objects_output += "\n        cant_walk_under=%s," % (
                            "True" if o.cant_walk_under else "False"
                        )
                        objects_output += "\n        cant_pass_walls=%s," % (
                            "True" if o.cant_pass_walls else "False"
                        )
                        objects_output += "\n        cant_jump_through=%s," % (
                            "True" if o.cant_jump_through else "False"
                        )
                        objects_output += "\n        cant_pass_npcs=%s," % (
                            "True" if o.cant_pass_npcs else "False"
                        )
                        objects_output += "\n        byte3_bit5=%s," % (
                            "True" if o.byte3_bit5 else "False"
                        )
                        objects_output += "\n        cant_walk_through=%s," % (
                            "True" if o.cant_walk_through else "False"
                        )
                        objects_output += "\n        byte3_bit7=%s," % (
                            "True" if o.byte3_bit7 else "False"
                        )
                        objects_output += "\n        slidable_along_walls=%s," % (
                            "True" if o.slidable_along_walls else "False"
                        )
                        objects_output += "\n        cant_move_if_in_air=%s," % (
                            "True" if o.cant_move_if_in_air else "False"
                        )
                        objects_output += "\n        byte7_upper2=%s," % (
                            "True" if o.byte7_upper2 else "False"
                        )
                    objects_output += "\n        priority_0=%s," % (
                        "True" if o.model.priority_0 else "False"
                    )
                    objects_output += "\n        priority_1=%s," % (
                        "True" if o.model.priority_1 else "False"
                    )
                    objects_output += "\n        priority_2=%s," % (
                        "True" if o.model.priority_2 else "False"
                    )
                    if o.model._show_shadow != None:
                        objects_output += "\n        show_shadow=%s," % (
                            "True" if o.model._show_shadow else "False"
                        )
                    if o.model._shadow_size != None:
                        objects_output += (
                            "\n        shadow_size=ShadowSize.%s,"
                            % SHADOW_SIZES[o.model._shadow_size]
                        )
                    if o.model._y_shift != None:
                        objects_output += "\n        y_shift=%i," % o.model._y_shift
                    if o.model._acute_axis != None:
                        objects_output += (
                            "\n        acute_axis=%i," % o.model._acute_axis
                        )
                    if o.model._obtuse_axis != None:
                        objects_output += (
                            "\n        obtuse_axis=%i," % o.model._obtuse_axis
                        )
                    if o.model._height != None:
                        objects_output += "\n        height=%i," % o.model._height
                    if o.model._directions != None:
                        objects_output += (
                            "\n        directions=VramStore.%s,"
                            % VRAM_SIZES[o.model._directions]
                        )
                    if o.model._vram_size != None:
                        objects_output += "\n        vram_size=%i," % o.model._vram_size
                    objects_output += "\n        cannot_clone=%s," % (
                        "True" if o.model.cannot_clone else "False"
                    )
                    if o.model._byte2_bit0 != None:
                        objects_output += "\n        byte2_bit0=%s," % (
                            "True" if o.model._byte2_bit0 else "False"
                        )
                    if o.model._byte2_bit1 != None:
                        objects_output += "\n        byte2_bit1=%s," % (
                            "True" if o.model._byte2_bit1 else "False"
                        )
                    if o.model._byte2_bit2 != None:
                        objects_output += "\n        byte2_bit2=%s," % (
                            "True" if o.model._byte2_bit2 else "False"
                        )
                    if o.model._byte2_bit3 != None:
                        objects_output += "\n        byte2_bit3=%s," % (
                            "True" if o.model._byte2_bit3 else "False"
                        )
                    if o.model._byte2_bit4 != None:
                        objects_output += "\n        byte2_bit4=%s," % (
                            "True" if o.model._byte2_bit4 else "False"
                        )
                    if o.model._byte5_bit6 != None:
                        objects_output += "\n        byte5_bit6=%s," % (
                            "True" if o.model._byte5_bit6 else "False"
                        )
                    if o.model._byte5_bit7 != None:
                        objects_output += "\n        byte5_bit7=%s," % (
                            "True" if o.model._byte5_bit7 else "False"
                        )
                    if o.model._byte6_bit2 != None:
                        objects_output += "\n        byte6_bit2=%s," % (
                            "True" if o.model._byte6_bit2 else "False"
                        )
                    objects_output += "\n    ),"

                objects_output += "\n]"
                objects_file = open("%s/room_%i_objects.py" % (path, i), "w")
                writeline(objects_file, objects_output)
                objects_file.close()

            # room
            room_output = "from randomizer.entities.rooms.room_imports import *"
            room_output += (
                "\nfrom randomizer.entities.rooms.room.room_%i.room_%i_partition import partition"
                % (i, i)
            )
            if len(room.exit_fields) > 0:
                room_output += (
                    "\nfrom randomizer.entities.rooms.room.room_%i.room_%i_exits import exits"
                    % (i, i)
                )
            if len(room.event_tiles) > 0:
                room_output += (
                    "\nfrom randomizer.entities.rooms.room.room_%i.room_%i_events import events"
                    % (i, i)
                )
            if len(room.objects) > 0:
                room_output += (
                    "\nfrom randomizer.entities.rooms.room.room_%i.room_%i_objects import objects"
                    % (i, i)
                )
            room_output += "\n\nroom = Room("
            room_output += "\n    partition=partition,"
            room_output += "\n    music=%s," % get_music_name(room.music)
            room_output += "\n    entrance_event=%s," % get_event_name(
                room.entrance_event
            )
            if len(room.event_tiles) > 0:
                room_output += "\n    events=events,"
            else:
                room_output += "\n    events=[],"
            if len(room.exit_fields) > 0:
                room_output += "\n    exits=exits,"
            else:
                room_output += "\n    exits=[],"
            if len(room.objects) > 0:
                room_output += "\n    objects=objects,"
            else:
                room_output += "\n    objects=[],"
            if len(room.extra_required_actions) > 0:
                room_output += "\n    extra_sprite_actions=["
                for a in room.extra_required_actions:
                    room_output += "\n        %s.%s," % (a.__class__.__name__, a.name)
                room_output += "\n    ]"
            else:
                room_output += "\n    extra_sprite_actions=[]"
            # sprite actions go here
            room_output += "\n)"
            room_file = open("%s/room_%i.py" % (path, i), "w")
            writeline(room_file, room_output)
            room_file.close()

        # Remember to put room "510" at the end.
