from Actions.magnets import moveNegativeMagnets,movePositiveMagnets

class GamePlay:

    def __init__(self, startState , currentState):

        self.startState = startState

        self.currentState = currentState


    def play(self) :
        
        while(True) :

            try : 

                magnetType = input('choose a magnets ( NM or PM ) : ')

                x = int(input("What is number row : "))

                y = int(input("What is number clumn : "))
                
                if magnetType not in ['NM', 'PM']:
                    
                    raise ValueError("Invalid magnet type. Please choose 'NM' or 'PM'.")
            
                if magnetType == 'NM' : 

                    moveNegativeMagnets(y , x , self.currentState , self.startState ,magnetType )
                else : 
                    movePositiveMagnets(y , x , self.currentState , self.startState , magnetType)

                print('\n' , "{---------Now,This your grid---------}" , '\n')

                self.currentState.printGrid()

                print(f"number of the goals : {self.currentState.numGoals}")
                print(f"number of the steps : {self.currentState.numSteps}")

                if(self.currentState.isTerminated()):
                    break

            except ValueError as ve:

                print(f"Input error: {ve}")

            except Exception as e:

                print(f"An error occurred: {e}")
            

