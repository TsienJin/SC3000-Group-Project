"""
Purpose of memory

If the network learned only from consecutive samples of experience as they occurred sequentially in the environment,
the samples would be highly correlated and would therefore lead to inefficient learning.
Taking random samples from replay memory breaks this correlation.

src: https://deeplizard.com/learn/video/Bcuj2fTH4_4

"""
import random
from collections import deque

from helpers import ParseEnvironment, ParseRecord
from localTypes import Observation, Record, Environment


class Memory:
    def __init__(self, maxCapacity:int=10000):
        self.cap = maxCapacity
        self.memory = deque(maxlen=self.cap)

    def __len__(self) -> int:
        return self.memory.__len__()

    def __str__(self) -> str:
        return f"""Memory() capacity [{self.__len__}/{self.cap}]"""


    def __getInsertIndex(self, record:ParseRecord):

        if self.__len__()==0:
            return 0

        n = 0

        try:
            while record < self.memory[n]:
                n += 1
        finally:
            return n


    def push(self, record:ParseRecord) -> None:
        self.memory.insert(self.__getInsertIndex(record), record)

    def sample(self, size:int) -> [ParseRecord]:
        assert size>0

        return list(self.memory)[0:size]

