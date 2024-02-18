import streamlit as st
from math import sqrt
from copy import deepcopy
from typing import List, Tuple, Dict, Callable

st.set_page_config(layout="wide", initial_sidebar_state="expanded")

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
    st.table(completed_map)
    return pathcost


def update_world_map(world, edited_rows):
    for row_index in edited_rows:
        for col_index in edited_rows[row_index]:
            world[int(row_index)][int(col_index)] = edited_rows[row_index][col_index]

def find_emoji(emoji, world):
    for row_index, row in enumerate(world):
        for col_index, col in enumerate(row):
            if col == emoji:
                return (col_index, row_index)

def get_start(world):
    return find_emoji('🚶🏿‍♀️', world)

def get_goal(world):
    return find_emoji('🎁', world)

def display_search_world(world):
    path_cost_container = st.empty()
    start = get_start(world)
    goal = get_goal(world)
    path = a_star_search(world, start, goal, COSTS, MOVES, heuristic)
    if (path == None or None in path):
        path_cost_container.header(f"No path found!!")
        st.table(world)
    else:
        path_cost = pretty_print_path(world, path, start, goal, COSTS)
        path_cost_container.header(f"Total path cost: {path_cost}")

def replace_old_start_with_plain():
    old_start_x, old_start_y = get_start(full_world)
    add_edited_row_to_saved_edited_rows(str(old_start_y), str(old_start_x), '🌾')
    full_world[old_start_y][old_start_x] = '🌾'

def replace_old_goal_with_plain():
    old_goal_x, old_goal_y = get_goal(full_world)
    add_edited_row_to_saved_edited_rows(str(old_goal_y), str(old_goal_x), '🌾')
    full_world[old_goal_y][old_goal_x] = '🌾'

def get_saved_edited_rows():
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

def add_edited_row_to_saved_edited_rows(row_index, col_index, emoji):
    col = {col_index: emoji}
    saved_edited_rows = get_saved_edited_rows()
    saved_edited_rows[row_index] = col

def data_editor_callback():
    edited_rows = st.session_state.get("world").get("edited_rows")
    st.write(edited_rows)
    #check if adding start or goal
    for row_index in edited_rows:
        for col_index in edited_rows[row_index]:
            if edited_rows[row_index][col_index] == '🚶🏿‍♀️':
                st.write("found replacing start")
                replace_old_start_with_plain()
            if edited_rows[row_index][col_index] == '🎁':
                replace_old_goal_with_plain()
    copy_data_editor_edited_rows_to_saved_edited_rows()

def display_edit_world(world):
    st.header("Instructions:")
    st.subheader("Double-Click any cell to select Terrain.  If you choose a new Start or Goal, the old Start or Goal will change to a Plain terrain")
    st.subheader("Copy/Paste also works, but only Start, Goal, or Terrain are allowed")
    st.subheader("Click 'Search World' to find the least cost path to the Goal.  Click 'Edit World' to return to this screen")
    terrain_choices = {}
    for col_index in range(len(world[0])):
        terrain_choices[str(col_index)] = st.column_config.SelectboxColumn(
            options=['🚶🏿‍♀️', '🌾', '🌲', '⛰', '🐊','🌋', '🎁'])
    st.data_editor(world, key="world", hide_index=True, height=1000, column_config=terrain_choices, on_change=data_editor_callback)

def copy_data_editor_edited_rows_to_saved_edited_rows():
    edited_rows = st.session_state.get("world").get("edited_rows")

    #merge current edits with saved previous edits
    for row_index in edited_rows:
        for col_index in edited_rows[row_index]:
            add_edited_row_to_saved_edited_rows(row_index, col_index, edited_rows[row_index][col_index])

def print_legend():
    st.sidebar.markdown("Legend:")
    st.sidebar.markdown(f"🚶🏿‍♀️- Start. {get_start(full_world)}, cost=0")
    st.sidebar.markdown(f"🎁- Goal. {get_goal(full_world)}, cost=0")
    st.sidebar.markdown("🌾- plains. cost=1")
    st.sidebar.markdown("🌲- forest. cost=3")
    st.sidebar.markdown("⛰ - hills.  cost=5")
    st.sidebar.markdown("🐊- swamp.  cost=7")
    st.sidebar.markdown("🌋 - mountains.  impassible")
    st.sidebar.write(get_saved_edited_rows())

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
    add_edited_row_to_saved_edited_rows("0", "0", '🚶🏿‍♀️')
    add_edited_row_to_saved_edited_rows("26", "26", '🎁')
#    st.session_state["_world"] = {"edited_rows": {"0": {"0": '🚶🏿‍♀️'}, "26": {"26": '🎁'}}}
    display_edit_world(full_world)
    
#Edit World Cell
if (st.session_state.get("edit") == False and st.session_state.get("search") == False):
    copy_data_editor_edited_rows_to_saved_edited_rows()
    update_world_map(full_world, get_saved_edited_rows())
    display_edit_world(full_world)

#Edit World Button Clicked
if st.sidebar.button("Edit World", key="edit"):
    update_world_map(full_world, get_saved_edited_rows())
#    if (st.session_state.get("world") != None):
#        update_world_map(full_world, st.session_state.get("world").get("edited_rows"))
    display_edit_world(full_world)

#Search World Button Clicked
if st.sidebar.button("Search World", key="search"):
    update_world_map(full_world, get_saved_edited_rows())
    display_search_world(full_world)

print_legend()

