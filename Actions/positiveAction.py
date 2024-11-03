from Actions.pull import pullToDown , pullToLeft , pullToRight , pullToUp

    # A method to check if there are iron pieces on right side of the magnets

def moveRightIrons(columnNumber  , rowNumber , currentState , startGrid):

    from Actions.magnets import moveMagnets , getMagnets

    n = currentState.numColumns
    grid = currentState.grid
    i = columnNumber
    i += 1

    while i < n : 

        if  grid[rowNumber][i] == '#' and i-1 > columnNumber  : 
            if not grid[rowNumber][i-1] == '': 

                pullToLeft(grid , rowNumber , i , startGrid , currentState)

        if grid[rowNumber][i] == 'NM' and i-1 > columnNumber  : 
            if not grid[rowNumber][i-1] == '':

                magnets = getMagnets(currentState.magnets , 'NM')

                moveMagnets(i-1  , rowNumber , currentState , startGrid , magnets)     

        i += 1
            


    # A method to check if there are iron pieces on left side of the magnets

def moveLeftIrons(columnNumber  , rowNumber , currentState , startGrid):

    from Actions.magnets import moveMagnets , getMagnets

    grid = currentState.grid
    i = columnNumber
    i -= 1
    while i >=  0 : 

        if  grid[rowNumber][i] == '#' and i+1 < columnNumber : 
            if not grid[rowNumber][i+1] == '' :

                pullToRight(grid , rowNumber , i , startGrid,currentState)

        if grid[rowNumber][i] == 'NM' and i+1 < columnNumber : 
            if not grid[rowNumber][i+1] == '' :

                magnets = getMagnets(currentState.magnets , 'NM')

                moveMagnets(i+1  , rowNumber , currentState , startGrid , magnets)     

        i -= 1





    # A method to check if there are iron pieces top of the magnets

def moveUpIrons(columnNumber  , rowNumber , currentState , startGrid):

    from Actions.magnets import moveMagnets , getMagnets

    grid = currentState.grid
    i = rowNumber
    i -= 1

    while i >= 0 : 

        if  grid[i][columnNumber] == '#' and i+1 < rowNumber : 
            if not grid[i+1][columnNumber] == '':

                pullToDown(grid , columnNumber , i , startGrid,currentState)
        
        if  grid[i][columnNumber] == 'NM' and i+1 < rowNumber : 
            if not grid[i+1][columnNumber] == '':

                magnets = getMagnets(currentState.magnets , 'NM')

                moveMagnets(columnNumber  , i+1 , currentState , startGrid , magnets)

        i -= 1





    # A method to check if there are iron pieces under the magnets

def moveDownIrons(columnNumber  , rowNumber , currentState , startGrid):
    
    from Actions.magnets import moveMagnets , getMagnets

    n = currentState.numRows
    grid = currentState.grid
    i = rowNumber
    i += 1
    while i <  n: 

        if  grid[i][columnNumber] == '#' and i-1 > rowNumber : 
            if not   grid[i-1][columnNumber] == '': 
           
                pullToUp(grid , columnNumber , i , startGrid,currentState)

        if  grid[i][columnNumber] == 'NM' and i-1 > rowNumber : 
            if not   grid[i-1][columnNumber] == '': 

                magnets = getMagnets(currentState.magnets , 'NM')

                moveMagnets(columnNumber  , i-1 , currentState , startGrid , magnets)


        i += 1




