from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from apps.database import get_db
from apps import models, schemas

router = APIRouter(prefix="/attendance", tags=["Attendance"])

@router.post("/", response_model=schemas.AttendanceResponse)
def create_attendance_log(attendance: schemas.AttendanceCreate, db: Session = Depends(get_db)):
    db_attendance = models.AttendanceLog(**attendance.dict())
    db.add(db_attendance)
    db.commit()
    db.refresh(db_attendance)
    return db_attendance

@router.get("/", response_model=List[schemas.AttendanceResponse])
def get_attendance_logs(db: Session = Depends(get_db)):
    return db.query(models.AttendanceLog).all()
