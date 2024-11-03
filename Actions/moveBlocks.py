from Actions.push import pushToDown,pushToLeft,pushToRight,pushToUP

def move_block_iron_left(rowNumber, currentState, startGrid, grid, i):

    from Actions.magnets import moveMagnets,getMagnets

    j = i
    stack = []

    while j > 0 and (grid[rowNumber][j] == '#' or grid[rowNumber][j] == 'PM'):

        stack.append(j)
        j -= 1
        
    while(len(stack) > 0):

        top = stack.pop()

        if(grid[rowNumber][top] == 'PM') :

            magnets = getMagnets(currentState.magnets , 'PM')
            moveMagnets(top-1 , rowNumber , currentState , startGrid ,magnets)

        else :
            pushToLeft(grid , rowNumber , top , startGrid , currentState)



def move_block_iron_right(rowNumber, currentState, startGrid, n, grid, i):

    from Actions.magnets import moveMagnets,getMagnets

    j = i
    stack = []
    while j < n-1 and (grid[rowNumber][j] == '#' or grid[rowNumber][j] == 'PM'):

        stack.append(j)
        j += 1
                
    while(len(stack) > 0):

        top = stack.pop()

        if(grid[rowNumber][top] == 'PM') :

            magnets = getMagnets(currentState.magnets , 'PM')
            moveMagnets(top+1 , rowNumber , currentState , startGrid ,magnets)

        else :
            pushToRight(grid , rowNumber , top , startGrid , currentState)


