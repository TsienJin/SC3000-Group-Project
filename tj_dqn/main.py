from memory import Memory
from v1 import DQN
from copy import deepcopy
from helpers import *
from localTypes import *


class Agent:
    MEM_SIZE = 50_000
    MIN_MEM_SIZE = 10_000
    MIN_MEMORY_LEN = 1_000
    DISCOUNT = 0.99
    LEARNING_RATE = 0.0001
    GAMMA = 0.95
    EPS = 0.5
    EPS_DECAY = 0.999
    EPS_MIN = 0.001
    EPS_MAX = 1.0
    MIN_BATCH = 64
    TARGET_UPDATE_FREQ = 5

    def __init__(self):

        self.memory = Memory(maxCapacity=self.MEM_SIZE)
        self.model = DQN(n_obsv=4, n_actions=2, memory=self.memory)
        self.targetModel = deepcopy(self.model)

        self.targetUpdateCounter = 0

    def addToMem(self, record:Record):
        self.memory.push(record)





if __name__ == '__main__':
    agent = Agent()
