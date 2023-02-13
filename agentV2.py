import math
import random
import pickle
import matplotlib.pyplot as plt
from abc import ABC

import numpy as np
import sklearn

from main import IAgent
from main import ABC


class QLearnAgentV2(IAgent, ABC):
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

    def updateTable(self, bucket, state, action, reward):
        # oldMax = max(self.qTable[bucket])
        # oldValOffset = (1 - self.learningRate) * (self.qTable[bucket][action])
        # # biasReward = ((1 - self.bias) / abs(state[0])) * reward
        # biasReward = (1 / abs(state[0])) * reward
        # # biasReward = reward
        # qValue = oldValOffset + self.learningRate * (biasReward + self.discount * oldMax)
        #
        # self.qTable[bucket][action] = qValue

        oldMax = max(self.qTable[bucket])
        biasReward = (1 / abs(state[0])+0.1) * reward
        qVal = (1-self.learningRate) * oldMax + self.learningRate * self.discount * biasReward
        self.qTable[bucket][action] = qVal

    def predict(self, state):

        cPos = math.floor(state[0]*1)
        cVel = math.floor(state[1]*1)
        pPos = math.floor(state[2]*4)
        pVel = math.floor(state[3]*1)

        return tuple([cVel,pVel])

    def policy(self, bucket, state) -> int:

        if bucket not in self.qTable.keys():
            # print("NEW")
            self.qTable[bucket] = [0,0]
            cPos = state[0]
            cVel = state[1]
            pPos = state[2]
            pVel = state[3]

            if(pVel< -1):
                return 0
            elif(pVel> 1):
                return 1
            else:
                return random.randint(0,1)

        return self.qTable[bucket].index(max(self.qTable[bucket]))

    def run(self) -> None:
        while self.episodeCount<self.maxEp:

            # INIT Episode
            state = self.env.reset()[0]
            isDone = False
            action = -1
            bucket = -1

            # Cycle Episode
            while not isDone:

                bucket = self.predict(state)
                action = self.policy(bucket, state)

                self.env.render()
                environment = self.env.step(action)


                state = environment[0]
                reward = environment[1]
                isDone = environment[2]

                self.scoreTable[self.episodeCount] += reward
                self.updateTable(bucket, state, action, reward)

            # END Episode
            self.updateTable(bucket, state, action, max(-self.episodeCount, self.penalty))
            # print(self.qTable)
            # print("EP COUNT: ", self.episodeCount)
            # print("REWARD: ", self.scoreTable[self.episodeCount])
            # self.printAvg(self.scoreTable)
            # print("-"*10)
            self.episodeCount+=1


        ### FINISHED INSTANCE
        # self.printTable()
        return self.printAvg(self.scoreTable)
