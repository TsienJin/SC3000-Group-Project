
from collections import namedtuple

Observation = namedtuple("observation", ("cartPos", "cartVel", "poleAngle", "poleVel"))

# Referenced as "experience" in the DQN paper
Record = namedtuple("record", ("state", "action", "nextState", "reward"))
