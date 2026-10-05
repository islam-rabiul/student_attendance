from datetime import date
from pydantic import BaseModel

class AttendanceCreate(BaseModel):
    student_name: str
    roll_number: str
    date: date
    status: str

    class Config:
        from_attributes = True

class AttendanceResponse(AttendanceCreate):
    id: int

    class Config:
        from_attributes = True