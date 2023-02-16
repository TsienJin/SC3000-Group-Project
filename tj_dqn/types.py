
from collections import namedtuple

Observation = namedtuple("observation", ("cartPos", "cartVel", "poleAngle", "poleVel"))
Record = namedtuple("record", ("state", "action", "nextState", "reward"))
