import tkinter as ent
from agent.brain import EntityBrain

class Entity():
    def __init__(self) -> None:
        self.animationTotal = 0
        
        self.brain = EntityBrain()
        self.body = ent.Tk()
        self.bodyConf = ent.Label(self.body, bd=0, background='green')
    
    def setActionAnimation(self, gifImageRight: str, gifImageLeft: str, frames: tuple):
        self.idleFrames = frames 
        self.animations = (
            [ent.PhotoImage(file=gifImageRight, format=f'gif -index {i}') for i in range(frames[0])], #frames
            [ent.PhotoImage(file=gifImageLeft, format=f'gif -index {i}') for i in range(frames[1])]
        )

    def materialize(self):
        self.bodyConf.pack()
        self.body.wm_overrideredirect(True)
        self.body.wm_attributes("-topmost", True)
        self.body.wm_attributes("-transparentcolor", 'green')
        
        self.animateChar(0)
        self.moveChar()

        self.body.mainloop()

    def animateChar(self, anima: int):
        orientation = self.entityOrientation(self.body.winfo_x(), self.body.winfo_y())
        frame = self.animations[orientation][anima]
        self.bodyConf.configure(image=frame)
        anima += 1
        if anima == self.idleFrames :
            anima = 0
        self.body.after(100, self.animateChar, anima)
    
    def entityOrientation(self, entity_x, entity_y): #0 atau 1 sementara x aja
        return self.brain.determineObjectPos(entity_x, entity_y)

    def moveChar(self):
        position = self.brain.findObject()
        self.body.wm_geometry(f'180x180-{position.x}-{position.y}')
        self.body.after(10, self.moveChar)