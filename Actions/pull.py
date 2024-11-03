

def pullToLeft(grid , rowNumber , i , startGrid , currentState):

    if grid[rowNumber][i-1] == 'O' or grid[rowNumber][i-1] == '.':
        if  grid[rowNumber][i-1] == 'O' :
            currentState.numGoals -= 1
        grid[rowNumber][i-1] = '#'
        
        handling_move_hrizontal_iron(grid, rowNumber, i, startGrid, currentState) 


def pullToRight(grid , rowNumber , i , startGrid,currentState):

    if grid[rowNumber][i+1] == 'O' or grid[rowNumber][i+1] == '.':
        if  grid[rowNumber][i+1] == 'O' :
            currentState.numGoals -= 1
        grid[rowNumber][i+1] = '#'
        
        handling_move_hrizontal_iron(grid, rowNumber, i, startGrid, currentState) 


def pullToDown(grid , columnNumber , i , startGrid,currentState):

    if grid[i+1][columnNumber] == 'O' or grid[i+1][columnNumber] == '.' :
        if  grid[i+1][columnNumber] == 'O' :
            currentState.numGoals -= 1
        grid[i+1][columnNumber] = '#'

        handling_move_vertical_iron(grid, columnNumber, i, startGrid, currentState)


def pullToUp(grid , columnNumber , i , startGrid,currentState):
    if grid[i-1][columnNumber] == 'O' or grid[i-1][columnNumber] == '.' :
        if  grid[i-1][columnNumber] == 'O' :
            currentState.numGoals -= 1
        grid[i-1][columnNumber] = '#'

        handling_move_vertical_iron(grid, columnNumber, i, startGrid, currentState)


def handling_move_hrizontal_iron(grid, rowNumber, i, startGrid, currentState):

    if startGrid[rowNumber][i] == 'O' :
        grid[rowNumber][i] = 'O'
        currentState.numGoals += 1
    else :
        grid[rowNumber][i] = '.'


def handling_move_vertical_iron(grid, columnNumber, i, startGrid, currentState):
    if startGrid[i][columnNumber] == 'O' :
        grid[i][columnNumber] = 'O'
        currentState.numGoals += 1

    else :
        grid[i][columnNumber] = '.'