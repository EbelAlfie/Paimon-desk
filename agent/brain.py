import pyautogui
import random as rand

class EntityBrain:
    def __init__(self) -> None:
        pass

    def findObject(self):
        return pyautogui.position()
    
    def determineObjectPos(self, my_x, my_y):
        objectPos = self.findObject()
        if (objectPos.x - my_x > 0) : return 0
        else: return 1
    
    def chooseAction(self) -> int:
        action = rand.randint(0, 10)
        return action