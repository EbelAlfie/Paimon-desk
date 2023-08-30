import tkinter as ent
from agent.brain import EntityBrain

class Entity():
    def __init__(self) -> None:
        self.animationTotal = 0
        self.brain = EntityBrain()
        self.body = ent.Tk()
        self.bodyConf = ent.Label(self.body, bd=0, background='green')
    
    def setActionAnimation(self, gifImage, frames):
        self.idleFrames = frames 
        self.animations = [ent.PhotoImage(file=gifImage, format=f'gif -index {i}') for i in range(frames)] #frames

    def materialize(self):
        self.bodyConf.pack()
        self.body.wm_overrideredirect(True)
        self.body.wm_attributes("-topmost", True)
        self.body.wm_attributes("-transparentcolor", 'green')
        
        self.animateChar(0)
        self.moveChar()

        self.body.mainloop()

    def animateChar(self, anima: int):
        frame = self.animations[anima]
        self.bodyConf.configure(image=frame)
        anima += 1
        if anima == self.idleFrames :
            anima = 0
        self.body.after(100, self.animateChar, anima)

    def moveChar(self):
        position = self.brain.findObject()
        self.body.wm_geometry(f'180x180-{position.x}-{position.y}')
        self.body.after(10, self.moveChar)