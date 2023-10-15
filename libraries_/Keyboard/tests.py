import keyboard as kb
import os
import webbrowser

path = r"C:\WINDOWS\system32\cmd.exe"

def open_command_prompt():
    command = f"start {path}"
    os.system(command)
    
def open_web_guide():
    url = "https://stackabuse.com/guide-to-pythons-keyboard-module/"
    webbrowser.open(url)

kb.add_hotkey("esc", open_command_prompt)
kb.add_hotkey("f1", open_web_guide)

kb.wait()

# url = "https://stackabuse.com/guide-to-pythons-keyboard-module/"
# webbrowser.open(url)