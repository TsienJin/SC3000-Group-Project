from memory import Memory
from v1 import DQN
from copy import deepcopy
from helpers import *
from localTypes import *


class Agent:
    MEM_SIZE = 50_000
    MIN_MEMORY_LEN = 1_000
    DISCOUNT = 0.99
    LEARNING_RATE = 0.0001
    GAMMA = 0.95
    EXP_DECAY = 0.999
    EXP_MIN = 0.001
    EXP_MAX = 1.0

    def __init__(self):

        self.memory = Memory(maxCapacity=self.MEM_SIZE)
        self.model = DQN(n_obsv=4, n_actions=2, memory=self.memory)
        self.targetModel = deepcopy(self.model)

    def





if __name__ == '__main__':
    agent = Agent()
