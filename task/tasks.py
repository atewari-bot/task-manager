
from dataclasses import dataclass
from enum import Enum, auto

class Status(Enum):
    TODO = 1
    WIP = 2
    COMPLETED = 3
    REJECTED = 4

@dataclass
class Task:
    id: str
    user_id: str
    description: str
    status: Status