import math
import random
import pickle
import matplotlib.pyplot as plt
from abc import ABC

import numpy as np
import sklearn

from main import IAgent
from main import ABC


class QLearnAgentV3(IAgent, ABC):
    def __init__(self, maxEpisode:int=100, learningRate:float=0.5, bias:float=0.5, discount=0.5, penalty=-1, visualise=False):
        if maxEpisode<=0:
            raise ValueError("Invalid number for maxEpisode! Minimum 1")

        if learningRate<0 or learningRate>1:
            raise ValueError("Invalid learning rate")

        if bias<0 or bias>1:
            raise ValueError("Invalid bias")

        if discount<0 or discount>1:
            raise ValueError("Invalid discount")

        super().__init__(maxEpisode=maxEpisode, visualise=visualise)

        # DEFINE Local Attr
        self.episodeCount = 0
        self.learningRate = learningRate
        self.bias = bias
        self.discount = discount
        self.penalty = penalty

        # DEFINE TABLE
        self.qTable = {}

    def printTable(self):
        print(self.scoreTable)
        print(self.qTable)

    def fetchTable(self, state):
        bucket = self.predict(state)
        if bucket not in self.qTable.keys():
            self.qTable[bucket] = [0,0]

        return self.predict(state)

    def updateTable(self, bucket, state, action, reward, prevState):

        if bucket not in self.qTable.keys():
            self.qTable[bucket] = [0,0]

        maxFutureQ = np.max(self.qTable[self.predict(state)])
        curQ = np.max(self.qTable[self.fetchTable(state)][action])

        newQ = (1-self.learningRate)*curQ + self.learningRate*(reward + self.discount*maxFutureQ)

        self.qTable[bucket][action] = newQ

    def predict(self, state):
        cPos = np.rint((state[0] * .25))
        cVel = np.rint((state[1] * 2))
        pPos = np.rint((state[2] * 1))
        pVel = np.rint((state[3] * 2))

        return tuple(np.array([cVel, pVel, pPos]).astype(np.int32))

    def policy(self, bucket, state) -> int:
        if bucket not in self.qTable.keys():
            self.qTable[bucket] = [0,0]
            return random.randint(0,1)

        return self.qTable[bucket].index(max(self.qTable[bucket]))


    def run(self):
        while self.episodeCount<self.maxEp:

            # INIT Episode
            state = self.env.reset()[0]
            prevState = state
            isDone = False
            action = None
            bucket = None

            # Cycle Episode
            while not isDone:

                bucket = self.predict(state)
                action = self.policy(bucket, state)

                self.env.render()
                environment = self.env.step(action)

                prevState = state
                state = environment[0]
                reward = environment[1]
                isDone = environment[2]

                self.scoreTable[self.episodeCount] += reward
                self.updateTable(bucket, state, action, reward, prevState)

            # END Episode
            self.updateTable(bucket, state, action, max(-self.episodeCount, self.penalty))
            self.episodeCount+=1


        ### FINISHED INSTANCE
        self.printTable()
        return self.printAvg(self.scoreTable)
