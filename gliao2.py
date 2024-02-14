import streamlit as st
st.title('A* Search 2')

full_world = [
['🌾', '🌾', '🌾', '🌾', '🌾', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌲', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾'],
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
['⛰', '⛰', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '🌾', '⛰', '⛰', '⛰', '⛰', '⛰', '🌾', '🌾', '🌾', '🌾', '⛰', '⛰', '⛰', '🌾', '🌾', '🌾']
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

COSTS = {'🌾': 1, '🌲': 3, '⛰': 5, '🐊': 7}

from typing import List, Tuple, Dict, Callable
from copy import deepcopy
from math import sqrt

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
    add_to_frontier(frontier, (start, get_state_metadata(world, start, goal, costs, heuristic, None)))

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
    for row in completed_map:
        st.write("".join(row))
    return pathcost

small_start = (0, 0)
small_goal = (len(small_world[0]) - 1, len(small_world) - 1)
small_path = a_star_search(small_world, small_start, small_goal, COSTS, MOVES, heuristic)
small_path_cost = pretty_print_path(small_world, small_path, small_start, small_goal, COSTS)
st.write(f"total path cost: {small_path_cost}")
#st.write(small_path)

full_start = (0, 0)
full_goal = (len(full_world[0]) - 1, len(full_world) - 1)
full_path = a_star_search(full_world, full_start,
                          full_goal, COSTS, MOVES, heuristic)
full_path_cost = pretty_print_path(
    full_world, full_path, full_start, full_goal, COSTS)
st.write(f"total path cost: {full_path_cost}")
#st.write(full_path)

