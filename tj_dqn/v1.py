import os
import sys

from memory import Memory
from localTypes import Record, Observation

import matplotlib
from collections import namedtuple
import numpy as np
import torch
from torch import nn
from torch import optim
import torch.nn.functional as F


# from torch.utils.data import DataLoader

class DQN(nn.Module):

    def __init__(self,
                 n_obsv: int, n_actions: int, n_layer: int = 1, n_layerSize: int = 6,
                 learningRate: float = 0.0001, gamma: float = 0.95,
                 expDecay: float = 0.999, expMin: float = 0.001, expMax: float = 1.0,
                 _device: str = "cpu",
                 memory: Memory = Memory()):
        """

        :param n_obsv: size of observation space
        :param n_actions: size of action space
        :param n_layer: number of hidden layers
        :param n_layerSize: number of neurons per hidden layer
        :param learningRate:
        :param gamma: discount for future values
        :param expDecay:
        :param expMin:
        :param expMax:
        :param _device: defaults to "cpu"
        """

        super(DQN, self).__init__()

        # Ensuring that values are proper
        assert n_layer >= 0
        assert n_obsv > 0
        assert n_actions > 0
        assert n_layerSize > 0
        assert 0 < learningRate < 1
        assert 0 < gamma < 1
        assert 0 < expDecay < 1
        assert 0 < expMin < 1
        assert 0 < expMax <= 1

        self.learningRate = learningRate
        self.gamma = gamma
        self.expDecay = expDecay
        self.expMin = expMin
        self.expMax = expMax

        self.n_obsv = n_obsv
        self.n_actions = n_actions
        self.n_layer = n_layer
        self.n_layerSize = n_layerSize

        self.memory = memory

        self.layers = nn.ModuleList(self.__createLayers())
        self.optim = optim.Adam(self.parameters(), lr=self.learningRate)

        self.to(_device)

    def __createLayers(self):
        """
        Private method to generate neural network given the specified params in __init__()
        :return: [nn.Linear()]
        """
        # init layers starting with input shape to layer size
        layers = [nn.Linear(self.n_obsv, self.n_layerSize)]

        # creates more layers with specified layer size
        for _ in range(self.n_layer):
            layers.append(nn.Linear(self.n_layerSize, self.n_layerSize))

        # adds final output layer
        layers.append(nn.Linear(self.n_layerSize, self.n_actions))

        return layers

    def forward(self, x):
        """
        Processes the given state and returns a tensor with qValues for actions
        :param x: <torch.tensor> with shape (1,4) and type float32 | State of current observation as a tensor
        :return: <torch.tensor> with shape (1,2) | Tensor of qValues
        """
        assert (x.dim() == torch.randn(4).dim())
        for layer in self.layers:
            x = F.relu(layer(x))
        return x


if __name__ == '__main__':
    model = DQN(n_obsv=4, n_actions=2, n_layer=0, n_layerSize=4)
    print(model)

    egObsv = np.array([0.24, -2, 0.002, 4]).astype(np.float32)

    print(model.forward(torch.as_tensor(egObsv)))
    print(model.parameters())
