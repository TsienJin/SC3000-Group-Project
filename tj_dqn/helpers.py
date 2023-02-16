from types import *


def toObservation(cartPos: float, cartVel: float, poleAngle: float, poleVel: float) -> Observation:
    return Observation(cartPos, cartVel, poleAngle, poleVel)


def toRecord(state:Observation, action:int, nextState:Observation, reward:float) -> Record:
    assert action in [0, 1]
    return Record(state, action, nextState, reward)
