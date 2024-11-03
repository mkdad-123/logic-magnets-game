import copy

def get_tree_search_space(state, startState , visited):

    from Actions.magnets import moveNegativeMagnets,movePositiveMagnets

    neighbors = []
    grid = state.grid

    for x, row in enumerate(grid):
        for y, cell in enumerate(row):

            if grid[x][y] in ('.', 'O'):

                for magnet in state.magnets:
                    newState = copy.deepcopy(state)

                    if magnet.type == 'NM':
                        newState = moveNegativeMagnets(y, x, newState, startState, magnet.type)
                    else:
                        newState = movePositiveMagnets(y, x, newState, startState, magnet.type)

                    if newState not in visited : 
                        neighbors.append(newState)

    return neighbors

    

def get_path(path_map, startState, goalState):
    path = []
    current = goalState
    while current != startState:
        path.append(current)
        current = path_map[current]
    path.append(startState)
    path.reverse()
    return path