def pushToRight(grid , rowNumber , i , startGrid , currentState):
     
    if grid[rowNumber][i+1] == 'O' or grid[rowNumber][i+1] == '.':
        if  grid[rowNumber][i+1] == 'O' :
            currentState.numGoals -= 1
        grid[rowNumber][i+1] = '#'
        
        if startGrid[rowNumber][i] == 'O' :
            grid[rowNumber][i] = 'O'
            currentState.numGoals += 1
        else :
            grid[rowNumber][i] = '.' 



def pushToLeft(grid , rowNumber , i , startGrid , currentState):
     
    if grid[rowNumber][i-1] == 'O' or grid[rowNumber][i-1] == '.':
        if  grid[rowNumber][i-1] == 'O' :
            currentState.numGoals -= 1

        grid[rowNumber][i-1] = '#'

        if startGrid[rowNumber][i] == 'O' :
            grid[rowNumber][i] = 'O'
            currentState.numGoals += 1

        else :
            grid[rowNumber][i] = '.' 


def pushToUP(grid , columnNumber , i , startGrid , currentState):

    if grid[i-1][columnNumber] == 'O' or grid[i-1][columnNumber] == '.' :
        if  grid[i-1][columnNumber] == 'O' :
            currentState.numGoals -= 1
        grid[i-1][columnNumber] = '#'

    
        if startGrid[i][columnNumber] == 'O' :
            grid[i][columnNumber] = 'O'
            currentState.numGoals += 1

        else :
            grid[i][columnNumber] = '.'



def pushToDown(grid , columnNumber , i , startGrid , currentState):
    
    if grid[i+1][columnNumber] == 'O' or  grid[i+1][columnNumber] == '.' :
        if  grid[i+1][columnNumber] == 'O' :
            currentState.numGoals -= 1
        grid[i+1][columnNumber] = '#'

        if startGrid[i][columnNumber] == 'O' :
            grid[i][columnNumber] = 'O'
            currentState.numGoals += 1

        else :
            grid[i][columnNumber] = '.'