from IAgent import ABC, abstractmethod
from IAgent import IAgent
import sys
import agentV2
import warnings
warnings.filterwarnings("ignore")  # YOLO


if __name__ == "__main__":
    vis = False
    if len(sys.argv)>1:
        vis=True

    score = {}
    for i in range(25):
        item = agentV2.QLearnAgentV2(maxEpisode=200, learningRate=0.4, bias=0.8, discount=0.5, penalty=-4, visualise=vis)
        score[i] = item.run()
        print(score[i])

    print(score)
