from Structure.state import State
from Structure.levels import Level
from Logic.gamePlay import GamePlay
from Logic.dfs import dfs
from Logic.bfs import bfs
from Logic.explore_search_space import get_path
import copy
from utils import display_path



def main():
    
    method = int(input('enter a method : {1 : user play , 2 : bfs , 3 : dfs} : '))

    level = Level.chooseLevel()

    startState = State(level)

    currentState = copy.deepcopy(startState)
    
    print('\n' , "{--------- Welcome to The Logic Magnets ---------}" , '\n')
    
    startState.printGrid()
    
    print(f"number of the goals : {currentState.numGoals}")


    if method == 1 : 
        GamePlay(startState , currentState).play()

    if method == 2 : 
        path_map, goalState = bfs(startState)
        if goalState:

            path = get_path(path_map, startState, goalState) 

            display_path(path)
            
    if method == 3 : 
            
            path_map, goalState = dfs(startState)
            if goalState:

                path = get_path(path_map, startState, goalState) 

                display_path(path)
    
        
        # for state in path:
        #     state.printGrid() 
        #     print()
        #     print(f"number of the goals : {state.numGoals}")
        #     print()

    
if __name__ == "__main__" :
    main()