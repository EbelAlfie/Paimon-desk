from agent.creature import Entity

if __name__ == "__main__":
    frames = 90
    animation = './entity/paimon.gif' 
    paimon = Entity()
    paimon.setActionAnimation(animation, frames)
    paimon.materialize()