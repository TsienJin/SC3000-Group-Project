from localTypes import *

import numpy as np


class ParseEnvironment:
    def __init__(self, cartPos: float, cartVel: float, poleAngle: float, poleVel: float):
        self.cartPos = cartPos
        self.cartVel = cartVel
        self.poleAngle = poleAngle
        self.poleVel = poleVel

    def toObservation(self) -> Observation:
        return Observation(self.cartPos, self.cartVel, self.poleAngle, self.poleVel)

    def toFloat32(self) -> [np.float32]:
        return np.array([self.cartPos, self.cartVel, self.poleAngle, self.poleVel], type=np.float32)


# class ParseStep:
#     def __init__(self):


def toRecord(state: Observation, action: int, nextState: Observation, reward: float) -> Record:
    assert action in [0, 1]
    return Record(state, action, nextState, reward)
