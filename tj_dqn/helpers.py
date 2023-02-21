from localTypes import *

import numpy as np

import torch


class ParseEnvironment:
    def __init__(self, environment:[float], reward:float, isDone:bool=False, isTruncated:bool=False, *args):
        assert len(environment) == 4
        self.cartPos = environment[0]
        self.cartVel = environment[1]
        self.poleAngle = environment[2]
        self.poleVel = environment[3]

        self.reward = reward
        self.isDone = isDone
        self.isTruncated = isTruncated

    def __str__(self):
        return f"""
        cPOS: {self.cartPos}\tcVEL: {self.cartVel}\tpANG: {self.poleAngle}\tpVEL: {self.poleVel}\n
        reward: {self.reward}\tisDone: {}
        """


    def toObservation(self) -> Observation:
        return Observation(self.cartPos, self.cartVel, self.poleAngle, self.poleVel)

    def toTensor(self):
        return torch.FloatTensor((self.cartPos, self.cartVel, self.poleAngle, self.poleVel))

    def toFloat32(self) -> [np.float32]:
        return np.array([self.cartPos, self.cartVel, self.poleAngle, self.poleVel], type=np.float32)

    def toEnvironment(self) -> Environment:
        return Environment(self.toObservation(), self.reward, self.isDone, self.isTruncated)


class ParseStep:
    def __init__(self, state: Observation, action: int, nextState: Observation, reward: float):
        assert action in [0, 1]
        self.state = state
        self.action = action
        self.nextState = nextState
        self.reward = reward

    def toRecord(self) -> Record:
        return Record(self.state, self.action, self.nextState, self.reward)
