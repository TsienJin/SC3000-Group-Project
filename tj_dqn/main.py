import matplotlib

from memory import Memory
from v1 import DQN
from copy import deepcopy
from helpers import *
from localTypes import *

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
    MIN_MEM_SIZE = 10_000
    MIN_MEMORY_LEN = 1_000
    MIN_BATCH = 64
    TARGET_UPDATE_FREQ = 5

    def __init__(self, maxEp:int=10_000, env=gym.make("CartPole-v1")):

        # Bootstrapping to maintain stability of prediction
        self.memory = Memory(maxCapacity=self.MEM_SIZE)
        self.model = DQN(n_obsv=4, n_actions=2, memory=self.memory)
        self.targetModel = deepcopy(self.model)

        # Setting individual stats for the environment to run
        self.maxEpisode = maxEp
        self.env = env
        self.targetUpdateCounter = 0

    def addToMem(self, record:Record):
        self.memory.push(record)

    def run(self):
        print(self.env.reset())
        print(self.env.step(0))
        thing = self.env.reset()
        print(ParseEnvironment(thing[0]))
        curThing = ParseEnvironment(thing[0])
        print(curThing.toObservation().poleVel)




if __name__ == '__main__':
    agent = Agent(maxEp=100)
    agent.run()
