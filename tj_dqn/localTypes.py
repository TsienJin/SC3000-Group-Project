
from collections import namedtuple

Observation = namedtuple("observation", ("cartPos", "cartVel", "poleAngle", "poleVel"))

Environment = namedtuple("environment", ("observation", "reward", "isDone", "isTruncated"))

Record = namedtuple("record", ("state", "action", "nextState", "reward", "qValue"))
