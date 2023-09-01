from agent.creature import Entity

if __name__ == "__main__":
    frames = 90
    animationRight = './entity/paimonRight.gif' 
    animationLeft = './entity/paimonLeft.gif'
    paimon = Entity()
    paimon.setActionAnimation(animationRight, animationLeft, frames)
    paimon.materialize()