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
    def __init__(self, maxEpisode:int=100, visualise=False):
        super().__init__(maxEpisode=maxEpisode, visualise=visualise)

        # DEFINE Local Attr
        self.episodeCount = 0

        # DEFINE TABLE
        self.qTable = {}

    def policy(self):
        pass

    def getState(self):
        pass



    def run(self):
        pass
