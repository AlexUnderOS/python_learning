import keyboard as kb

kb.add_abbreviation("h", "hello")
# #h + space == hello

#
#
kb.add_hotkey("esc", lambda: kb.write("Python programming is funny!", delay=0.1))
#
#

# i = 10
# for j in range(i):
#     kb.wait("alt")
#     print(j+1)
    
#    
#

#Be careful about this!
# events = kb.record("alt")
# kb.play(events)
# kb.wait()

#
#

# while True:
#     kb.wait("s")
#     kb.press("ctrl+shift+s")
    
#
#

