from pydantic import BaseModel
from datetime import datetime

class DepartmentBase(BaseModel):
    department_name: str

class DepartmentCreate(DepartmentBase):
    submitted_by: int

class DepartmentResponse(DepartmentBase):
    id: int
    submitted_by: int
    updated_at: datetime

    class Config:
        from_attributes = True
