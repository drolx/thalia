from sqlalchemy import Enum, Column, Integer, String, Sequence, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from thalia.system.data.models.enum_model import TaskStatus

Base = declarative_base()


class Queue(Base):
    __tablename__ = "queues"

    id = Column(Integer, Sequence("queue_id_seq"), primary_key=True)
    schedule_id = Column(Integer, ForeignKey("schedules.id"))
    status = Column(Enum(TaskStatus), nullable=False)
    startedAt = Column(String, nullable=True)
    completedAt = Column(String, nullable=True)
    result = Column(String, nullable=True)
