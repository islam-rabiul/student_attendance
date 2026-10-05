from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

from . import schemas, models
from .database import engine, get_db
from . import crud

# Automatically create the database tables if they do not exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Attendance API", version="1.0")

@app.post("/attendance/", response_model=schemas.AttendanceResponse)
def create_attendance(attendance: schemas.AttendanceCreate, db: Session = Depends(get_db)):
    """API 1: Record student attendance by calling the CRUD function"""
    return crud.create_student_attendance_in_db(db=db, attendance=attendance)

@app.get("/attendance/", response_model=List[schemas.AttendanceResponse])
def get_attendance_records(db: Session = Depends(get_db)):
    """API 2: Fetch all student attendance records by calling the CRUD function"""
    return crud.get_all_attendance_from_db(db=db)