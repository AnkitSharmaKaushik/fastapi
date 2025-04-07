from pydantic import BaseModel
from datetime import datetime

class StudentBase(BaseModel):
    full_name: str
    department_id: int
    class_name: str

class StudentCreate(StudentBase):
    submitted_by: int

class StudentResponse(StudentBase):
    id: int
    submitted_by: int
    updated_at: datetime

    class Config:
        from_attributes = True
