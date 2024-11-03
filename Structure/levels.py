
from Structure.magnets import NegativeMagnets as Mag

class Level:
    
    levels = [
        #1
        {
            'numColumns': 4,
            'numRows': 3,
            'magnets': [Mag(2,0,'NM')], 
            'ironsPos': [(1, 2)],
            'goalsPos': [(1,1) , (1,3)], 
            'numSteps': 4,
            'blocks' : []
        },
        # 2
        {
            'numColumns': 5,
            'numRows': 5,
            'magnets': [Mag(4,0,'NM')], 
            'ironsPos': [(2, 1) ,(1,2) , (2,3) , (3,2)],
            'goalsPos': [(0,2) , (2,0) , (2,2) , (2, 4),(4,2)], 
            'numSteps': 5,
            'blocks' : []
        },
        # 15
        {
            'numColumns': 5,
            'numRows': 3,
            'magnets': [Mag(1,2,'NM') ,Mag(2,2,'PM')], 
            'ironsPos': [(0, 1) ,(0,3)],
            'goalsPos': [(0,0) , (0,2)  , (1, 4),(2,4)], 
            'numSteps': 5,
            'blocks' : []
        },
        #17
        {
            'numColumns': 4,
            'numRows': 4,
            'magnets': [Mag(3,3,'NM') ,Mag(0,0,'PM')], 
            'ironsPos': [(0, 2) ,(2,0)],
            'goalsPos': [(1,1) , (2,2)  , (1, 3),(3,1)], 
            'numSteps': 2,
            'blocks' : []
        },
        #18
        {
            'numColumns': 6,
            'numRows': 5,
            'magnets': [Mag(4,3) , Mag(4,2, 'PM')], 
            'ironsPos': [(0, 3) , (2,0) , (2,5)],
            'goalsPos': [(2,1), (2,2), (2,3) , (1,3) , (2,5)], 
            'numSteps': 2, 
            'blocks' : [(0,0),(0,1),(0,4),(0,5) , (1,0) ,(1,1) , (1,4) ,(1,5) ,(4,0),(4,1),(4,4),(4,5)]
        },
       
    ]

    
    def chooseLevel():

        try:

            level_num = int(input("Choose a level (1 ---> 5 ) : "))

            if 1 <= level_num <= 25:

                return Level.levels[level_num - 1]
            
            else:
                print("Invalid level number, Please choose a number between 1 and 25 " , '\n')

        except ValueError:
            print("Invalid input  , Please enter a number between 1 and 25 " , '\n')

       
    