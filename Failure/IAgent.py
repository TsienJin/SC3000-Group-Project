from abc import ABC, abstractmethod
import gym


class IAgent(ABC):
    env = None
    maxEp = 0

    def __init__(self, maxEpisode:int=100000, visualise=False) -> None:
        self.maxEp = maxEpisode

        if visualise:
            self.env = gym.make("CartPole-v1", render_mode="human")
        else:
            self.env = gym.make("CartPole-v1")

        self.scoreTable = {}
        for i in range(self.maxEp):
            self.scoreTable[i] = 0
        pass

    @classmethod
    def printAvg(cls, scoreTable):
        count=0
        total=0
        for key, val in scoreTable.items():
            if scoreTable[key] > 0:
                count+=1
                total+=scoreTable[key]

        rollAvg = total/count

        print(f"ROLLING AVG: {total/count:.2f}")
        return rollAvg

    @abstractmethod
    def run(self) -> float:
        pass
