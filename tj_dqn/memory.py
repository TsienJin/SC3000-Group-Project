"""
Purpose of memory

If the network learned only from consecutive samples of experience as they occurred sequentially in the environment,
the samples would be highly correlated and would therefore lead to inefficient learning.
Taking random samples from replay memory breaks this correlation.

src: https://deeplizard.com/learn/video/Bcuj2fTH4_4

"""
import random
from collections import deque

from localTypes import Observation, Record


class Memory:
    def __init__(self, maxCapacity:int=10000):
        self.cap = maxCapacity
        self.memory = deque([], maxlen=maxCapacity)

    def __len__(self):
        return len(self.memory)

    def __str__(self):
        return f"""Memory() capacity [{self.__len__}/{self.cap}]"""

    def push(self, record:Record):
        self.memory.append(record)

    def sample(self, size:int):
        assert size>0
        return random.sample(self.memory, size)
