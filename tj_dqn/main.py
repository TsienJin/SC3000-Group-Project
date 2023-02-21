import matplotlib

from memory import Memory
from v1 import DQN
from copy import deepcopy
from helpers import *
from localTypes import *

import torch

import gym

ENV = gym.make("CartPole-v1")

is_ipython = 'inline' in matplotlib.get_backend()
if is_ipython:
    from IPython import display



class Agent:
    # Q Value vals
    DISCOUNT = 0.99
    LEARNING_RATE = 0.0001
    GAMMA = 0.95

    # Epsilon GREEDY vals
    EPS = 0.5
    EPS_DECAY = 0.999
    EPS_MIN = 0.001
    EPS_MAX = 1.0

    # Memory vals
    MEM_SIZE = 50_000
    MIN_MEM_SIZE = 1_000
    MEM_BATCH = 64
    TARGET_UPDATE_FREQ = 5

    def __init__(self, maxEp:int=10_000, env=gym.make("CartPole-v1")):

        # Bootstrapping to maintain stability of prediction
        self.memory = Memory(maxCapacity=self.MEM_SIZE)
        self.model = DQN(n_obsv=4, n_actions=2, memory=self.memory)  # updates every iteration
        self.targetModel = deepcopy(self.model)  # updates only once threshold has been reached

        # Setting individual stats for the environment to run
        self.maxEpisode = maxEp
        self.env = env
        self.episodeCounter = 0

    def addToMem(self, record:Record):
        self.memory.push(record)

    def predict(self, environment:ParseEnvironment) -> int:
        res = self.targetModel.forward(environment.toTensor())
        return torch.argmax(res).detach().numpy()

    def evaluate(self) -> np.float32:
        pass

    def train(self):
        # TODO uncomment for actual training
        # if len(self.memory) < self.MIN_MEM_SIZE:
        #     return

        batch = self.memory.sample(size=self.MEM_BATCH)
        allStates = np.array([record.state for record in batch])  # need to check if this works; no intellisense


    def run(self):
        # thing = self.env.reset()
        # curThing = ParseEnvironment(thing[0])
        # print(self.predict(curThing))
        # print(self.env.reset())
        # print(self.env.step(0))
        #
        # curEnv = ParseEnvironment(*self.env.reset(), isDone=False, isTruncated=False)
        # print(curEnv.toEnvironment())
        #
        # nextEnv = ParseEnvironment(*self.env.step(0))
        # print(nextEnv.toEnvironment())

        while self.episodeCounter < self.maxEpisode:
            curEnv = ParseEnvironment(*self.env.reset())

            while curEnv.isDone is not True:
                print(curEnv)


        pass




if __name__ == '__main__':
    agent = Agent(maxEp=10)
    agent.run()
