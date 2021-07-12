import keyboard
import time


# keyboard.add_hotkey("ctrl+alt+p", lambda: print("CTRL+ALT+P Pressed!"))


# # check if a ctrl is pressed
# print(keyboard.is_pressed('ctrl'))


# # press space
# keyboard.send("ctrl+s")

# # send ALT+F4 in the
# same time, and then send space,
# # (be carful, this will close any current open window)
# # keyboard.send("alt+F4, space")

# # press CTRL button
# keyboard.press("ctrl")
# # release the CTRL button
# keyboard.release("ctrl")

# time.sleep(1)

# keyboard.write("Python Programming is always fun!", delay=0.1)

# record all keyboard clicks until esc is clicked
events = keyboard.record('enter')
# play these events
keyboard.play(events)

# print all typed strings in the events
print(list(keyboard.get_typed_strings(events)))

keyboard.on_release(lambda e: print(e.name))
# time.sleep(4)
