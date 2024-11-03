

class State : 
    
    def __init__(self , level):
        
        self.numColumns = level['numColumns']
        self.numRows = level['numRows']
        self.blocks = level['blocks']
        self.magnets = level['magnets']
        self.irons = level['ironsPos']
        self.goals = level['goalsPos']
        self.numGoals = len(self.goals)
        self.numSteps = level['numSteps']
        self.grid = self.build()

    def __eq__(self, other):
        return self.grid == other.grid

    def __hash__(self):
        return hash(str(self.grid))
    
    def build(self) : 

        grid = [ ['.' for _ in range(self.numColumns)] for _ in range(self.numRows)]

        for x, y in self.blocks : 
            grid[x][y] = ''

        for x, y in self.goals:
            grid[x][y] = 'O'

        for  magnet in self.magnets:

            self.checkGoals(grid[magnet.posX][magnet.posY])

            grid[magnet.posX][magnet.posY] = magnet.type
            

        for x, y in self.irons:

            self.checkGoals(grid[x][y])

            grid[x][y] = '#'

        

        return grid


    def printGrid(self) :

        for row in self.grid :
            for element in row : 
                print(element , end='  ')
            print()    

    def isTerminated(self) :
        if self.numGoals == 0 :
            print("<------- You are the winner ------->")
            return True
        if self.numSteps == 0 : 
            print("<------- You are the loser ------->")
            return True
    
    def isGoal(self) : 
        if self.numGoals == 0 and self.numSteps >= 0:
            return True
        return False
        
    def checkGoals(self,value) : 
        if value == 'O':
            self.numGoals -= 1

    
