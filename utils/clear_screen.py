import os 

def cls():
    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name=='nt' else 'clear')