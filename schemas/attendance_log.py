from pydantic import BaseModel
from datetime import datetime

class AttendanceBase(BaseModel):
    student_id: int
    course_id: int
    present: bool

class AttendanceCreate(AttendanceBase):
    submitted_by: int

class AttendanceResponse(AttendanceBase):
    id: int
    submitted_by: int
    updated_at: datetime

    class Config:
        from_attributes = True
