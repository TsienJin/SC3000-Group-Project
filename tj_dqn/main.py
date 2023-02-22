import random
import sys
import matplotlib

from memory import Memory
from v1 import DQN
from copy import deepcopy
from helpers import *
import torch

import gym

ENV = gym.make("CartPole-v1", render_mode="human")

is_ipython = 'inline' in matplotlib.get_backend()
if is_ipython:
    from IPython import display


class Agent:
    # Number of episodes
    MAX_EP = 1_000_000

    # Q Value vals
    DISCOUNT = 0.9
    LEARNING_RATE = 0.001

    # Epsilon GREEDY vals
    EPS = 0.9999
    EPS_DECAY = 0.999
    EPS_MIN = 0.05
    EPS_MAX = 1.0

    # Memory vals
    MEM_SIZE = 50_000
    MIN_MEM_SIZE = 1_000
    MEM_BATCH = 200
    TARGET_UPDATE_FREQ = 75

    def __init__(self, maxEp:int=10_000, env=gym.make("CartPole-v1")):

        # Bootstrapping to maintain stability of prediction
        self.memory = Memory(maxCapacity=self.MEM_SIZE)
        self.model = DQN(n_obsv=4, n_actions=2, n_layer=10, n_layerSize=10,learningRate=self.LEARNING_RATE, memory=self.memory)  # updates every iteration
        self.targetModel = deepcopy(self.model)  # updates only once threshold has been reached

        # Setting individual stats for the environment to run
        self.maxEpisode = maxEp
        self.env = env
        self.episodeCounter = 0
        self.totalReward = 0

    def __printStats(self):
        print(f"EP: {self.EPS:.3f} | MEM: {len(self.memory)} | EP: {self.episodeCounter} | AVG: {self.totalReward/self.episodeCounter:.5f}")

    def predict(self, environment:ParseEnvironment) -> int:
        if self.EPS < self.EPS_MIN:
            res = self.targetModel.forward(environment.toTensor())
            return torch.argmax(res).detach().numpy()
        else:
            # print("USING RANDOM")
            self.EPS = self.EPS * self.EPS_DECAY
            return random.randint(0,1)


    def getMaxQ(self, environment:ParseEnvironment) -> torch.tensor:
        res = self.targetModel.forward(environment.toTensor())
        return res.clone().detach().numpy()


    def train(self):
        if len(self.memory) < self.MIN_MEM_SIZE:
            return

        batch = self.memory.sample(size=self.MEM_BATCH)

        allStates = np.array([record.state for record in batch])  # need to check if this works; no intellisense
        predicted = [self.getMaxQ(record.state) for record in batch]
        predictedNew = [self.getMaxQ(record.nextState) for record in batch]

        oldValsToFit = []
        valsToFit = []

        for index, env in enumerate(batch):
            maxFutureQ = np.max(self.getMaxQ(env.nextState))

            if not env.state.isDone:
                newQ = env.reward + self.DISCOUNT * maxFutureQ
            else:
                newQ = env.reward

            oldFit = self.getMaxQ(env.state)
            toFit = deepcopy(oldFit)
            toFit[env.action] = (1-self.LEARNING_RATE)*oldFit[env.action] + self.LEARNING_RATE * newQ


            oldValsToFit.append(oldFit)
            valsToFit.append(toFit)

        loss = self.model.crit(torch.tensor(np.array(oldValsToFit), requires_grad=True), torch.tensor(np.array(valsToFit), requires_grad=True))
        self.model.optim.zero_grad()
        loss.backward()
        self.model.optim.step()

        if self.episodeCounter % self.TARGET_UPDATE_FREQ == 0:
            self.targetModel.load_state_dict(self.model.state_dict())


    def run(self):
        while self.episodeCounter < self.maxEpisode:
            self.episodeCounter += 1
            cReward = 0.0
            curEnv = ParseEnvironment(self.env.reset()[0], reward=1.0, isDone=False, isTruncated=False)

            while curEnv.isDone is not True:

                # interact with env
                action = self.predict(curEnv)
                prevEnv = curEnv
                curEnv = ParseEnvironment(*self.env.step(action))

                # save record of what just happened
                thisRecord = ParseRecord(prevEnv, action, curEnv, curEnv.reward)
                self.memory.push(thisRecord)

                # # train model
                self.train()

                # # update local variables
                cReward += curEnv.reward
                self.totalReward += curEnv.reward
                self.__printStats()



if __name__ == '__main__':
    agent = Agent(maxEp=1_000_000)
    agent.run()
