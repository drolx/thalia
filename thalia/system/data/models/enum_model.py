from sqlalchemy import Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ScheduleStatus(Enum):
    Disabled = 1
    Paused = 2
    Running = 3


class TaskStatus(Enum):
    Queued = 1
    Running = 2
    Completed = 3
    Error = 4
