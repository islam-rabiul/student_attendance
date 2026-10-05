from sqlalchemy import Column, Integer, String, Date
from .database import Base

class StudentAttendance(Base):
    __tablename__ = "student_attendance"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    student_name = Column(String, index=True, nullable=False)
    roll_number = Column(String, unique=True, index=True, nullable=False)
    date = Column(Date, nullable=False)
    status = Column(String, nullable=False)