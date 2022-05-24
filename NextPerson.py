from BlackboardNextClicker import next
from BlackboardBackClicker import back

from pynput import keyboard

PAUSED = False

def on_press(key):
    pass
    # try:
    #     print('alphanumeric key {0} pressed'.format(
    #         key.char))
    # except AttributeError:
    #     print('special key {0} pressed'.format(
    #         key))

def on_release(key):
    global PAUSED
    # print('{0} released'.format(
    #     key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    if key == keyboard.KeyCode.from_char('`'):
        if PAUSED:
            print("Resuming")
        else:
            print("Pausing")
        PAUSED = not PAUSED
    if not PAUSED:
        if key == keyboard.Key.right:
            print("Clicking next")
            next()
        if key == keyboard.Key.left:
            print("Clicking back")
            back()
    
# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
    
# # ...or, in a non-blocking fashion:
# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)
# listener.start()