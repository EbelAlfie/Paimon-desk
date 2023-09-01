import pyautogui
from random import randint, choices

class EntityBrain:
    def __init__(self) -> None:
        self.objTarget = [self.randomLoc(), self.findObject()]
        pass

    def findObject(self) -> pyautogui.Point:
        return pyautogui.position() 
    
    def randomLoc(self) -> pyautogui.Point:
        x = randint(0, 1920)
        y = randint(0, 1080)
        return pyautogui.Point(x, y)
    
    def determineObjectPos(self, objectPost, my_x, my_y):
        if (objectPost.x - my_x > 0) : return 0
        else: return 1
    
    def chooseAction(self):
        # action = choices(population= self.objTarget, weights=[0.95, 0.5])[0]
        action = randint(0, 1)
        return self.objTarget[action]