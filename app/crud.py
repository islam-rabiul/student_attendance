from sqlalchemy.orm import Session
from sqlalchemy import text
from . import schemas


def create_student_attendance_in_db(db: Session, attendance: schemas.AttendanceCreate):
    """Executes Raw SQL INSERT statement and returns the newly created record"""
    query = text("""
        INSERT INTO student_attendance (student_name, roll_number, date, status)
        VALUES (:student_name, :roll_number, :date, :status)
        RETURNING id, student_name, roll_number, date, status;
    """)

    # attendance.model_dump() automatically converts the Pydantic model into a dictionary
    result = db.execute(query, attendance.model_dump())

    db.commit()

    # Fetch and return the inserted row
    return result.fetchone()


def get_all_attendance_from_db(db: Session):
    """Executes Raw SQL SELECT statement to fetch all attendance records"""
    query = text("SELECT id, student_name, roll_number, date, status FROM student_attendance;")
    result = db.execute(query)

    # Fetch and return all rows
    return result.fetchall()