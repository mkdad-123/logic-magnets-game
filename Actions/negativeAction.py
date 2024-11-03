from Actions.push import pushToDown,pushToLeft,pushToRight,pushToUP
from Actions.moveBlocks import move_block_iron_left , move_block_iron_right


    # A method to check if there are iron pieces on right side of the magnets

def moveRightIrons(columnNumber  , rowNumber , currentState , startGrid):

    from Actions.magnets import moveMagnets , getMagnets

    n = currentState.numColumns
    grid = currentState.grid
    i = columnNumber
    i += 1

    while i < n : 

        if  grid[rowNumber][i] == '#' and i+1 < n : 
            if not grid[rowNumber][i+1] == '': 
            
                if grid[rowNumber][i+1] == '#':
                    move_block_iron_right(rowNumber, currentState, startGrid, n, grid, i)
                    break

                        
                pushToRight(grid , rowNumber , i , startGrid , currentState)
                break

        if grid[rowNumber][i] == 'PM' and i+1 < n : 
            if not grid[rowNumber][i+1] == '':

                magnets = getMagnets(currentState.magnets , 'PM')

                moveMagnets(i+1  , rowNumber , currentState , startGrid , magnets)     

        i += 1


    # A method to check if there are iron pieces on left side of the magnets

def moveLeftIrons(columnNumber  , rowNumber , currentState , startGrid):

    from Actions.magnets import moveMagnets , getMagnets

    grid = currentState.grid
    i = columnNumber
    i -= 1

    while i >= 0 : 

        if  grid[rowNumber][i] == '#' and i-1 >= 0  : 
            if not grid[rowNumber][i-1] == '':

                if grid[rowNumber][i-1] == '#' or grid[rowNumber][i-1] == 'PM':
                    
                    move_block_iron_left(rowNumber, currentState, startGrid, grid, i)
                    break

                pushToLeft(grid , rowNumber , i , startGrid,currentState)
                break
        
        if  grid[rowNumber][i] == 'PM' and i-1 >= 0  :
            if not grid[rowNumber][i-1] == '':

                magnets = getMagnets(currentState.magnets , 'PM')

                moveMagnets(i-1  , rowNumber , currentState , startGrid , magnets)

        i -= 1





    # A method to check if there are iron pieces top of the magnets

def moveUpIrons(columnNumber  , rowNumber , currentState , startGrid):

    from Actions.magnets import moveMagnets , getMagnets


    grid = currentState.grid
    i = 0
    i += 1

    while i < rowNumber : 

        if  grid[i][columnNumber] == '#' and i-1 >= 0 : 

            if not grid[i-1][columnNumber] == '':

                pushToUP(grid , columnNumber , i , startGrid,currentState)

        if  grid[i][columnNumber] == 'PM' and i-1 >= 0 : 
            if not grid[i-1][columnNumber] == '':

                magnets = getMagnets(currentState.magnets , 'PM')

                moveMagnets(columnNumber  , i-1 , currentState , startGrid , magnets)

        i += 1


    # A method to check if there are iron pieces under the magnets

def moveDownIrons(columnNumber  , rowNumber , currentState , startGrid):
    
    from Actions.magnets import moveMagnets , getMagnets

    n = currentState.numRows
    grid = currentState.grid
    i = n-1
    i -= 1

    while i >  rowNumber: 

        if  grid[i][columnNumber] == '#' and i+1 < n : 
            if not grid[i+1][columnNumber] == '': 
           
                pushToDown(grid , columnNumber , i , startGrid,currentState)

        if  grid[i][columnNumber] == 'PM' and i+1 < n : 
            if not grid[i+1][columnNumber] == '':

                magnets = getMagnets(currentState.magnets , 'PM')

                moveMagnets(columnNumber, i+1 , currentState , startGrid , magnets)

        i -= 1

