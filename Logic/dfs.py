from collections import deque
from utils import timing_function
from Logic.explore_search_space import get_tree_search_space

@timing_function
def dfs(startState ):

    stack = deque([startState])
    visited = set()
    path_map = {startState: None}

    while stack:
        current = stack.pop()
        if current.isGoal():
            print("Goal found")
            return path_map , current
        
        visited.add(current)

        for state in get_tree_search_space(current , startState , visited):
            if state not in visited:
                path_map[state] = current
                stack.append(state)
                visited.add(state)
    
    print("Goal not found")
    return path_map , None


