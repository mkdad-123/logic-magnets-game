import time

def timing_function(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time()
        print(f"Function {f.__name__} took {end_time - start_time} seconds to execute")
        return result
    return wrapper


import os
def clear_screen():
    if os.name == 'nt':
        os.system('cls') 

def display_path(path):
    for state in path:
        clear_screen()
        state.printGrid()
        print("-----------------")
        print(f"number of the goals : {state.numGoals}")
        print(f"number of the steps : {state.numSteps}")
        time.sleep(2)