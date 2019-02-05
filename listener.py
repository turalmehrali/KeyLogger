
from pynput.mouse import Listener

def writetofile(x, y):
    print("Current position of mouse {0}".format(x, y))

with Listener(on_move=writetofile) as listener:
    listener.join()