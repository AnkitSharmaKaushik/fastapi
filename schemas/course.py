from pydantic import BaseModel
from datetime import datetime

class CourseBase(BaseModel):
    course_name: str
    department_id: int
    semester: int
    class_name: str
    lecture_hours: int

class CourseCreate(CourseBase):
    submitted_by: int

class CourseResponse(CourseBase):
    id: int
    submitted_by: int
    updated_at: datetime

    class Config:
        from_attributes = True
