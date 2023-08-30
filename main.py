from agent.creature import Entity

if __name__ == "__main__":
    frames = (90, 90)
    animationRight = './entity/paimon.gif' 
    animationLeft = './entity/paimonfliped.gif'
    paimon = Entity()
    paimon.setActionAnimation(animationRight, animationLeft, frames)
    paimon.materialize()