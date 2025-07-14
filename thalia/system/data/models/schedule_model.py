from sqlalchemy import (
    UniqueConstraint,
    Enum,
    Column,
    Integer,
    String,
    Boolean,
    Sequence,
)
from sqlalchemy.ext.declarative import declarative_base

from thalia.system.data.models.enum_model import ScheduleStatus

Base = declarative_base()


class Schedule(Base):
    __tablename__ = "schedules"
    __table_args__ = UniqueConstraint("name", name="uq_schedule_name")

    id = Column(Integer, Sequence("schedule_id_seq"), primary_key=True)
    active = Column(Boolean, nullable=False)
    status = Column(Enum(ScheduleStatus), nullable=False)
    name = Column(String, nullable=False)
    cron = Column(String, nullable=False)
    lastExecuted = Column(String, nullable=False)
    description = Column(String, nullable=True)
