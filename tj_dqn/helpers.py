from localTypes import *

import numpy as np


class ParseEnvironment:
    def __init__(self, environment:[float]):
        assert len(environment) == 4
        self.cartPos = environment[0]
        self.cartVel = environment[1]
        self.poleAngle = environment[2]
        self.poleVel = environment[3]

    def __str__(self):
        return f"cPOS: {self.cartPos}\tcVEL: {self.cartVel}\tpANG: {self.poleAngle}\tpVEL: {self.poleVel}"

    def toObservation(self) -> Observation:
        return Observation(self.cartPos, self.cartVel, self.poleAngle, self.poleVel)

    def toFloat32(self) -> [np.float32]:
        return np.array([self.cartPos, self.cartVel, self.poleAngle, self.poleVel], type=np.float32)


# class ParseStep:
#     def __init__(self):


def toRecord(state: Observation, action: int, nextState: Observation, reward: float) -> Record:
    assert action in [0, 1]
    return Record(state, action, nextState, reward)
