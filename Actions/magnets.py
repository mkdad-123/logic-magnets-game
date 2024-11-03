import Actions.negativeAction as negativeAction
import Actions.positiveAction as positiveAction
from utils import timing_function

moveNtv = negativeAction
movePtv = positiveAction

    # A method to move magnets

def moveMagnets(columnNumber  , rowNumber , currentState , startGrid , magnets) : 

    grid = currentState.grid

    try:

        if not validateMove(grid , rowNumber ,  columnNumber) : 
            raise ValueError('I am Sorry, there is an iron')
        
        if grid[rowNumber][columnNumber] == 'O' :
            currentState.numGoals -= 1

        grid[rowNumber][columnNumber] = magnets.type

        if startGrid[magnets.posX][magnets.posY] == 'O':
            grid [magnets.posX][magnets.posY] = 'O'
            currentState.numGoals += 1
        else : 
            grid [magnets.posX][magnets.posY] = '.'
        

        magnets.posX = rowNumber
        magnets.posY = columnNumber

    except IndexError:
        print(" The position is out of the grid s bounds ")
    except Exception as e:
        print(f"An unexpected error occurred : {e}")



    # A method to move negative magnets 

def moveNegativeMagnets(columnNumber  , rowNumber , currentState , startState , magnetType) :

    startGrid = startState.grid
    
    magnets = getMagnets(currentState.magnets, magnetType)

    if(not magnets) :
        print('No magnet found with the specified type','\n')
        return
    
    moveMagnets(columnNumber  , rowNumber , currentState , startGrid , magnets) 
        
    
    moveNtv.moveRightIrons(columnNumber  , rowNumber , currentState , startGrid)
    moveNtv.moveLeftIrons(columnNumber  , rowNumber , currentState , startGrid)
    moveNtv.moveUpIrons(columnNumber  , rowNumber , currentState , startGrid)
    moveNtv.moveDownIrons(columnNumber  , rowNumber , currentState , startGrid)

    currentState.numSteps -= 1

    return currentState

    # A method to move positive magnets 

def movePositiveMagnets(columnNumber  , rowNumber , currentState , startState , magnetType) :

    startGrid = startState.grid

    magnets = getMagnets(currentState.magnets, magnetType)

    if(not magnets) :

        print('No magnet found with the specified type','\n')
        return
    
    moveMagnets(columnNumber  , rowNumber , currentState , startGrid , magnets)
         

    movePtv.moveRightIrons(columnNumber  , rowNumber , currentState , startGrid )
    movePtv.moveLeftIrons(columnNumber  , rowNumber , currentState , startGrid)
    movePtv.moveDownIrons(columnNumber  , rowNumber , currentState , startGrid)
    movePtv.moveUpIrons(columnNumber  , rowNumber , currentState , startGrid)

    currentState.numSteps -= 1
    return currentState


def getMagnets(magnets, magnet_type):
    for magnet in magnets:
        if magnet.type == magnet_type:
            return magnet
    return None

def validateMove(grid , rowNumber ,  columnNumber) : 
    if grid[rowNumber][columnNumber] == '#':
        print()
        return False
    return True
