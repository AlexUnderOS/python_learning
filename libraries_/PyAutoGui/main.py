import pyautogui

i = 0
while True:
    screensh_name = input("Screenshot name:")
    pyautogui.screenshot(rf"C:\Users\AlexOsta\Documents\~Programming\Python_learning\libraries_\PyAutoGui\screenshots_\{screensh_name}{i}.jpg")
    i = i+1
    a = input("You made a screenshoot!")