import pyautogui
import random as rand

class EntityBrain:
    def __init__(self) -> None:
        pass

    def findObject(self):
        return pyautogui.position()
    
    def chooseAction(self) -> int:
        action = rand.randint(0, 10)
        return action