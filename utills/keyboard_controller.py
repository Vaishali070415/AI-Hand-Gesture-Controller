import pyautogui
import time

pyautogui.FAILSAFE = False


class KeyboardController:

    def __init__(self):

        self.last_gesture = None
        self.cooldown = 0.25
        self.last_time = time.time()

    def execute(self, gesture):

        current_time = time.time()

        # Cooldown
        if gesture == self.last_gesture and (current_time - self.last_time) < self.cooldown:
            return

        self.last_gesture = gesture
        self.last_time = current_time

        # Release both keys first
        pyautogui.keyUp("right")
        pyautogui.keyUp("left")

        if gesture == "ACCELERATE":

            pyautogui.keyDown("right")
            print("ACCELERATE")

        elif gesture == "BRAKE":

            pyautogui.keyDown("left")
            print("BRAKE")

        else:

            pyautogui.keyUp("right")
            pyautogui.keyUp("left")