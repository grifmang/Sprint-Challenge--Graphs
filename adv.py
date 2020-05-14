from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
'''
player.travel(direction, boolean)
room.print_room_description(player)
room.get_exits()
room.get_exits_string()
room.connect_rooms(direction, connecting_room)
room.get_room_in_direction(direction)
room.get_coords()
'''
traversal_path = []
visited_rooms = set()
back_up_tracker = -1
opposite_direction = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

while len(visited_rooms) < len(room_graph):
    has_exits = False
    # if player.current_room not in visited_rooms:
    visited_rooms.add(player.current_room)
    exits = player.current_room.get_exits()

    for exit in exits:
        if player.current_room.get_room_in_direction(exit) not in visited_rooms:
            back_up_tracker = -1
            player.travel(exit)
            traversal_path.append(exit)
            has_exits = True
            # print('exit', player.current_room)
            break
    if has_exits == False:
        # print('has_exits', player.current_room)
        player.travel(opposite_direction[traversal_path[back_up_tracker]])
        traversal_path.append(opposite_direction[traversal_path[back_up_tracker]])
        back_up_tracker -= 2
        visited_rooms.add(player.current_room)
        # print(traversal_path)
        




# TRAVERSAL TEST - DO NOT MODIFY
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
