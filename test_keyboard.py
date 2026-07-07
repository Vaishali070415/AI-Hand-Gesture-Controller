import pyautogui
import time

print("Click on Hill Climb game in 5 seconds...")

time.sleep(5)

print("Accelerate")
pyautogui.keyDown("right")

time.sleep(3)

pyautogui.keyUp("right")

print("Brake")
pyautogui.keyDown("left")

time.sleep(3)

pyautogui.keyUp("left")

print("Done")