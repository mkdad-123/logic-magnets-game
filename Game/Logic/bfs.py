from collections import deque
from Logic.explore_search_space import get_tree_search_space
from utils import timing_function


@timing_function
def bfs(startState):
    queue = deque([startState])  
    visited = set()
    path_map = {startState: None}

    while queue:
        current = queue.popleft()  
        if current.isGoal():
            print("Goal found")
            return path_map, current
        
        visited.add(current)

        for state in get_tree_search_space(current, startState , visited):
            if state not in visited:
                path_map[state] = current
                queue.append(state) 
                visited.add(state)
    
    print("Goal not found")
    return path_map, None
