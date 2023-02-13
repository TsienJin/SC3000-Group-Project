import math
import random
import pickle
import matplotlib.pyplot as plt
from abc import ABC

import numpy as np
import sklearn

from main import IAgent
from main import ABC


class QLearnAgentV1(IAgent, ABC):
    def __init__(self, maxEpisode:int=100, buckets:int=12, learningRate:float=0.5, bias:float=0.5, discount=0.5):
        if buckets<0 or buckets>100:
            raise ValueError("Invalid number of buckets")

        if maxEpisode<=0:
            raise ValueError("Invalid number for maxEpisode! Minimum 1")

        if learningRate<0 or learningRate>1:
            raise ValueError("Invalid learning rate")

        if bias<0 or bias>1:
            raise ValueError("Invalid bias")

        if discount<0 or discount>1:
            raise ValueError("Invalid discount")

        super().__init__(maxEpisode=maxEpisode)

        # DEFINE Local Attr
        self.buckets = buckets
        self.episodeCount = 0
        self.learningRate = learningRate
        self.bias = bias
        self.discount = discount

        # Setting up predicting model
        modelFile = open(f'./models/klearn_{self.buckets}.pkl', 'rb')
        self.model = pickle.load(modelFile)

        # DEFINE TABLE
        self.qTable = {}
        for i in range(self.buckets):
            self.qTable[i] = [0,0]

    def printTable(self):
        print(self.scoreTable)
        print(self.qTable)

    def updateTable(self, bucket, state, action, reward):
        if(reward<0):
            self.qTable[bucket][action] = self.qTable[bucket][action]-(abs(self.qTable[bucket][action])/10)
        else:
            oldMax = max(self.qTable[bucket])
            oldValOffset = (1 - self.learningRate) * (self.qTable[bucket][action])
            biasReward = ((self.bias / abs(state[2])) + ((1 - self.bias) / abs(state[0]))) * reward
            qValue = oldValOffset + self.learningRate * (biasReward + 0.7 * oldMax)

            self.qTable[bucket][action] = qValue


    def predict(self, state) -> int:
        return self.model.predict(np.array(state).astype(float).reshape(1,-1))[0]

    def policy(self, bucket) -> int:

        if min(self.qTable[bucket]) == 0:
            return random.randint(0, 1)

        return self.qTable[bucket].index(max(self.qTable[bucket]))

    def run(self) -> None:
        while self.episodeCount<self.maxEp:

            # INIT Episode
            state = self.env.reset()[0]
            isDone = False

            # Cycle Episode
            while not isDone:

                bucket = self.predict(state)
                action = self.policy(bucket)

                environment = self.env.step(action)


                state = environment[0]
                reward = environment[1]
                isDone = environment[2]

                self.scoreTable[self.episodeCount] += reward
                self.updateTable(bucket, state, action, reward)

            # END Episode
            self.updateTable(bucket, state, action, -6)
            print(self.qTable)
            print("EP COUNT: ", self.episodeCount)
            print("REWARD: ", self.scoreTable[self.episodeCount])
            self.printAvg(self.scoreTable)
            print("-"*10)
            self.episodeCount+=1


        ### FINISHED INSTANCE
        # self.printTable()
        return self.printAvg(self.scoreTable)
