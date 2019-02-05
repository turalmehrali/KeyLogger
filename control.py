
from pynput.mouse import Controller
from pynput.keyboard import Controller

def controlmouse():
    mouse = Controller()
    mouse.position = (700, 200)
def controlkeyboard():
    keyboard = Controller()
    keyboard.type("is this the real life?")

controlkeyboard()

#controlmouse()is this the real life?