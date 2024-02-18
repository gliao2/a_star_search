import streamlit as st
from math import sqrt
from copy import deepcopy
from typing import List, Tuple, Dict, Callable

full_world = [
['🚶🏿‍♀️', '🌾', '🌾', '🌾', '🌾', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾'],
['🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌾', '🌾', '🌋', '🌋', '🌋', '🌋', '🌋', '🌋', '🌋', '🌾', '🌾'],
['🌾', '🌾', '🌾', '🌾', '🌋', '🌋', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌋', '🌋', '🌋', '⛰', '⛰', '⛰', '🌋', '🌋', '⛰', '⛰'],
['🌾', '🌾', '🌾', '🌾', '⛰', '🌋', '🌋', '🌋', '🌲', '🌲', '🌲', '🌲', '🐊', '🐊', '🌲', '🌲', '🌲', '🌲', '🌲', '🌾', '🌾', '⛰', '⛰', '🌋', '🌋', '⛰', '🌾'],
['🌾', '🌾', '🌾', '⛰', '⛰', '🌋', '🌋', '🌲', '🌲', '🌾', '🌾', '🐊', '🐊', '🐊', '🐊', '🌲', '🌲', '🌲', '🌾', '🌾', '🌾', '⛰', '🌋', '🌋', '🌋', '⛰', '🌾'],
['🌾', '⛰', '⛰', '⛰', '🌋', '🌋', '⛰', '⛰', '🌾', '🌾', '🌾', '🌾', '🐊', '🐊', '🐊', '🐊', '🐊', '🌾', '🌾', '🌾', '🌾', '🌾', '⛰', '🌋', '⛰', '🌾', '🌾'],
['🌾', '⛰', '⛰', '🌋', '🌋', '⛰', '⛰', '🌾', '🌾', '🌾', '🌾', '⛰', '🌋', '🌋', '🌋', '🐊', '🐊', '🐊', '🌾', '🌾', '🌾', '🌾', '🌾', '⛰', '🌾', '🌾', '🌾'],
['🌾', '🌾', '⛰', '⛰', '⛰', '⛰', '⛰', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '⛰', '🌋', '🌋', '🌋', '🐊', '🐊', '🐊', '🌾', '🌾', '⛰', '⛰', '⛰', '🌾', '🌾'],
['🌾', '🌾', '🌾', '⛰', '⛰', '⛰', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '⛰', '⛰', '🌋', '🌋', '🌾', '🐊', '🐊', '🌾', '🌾', '⛰', '⛰', '⛰', '🌾', '🌾', '🌾'],
['🌾', '🌾', '🌾', '🐊', '🐊', '🐊', '🌾', '🌾', '⛰', '⛰', '⛰', '🌋', '🌋', '🌋', '🌋', '🌾', '🌾', '🌾', '🐊', '🌾', '⛰', '⛰', '⛰', '🌾', '🌾', '🌾', '🌾'],
['🌾', '🌾', '🐊', '🐊', '🐊', '🐊', '🐊', '🌾', '⛰', '⛰', '🌋', '🌋', '🌋', '⛰', '🌾', '🌾', '🌾', '🌾', '🌾', '⛰', '🌋', '🌋', '🌋', '⛰', '🌾', '🌾', '🌾'],
['🌾', '🐊', '🐊', '🐊', '🐊', '🐊', '🌾', '🌾', '⛰', '🌋', '🌋', '⛰', '🌾', '🌾', '🌾', '🌾', '🐊', '🐊', '🌾', '🌾', '⛰', '🌋', '🌋', '⛰', '🌾', '🌾', '🌾'],
['🐊', '🐊', '🐊', '🐊', '🐊', '🌾', '🌾', '⛰', '⛰', '🌋', '🌋', '⛰', '🌾', '🐊', '🐊', '🐊', '🐊', '🌾', '🌾', '🌾', '⛰', '🌋', '⛰', '🌾', '🌾', '🌾', '🌾'],
['🌾', '🐊', '🐊', '🐊', '🐊', '🌾', '🌾', '⛰', '🌲', '🌲', '⛰', '🌾', '🌾', '🌾', '🌾', '🐊', '🐊', '🐊', '🐊', '🌾', '🌾', '⛰', '🌾', '🌾', '🌾', '🌾', '🌾'],
['🌾', '🌾', '🌾', '🌾', '🌋', '🌾', '🌾', '🌲', '🌲', '🌲', '🌲', '⛰', '⛰', '⛰', '⛰', '🌾', '🐊', '🐊', '🐊', '🌾', '🌾', '⛰', '🌋', '⛰', '🌾', '🌾', '🌾'],
['🌾', '🌾', '🌾', '🌋', '🌋', '🌋', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌋', '🌋', '🌋', '⛰', '⛰', '🌾', '🐊', '🌾', '⛰', '🌋', '🌋', '⛰', '🌾', '🌾', '🌾'],
['🌾', '🌾', '🌋', '🌋', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌋', '🌋', '🌋', '🌾', '🌾', '🌋', '🌋', '🌋', '🌾', '🌾', '🌾', '🌾', '🌾'],
['🌾', '🌾', '🌾', '🌋', '🌋', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌋', '🌋', '🌋', '🌋', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾'],
['🌾', '🌾', '🌾', '🌋', '🌋', '🌋', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌾', '🌾', '🌾', '⛰', '⛰', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾'],
['🌾', '🌾', '🌾', '🌾', '🌋', '🌋', '🌋', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🐊', '🐊', '🐊', '🐊'],
['🌾', '🌾', '⛰', '⛰', '⛰', '⛰', '🌋', '🌋', '🌲', '🌲', '🌲', '🌲', '🌲', '🌾', '🌋', '🌾', '🌾', '🌾', '🌾', '🌾', '🐊', '🐊', '🐊', '🐊', '🐊', '🐊', '🐊'],
['🌾', '🌾', '🌾', '🌾', '⛰', '⛰', '⛰', '🌋', '🌋', '🌋', '🌲', '🌲', '🌋', '🌋', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🐊', '🐊', '🐊', '🐊', '🐊', '🐊', '🐊'],
['🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '⛰', '⛰', '⛰', '🌋', '🌋', '🌋', '🌋', '🌾', '🌾', '🌾', '🌾', '⛰', '⛰', '🌾', '🌾', '🐊', '🐊', '🐊', '🐊', '🐊', '🐊'],
['🌾', '⛰', '⛰', '🌾', '🌾', '⛰', '⛰', '⛰', '⛰', '⛰', '🌾', '🌾', '🌾', '🌾', '🌾', '⛰', '⛰', '🌋', '🌋', '⛰', '⛰', '🌾', '🐊', '🐊', '🐊', '🐊', '🐊'],
['⛰', '🌋', '⛰', '⛰', '⛰', '⛰', '🌾', '🌾', '🌾', '🌾', '🌾', '🌋', '🌋', '🌋', '⛰', '⛰', '🌋', '🌋', '🌾', '🌋', '🌋', '⛰', '⛰', '🐊', '🐊', '🐊', '🐊'],
['⛰', '🌋', '🌋', '🌋', '⛰', '🌾', '🌾', '🌾', '🌾', '🌾', '⛰', '⛰', '🌋', '🌋', '🌋', '🌋', '⛰', '⛰', '⛰', '⛰', '🌋', '🌋', '🌋', '🐊', '🐊', '🐊', '🐊'],
['⛰', '⛰', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '⛰', '⛰', '⛰', '⛰', '⛰', '🌾', '🌾', '🌾', '🌾', '⛰', '⛰', '⛰', '🌾', '🌾', '🎁']
]

small_world = [
    ['🌾', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲'],
    ['🌾', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲'],
    ['🌾', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲'],
    ['🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾'],
    ['🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌾'],
    ['🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌾'],
    ['🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌾']
]

MOVES = [(0, -1), (1, 0), (0, 1), (-1, 0)]

COSTS = {'🚶🏿‍♀️': 0, '🌾': 1, '🌲': 3, '⛰': 5, '🐊': 7, '🎁': 0}


def is_goal(current_state: Tuple[Tuple[int, int], Tuple[int, float, Tuple[int, int]]], goal: Tuple[int, int]):
    return current_state[0] == goal


def add_to_explored(explored: Dict[Tuple[int, int], Tuple[int, float, Tuple[int, int]]], state: Tuple[Tuple[int, int], Tuple[int, float, Tuple[int, int]]]):
    explored[state[0]] = state[1]
    return explored


def path(current_state: Tuple[Tuple[int, int], Tuple[int, float, Tuple[int, int]]], explored: Dict[Tuple[int, int], Tuple[int, float, Tuple[int, int]]]):
    return_path = []
    return_path.append(current_state[0])
    add_to_explored(explored, current_state)
    state = current_state[1][2]
    while state:
        return_path.append(state)
        state_metadata = explored.get(state)
        state = None if state_metadata == None else state_metadata[2]
    return return_path[::-1]


def get_next_state_on_frontier(frontier: List[Tuple[Tuple[int, int], Tuple[int, float, Tuple[int, int]]]], use_dfs=False):
    if not use_dfs:
        frontier.sort(key=lambda state: state[1][0] + state[1][1])
    return frontier.pop() if use_dfs else frontier.pop(0)


def add_to_frontier(frontier: List[Tuple[Tuple[int, int], Tuple[int, float, Tuple[int, int]]]], state: Tuple[Tuple[int, int], Tuple[int, float, Tuple[int, int]]]):
    frontier.append(state)
    return frontier


def is_state_on_explored(state: Tuple[Tuple[int, int], Tuple[int, float, Tuple[int, int]]], explored: Dict[Tuple[int, int], Tuple[int, float, Tuple[int, int]]]):
    if not state[0] in explored:
        return False
    state_cost = state[1][0] + state[1][1]
    state_position = state[0]
    explored_cost = explored[state_position][0] + explored[state_position][1]
    if state_cost < explored_cost:
        del explored[state_position]
        explored[state_position] = state[1]
    return True


def is_state_on_frontier(state: Tuple[Tuple[int, int], Tuple[int, float, Tuple[int, int]]], frontier: List[Tuple[Tuple[int, int], Tuple[int, float, Tuple[int, int]]]]):
    frontier_positions = [frontier_state[0] for frontier_state in frontier]
    state_position = state[0]
    if not state_position in frontier_positions:
        return False
    frontier_index = frontier_positions.index(state_position)
    state_cost = state[1][0] + state[1][1]
    frontier_costs = [frontier_state[1][0] + frontier_state[1][1]
                      for frontier_state in frontier if frontier_state[0] == state_position]
    if len(frontier_costs) > 0 and state_cost < frontier_costs[0] and frontier_index > 0:
        frontier[frontier_index] = state
    return True


def heuristic(current_position: Tuple[int, int], goal: Tuple[int, int]):
    return sqrt((current_position[0] - goal[0])**2 + (current_position[1] - goal[1])**2)


def get_state_metadata(world: List[List[str]], position: Tuple[int, int], goal: Tuple[int, int], costs: Dict[str, int], heuristic: Callable, parent_state: Tuple[Tuple[int, int], Tuple[int, float, Tuple[int, int]]]):
    parent_cost = parent_state[1][0] if parent_state != None else 0
    parent_position = parent_state[0] if parent_state != None else None
    g_n = parent_cost + costs[world[position[1]][position[0]]]
    h_n = heuristic(position, goal) if heuristic else None
    return (g_n, h_n, parent_position)


def successors(current_state: Tuple[Tuple[int, int], Tuple[int, float, Tuple[int, int]]], world: List[List[str]], goal: Tuple[int, int], costs: Dict[str, int], moves: List[Tuple[int, int]], heuristic: Callable):
    children_states = []
    for move in moves:
        current_position = current_state[0]
        next_position = (
            current_position[0] + move[0], current_position[1] + move[1])
        if next_position[0] >= 0 and next_position[0] < len(world[0]) and next_position[1] >= 0 and next_position[1] < len(world) and world[next_position[1]][next_position[0]] != '🌋':
            children_states.append(((next_position), get_state_metadata(
                world, next_position, goal, costs, heuristic, current_state)))
    return children_states


def get_path_icon(old_position: Tuple[int, int], new_position: Tuple[int, int]):
    path_icon = ''
    if (old_position == None or (new_position[1] - old_position[1] == 1)):
        path_icon = '⏬'
    elif ((new_position[1] - old_position[1] == -1)):
        path_icon = '⏫'
    elif ((new_position[0] - old_position[0] == 1)):
        path_icon = '⏩'
    elif ((new_position[0] - old_position[0] == -1)):
        path_icon = '⏪'
    return path_icon


def a_star_search(world: List[List[str]], start: Tuple[int, int], goal: Tuple[int, int], costs: Dict[str, int], moves: List[Tuple[int, int]], heuristic: Callable) -> List[Tuple[int, int]]:
    frontier = []
    explored = {}
    add_to_frontier(frontier, (start, get_state_metadata(
        world, start, goal, costs, heuristic, None)))

    while len(frontier) > 0:
        current_state = get_next_state_on_frontier(frontier)
        if is_goal(current_state, goal):
            return path(current_state, explored)
        children_states = successors(
            current_state, world, goal, costs, moves, heuristic)
        for child_state in children_states:
            if not (is_state_on_explored(child_state, explored) or is_state_on_frontier(child_state, frontier)):
                add_to_frontier(frontier, child_state)
        add_to_explored(explored, current_state)

    return None

# Above is unmodified code from Module 1
#######################################################################################
# Below is modified code from Module 1 or new code for Module 4

def pretty_print_path(world: List[List[str]], path: List[Tuple[int, int]], start: Tuple[int, int], goal: Tuple[int, int], costs: Dict[str, int]) -> int:
    """
    pretty_print_path overlays the lowest path cost on the world and displays it as a streamlit table
    Uses: get_path_icon.  Used by: display_search_world
    
    world List[List[str]]: the world (terrain map) for the path to be printed upon.
    path List[Tuple[int, int]]: the path from start to goal, in offsets.
    start Tuple[int, int]: the starting location for the path.
    goal Tuple[int, int]: the goal location for the path.
    costs Dict[str, int]: the costs for each action.

    returns int - The path cost.
    """
    pathcost = 0
    completed_map = deepcopy(world)
    old_position = None
    for position in path:
        pathcost += costs[world[position[1]][position[0]]]
        path_icon = get_path_icon(old_position, position)
        if (old_position != None):
            completed_map[old_position[1]][old_position[0]] = path_icon
        if (position == goal):
            completed_map[position[1]][position[0]] = '🎁'
        old_position = position
    
    #Display a streamlit table with overlayed path 
    st.table(completed_map)

    return pathcost

def display_path_coordinates(path: List[Tuple[int, int]]):
    """
    display_path_coordinates displays the coordinates of the path as text.  
    Impure function displays path on streamlit main container
    Uses: . Used by: display_search_world.

    path List[Tuple[int, int]]: List of tuples containing coordinates for lowest cost path to goal

    returns:  None
    """
    path_coordinates = ""
    coordinate_count = 0
    for x, y in path:
        coordinate_count+=1
        if coordinate_count%15==0:
            path_coordinates += "\n"
        if path_coordinates == "":
            path_coordinates += "(" + str(x) + ", " + str(y) + ")"
        else:
            path_coordinates += "->(" + str(x) + ", " + str(y) + ")"
    st.text(path_coordinates)


def update_world_map(world: List[List[str]], edited_rows: Dict[str, Dict[str, str]]):
    """
    update_world_map modifies the world with all the edits performed in the session.  A session is bound to a browser tab.
    If a browser tab is refreshed that's a new session.  A differrent tab or a different browser is its own session.
    The world is presented in 2 ways, edit mode and display mode.  In edit mode, the user can change start, goal, or any terrain.  
    Each edit is stored in edited_rows.  These edits are then applied to the world. 
    Uses: . Used By: Edit Cell in data_editor, Edit World button, Find Path button

    world List[List[str]]: The world terrain map with start and goal
    edited_rows Dict[Dict[str: str]]: Contains all the edits in the session.  The outside Dist is the row.  
                                      The inside Dict is the Col.  The value is the Start, Goal, or Terrain

    returns:  None
    """
    for row_index in edited_rows:
        for col_index in edited_rows[row_index]:
            world[int(row_index)][int(col_index)] = edited_rows[row_index][col_index]

def find_emoji(emoji: str, world:List[List[str]])->Tuple[int, int]:
    """
    find_emoji finds a particular emoji in the world.  If the emoji exist more than once, returns the first.  But this is used
    to find the start and goal in the world, and only one of each should exist. 
    Uses: . Used By: get_start, get_goal.

    emoji str: emoji character to find in world
    world List[List[str]]: The world terrain map with start and goal

    returns Tuple[int, int]:  returns x, y coordinate
    """
    for row_index, row in enumerate(world):
        for col_index, col in enumerate(row):
            if col == emoji:
                return (col_index, row_index)

def get_start(world:List[List[str]])->Tuple[int, int]:
    """
    get_start finds the start position in the world.  should only be one start at a time. 
    Uses: find_emoji. Used By: display_search_world, replace_old_start_with_plain, print_legend.

    world List[List[str]]: The world terrain map with start and goal

    returns Tuple[int, int]:  returns x, y coordinate of start
    """
    return find_emoji('🚶🏿‍♀️', world)

def get_goal(world:List[List[str]])->Tuple[int, int]:
    """
    get_goal finds the goal position in the world.  Should only be one goal at a time. 
    Uses: find_emoji. Used By: display_search_world, replace_old_goal_with_plain, print_legend.

    world List[List[str]]: The world terrain map with start and goal

    returns Tuple[int, int]:  returns x, y coordinate of goal
    """
    return find_emoji('🎁', world)

def display_search_world(world:List[List[str]]):
    """
    display_search_world impure function displays the world with overlay of lowest cost path from start to goal.  If no
    path is found displays message that no path is found.  Below the map, displays the path coordinates as text.  Displays
    the Total path cost as a header above the map.
    Uses: get_start, get_goal, a_star_search, pretty_print_path, display_path_coordinate. 
    Used By: Find Path button click.

    world List[List[str]]: The world terrain map with start and goal

    returns:  None
    """
    path_cost_container = st.empty()
    start = get_start(world)
    goal = get_goal(world)
    path = a_star_search(world, start, goal, COSTS, MOVES, heuristic)
    if (path == None or None in path):
        path_cost_container.header("No path found!!")
        st.table(world)
    else:
        path_cost = pretty_print_path(world, path, start, goal, COSTS)
        path_cost_container.header(f"Total path cost: {path_cost}")
        display_path_coordinates(path)

def replace_old_start_with_plain():
    """
    replace_old_start_with_plain replaces the start in saved_edited_rows and full_world with a plain.  This function
    allows the user to add a new start on the map and not worry about changing the old start.  This has to access
    the global and state variables since this is called from a callback that doesn't take parameters.
    Uses: get_start, add_edited_row_to_saved_edited_rows. Used By: data_editor_callback.

    world List[List[str]]: The world terrain map with start and goal

    returns:  None
    """
    old_start_x, old_start_y = get_start(full_world)
    add_edited_row_to_saved_edited_rows(str(old_start_y), str(old_start_x), '🌾')
    full_world[old_start_y][old_start_x] = '🌾'

def replace_old_goal_with_plain():
    """
    replace_old_goal_with_plain replaces the goal in saved_edited_rows and full_world with a plain.  This function
    allows the user to add a new goal on the map and not worry about changing the old goal.  This has to access
    the global and state variables since this is called from a callback that doesn't take parameters.
    Uses: get_goal, add_edited_row_to_saved_edited_rows. Used By: data_editor_callback.

    world List[List[str]]: The world terrain map with start and goal

    returns:  None
    """
    old_goal_x, old_goal_y = get_goal(full_world)
    add_edited_row_to_saved_edited_rows(str(old_goal_y), str(old_goal_x), '🌾')
    full_world[old_goal_y][old_goal_x] = '🌾'

def get_saved_edited_rows():
    """
    get_saved_edited_rows returns dictionary that stores all the previous edits.  It looks a little complex, but it's
    to handle the initialization of the nested dictionary structure.
    Uses: . Used By: add_edited_row_to_saved_edited_rows, Edit World Cell click, Edit World button click, Find Path button click.

    returns Dict[str, Dict[str, str]]:  Contains all the edits in the session.  The outside Dict is the row.  
                                      The inside Dict is the Col.  The value is the Start, Goal, or Terrain
    """
    saved_world = st.session_state.get("_world")
    if saved_world == None:
        saved_world = {}
        st.session_state["_world"] = saved_world
        saved_edited_rows = {}
        saved_world["edited_rows"] = saved_edited_rows
    else:
        saved_edited_rows = saved_world.get("edited_rows")
        if saved_edited_rows == None:
            saved_edited_rows = {}
            saved_world["edited_rows"] = saved_edited_rows
    return saved_edited_rows

def add_edited_row_to_saved_edited_rows(row_index: str, col_index: str, emoji: str):
    """
    add_edited_row_to_saved_edited_rows is a helper function to add entries into the saved_edited_rows dictionary structure.

    row_index str: row index that was edited
    col_index str: col index that was edited
    emoji str: emoji to store, can be start, goal, or terrain
    Uses: get_saved_edited_rows. 
    Used By: replace_old_start_with_plain, replace_old_goal_with_plain, copy_data_editor_edited_rows_to_saved_edited_rows, 
             First run to initialize with default start and goal.

    returns:  None
    """
    col = {col_index: emoji}
    saved_edited_rows = get_saved_edited_rows()
    saved_edited_rows[row_index] = col

def data_editor_callback():
    """
    data_editor_callback is the callback function that is called whenever a cell in the world is edited.  The edit is stored
    in a session_state variable associated with the data_editor key "world".  If the edit is for a new start or goal, 
    finds the old start or goal and replaces with a plain.  Then save the edit with all previous edits in session

    Uses: replace_old_start_with_plain, replace_old_goal_with_plain, copy_data_editor_edited_rows_to_saved_edited_rows. 
    Used By: on_change on data_editor with key="world".

    returns:  None
    """
    edited_rows = st.session_state.get("world").get("edited_rows")

    #check if adding new start or goal, if so replace the old start or goal
    for row_index in edited_rows:
        for col_index in edited_rows[row_index]:
            if edited_rows[row_index][col_index] == '🚶🏿‍♀️':
                replace_old_start_with_plain()
            if edited_rows[row_index][col_index] == '🎁':
                replace_old_goal_with_plain()

    #Save new edit with all other edits in this session
    copy_data_editor_edited_rows_to_saved_edited_rows()

def display_edit_world(world):
    """
    display_edit_world displays the world using a streamlit data_editor.  The data_editor allows the user to edit cells.  
    The cells restrict the values to start, goal, and terrain.  A callback is configured to check if the edit
    is for a new start or goal, so the old start or goal can be replaced with a plain to ensure there is one and only one
    start and goal.  Uses . Used By: on First Run, Edit Cell click, Find Path button click.

    world List[List[str]]: The world terrain map with start and goal

    returns:  None
    """
    st.header("Instructions:")
    st.subheader("Double-Click any cell to select Terrain.  If you choose a new Start or Goal, the old Start or Goal will change to a Plain terrain")
    st.subheader("Copy/Paste also works, but only Start, Goal, or Terrain are allowed")
    st.subheader("Click 'Find Path' to find the least cost path to the Goal.  Click 'Edit World' to return to this screen")
    terrain_choices = {}

    #restrict cell choices to start, goal, terrain
    for col_index in range(len(world[0])):
        terrain_choices[str(col_index)] = st.column_config.SelectboxColumn(options=['🚶🏿‍♀️', '🌾', '🌲', '⛰', '🐊','🌋', '🎁'], required=True)
    
    #make the height large enough to avoid scroll of editor, though the map is large so browser scroll is still required
    #configure cell value restriction and callback
    st.data_editor(world, key="world", hide_index=True, height=1000, column_config=terrain_choices, on_change=data_editor_callback)

def copy_data_editor_edited_rows_to_saved_edited_rows():
    """
    copy_data_editor_edited_rows_to_saved_edited_rows copies the edited rows from the data editor to the saved_edited_rows which, 
    which store all the edits for the entire session.  This is necessary because each edit causes a re-run.  
    Uses add_edited_row_to_saved_edited_rows. Used By: data_editor_callback.

    returns:  None
    """
    edited_rows = st.session_state.get("world").get("edited_rows")

    #merge current edits with saved previous edits
    for row_index in edited_rows:
        for col_index in edited_rows[row_index]:
            add_edited_row_to_saved_edited_rows(row_index, col_index, edited_rows[row_index][col_index])

def print_legend():
    """
    print_legend displays the legend in the sidebar.  Legend include Start, Goal, Terrain, including costs.  
    Costs for Start and Goal are 0, and the world is now modified to include them.
    Uses . Used By: streamlit main.

    returns:  None
    """
    st.sidebar.markdown("Legend:")
    st.sidebar.markdown(f"🚶🏿‍♀️- Start. {get_start(full_world)}, cost=0")
    st.sidebar.markdown(f"🎁- Goal. {get_goal(full_world)}, cost=0")
    st.sidebar.markdown("🌾- plains. cost=1")
    st.sidebar.markdown("🌲- forest. cost=3")
    st.sidebar.markdown("⛰ - hills.  cost=5")
    st.sidebar.markdown("🐊- swamp.  cost=7")
    st.sidebar.markdown("🌋 - mountains.  impassible")

st.set_page_config(layout="wide", initial_sidebar_state="expanded")

#Set the sidebar width as narrow as we can so we have more space for the map
st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 200px;
        }
    """,
    unsafe_allow_html=True,
)

#First Run
if (st.session_state.get("edit") == None and st.session_state.get("search") == None):
    #Initialize saved session edits with default start and goal
    #Saved session edits must have one and only one start and goal
    #start in edit mode with instructions
    add_edited_row_to_saved_edited_rows("0", "0", '🚶🏿‍♀️')
    add_edited_row_to_saved_edited_rows("26", "26", '🎁')
    display_edit_world(full_world)
    
#Edit World Cell - whenever a cell is edited, a rerun occurs and edit and search are false
if (st.session_state.get("edit") == False and st.session_state.get("search") == False):
    update_world_map(full_world, get_saved_edited_rows())
    display_edit_world(full_world)

#Edit World Button Clicked
if st.sidebar.button("Edit World", key="edit"):
    update_world_map(full_world, get_saved_edited_rows())
    display_edit_world(full_world)

#Search World Button Clicked
if st.sidebar.button("Find Path", key="search"):
    update_world_map(full_world, get_saved_edited_rows())
    display_search_world(full_world)

#print legend in the sidebar in all cases
print_legend()

