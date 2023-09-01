import tkinter as ent
from agent.brain import EntityBrain

class Entity():
    def __init__(self) -> None:        
        self.brain = EntityBrain()
        self.body = ent.Tk()
        self.bodyConf = ent.Label(self.body, bd=0, background='green')
        self.body.bind("<Escape>", lambda event: exit(1))
    
    def setActionAnimation(self, gifImageRight: str, gifImageLeft: str, frames: tuple):
        self.idleFrames = frames 
        self.animations = (
            [ent.PhotoImage(file=gifImageRight, format=f'gif -index {i}') for i in range(frames)], #frames
            [ent.PhotoImage(file=gifImageLeft, format=f'gif -index {i}') for i in range(frames)]
        )

    def materialize(self):
        self.bodyConf.pack()
        self.body.wm_overrideredirect(True)
        self.body.wm_attributes("-topmost", True)
        self.body.wm_attributes("-transparentcolor", 'green')
        
        self.entityAct()

        self.body.mainloop()
    
    def entityAct(self):
        self.moveToMouse()
        self.animateChar(0)

    def animateChar(self, anima: int):
        orientation = self.entityOrientation(self.brain.findObject(), self.body.winfo_x(), self.body.winfo_y())
        frame = self.animations[orientation][anima]
        self.bodyConf.configure(image=frame)
        anima += 1
        if anima == self.idleFrames :
            anima = 0
        self.body.after(100, self.animateChar, anima)
    
    def entityOrientation(self, objectPost, entity_x: int, entity_y: int): #0 atau 1 sementara x aja
        return self.brain.determineObjectPos(objectPost, entity_x + 110, entity_y)
    
    def moveChar(self, string: str):
        self.body.wm_geometry(string)
        self.body.after(10, self.moveToMouse)

    def moveToMouse(self):
        position = self.brain.findObject()
        #print(f"{position.x} and {position.y}")
        self.moveChar(f'180x180-{position.x}-{position.y}')
        return position
    
    def doSomething(self):
        position = self.brain.chooseAction()

        
    
    
        