from sqlalchemy import Table, Column, Integer, String, ForeignKey, DateTime, Boolean, func
from .database import metadata

# Users Table
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("type", String(50), nullable=False),
    Column("full_name", String(100), nullable=False),
    Column("username", String(50), unique=True, nullable=False),
    Column("email", String(100), unique=True, nullable=False),
    Column("password", String(255), nullable=False),
    Column("submitted_by", Integer, ForeignKey("users.id"), nullable=True),
    Column("updated_at", DateTime, server_default=func.now(), onupdate=func.now()),
)

# Departments Table
departments = Table(
    "departments",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("department_name", String(100), nullable=False),
    Column("submitted_by", Integer, ForeignKey("users.id"), nullable=True),
    Column("updated_at", DateTime, server_default=func.now(), onupdate=func.now()),
)

# Students Table
students = Table(
    "students",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("full_name", String(100), nullable=False),
    Column("department_id", Integer, ForeignKey("departments.id"), nullable=False),
    Column("class", String(50), nullable=False),
    Column("submitted_by", Integer, ForeignKey("users.id"), nullable=True),
    Column("updated_at", DateTime, server_default=func.now(), onupdate=func.now()),
)

# Courses Table
courses = Table(
    "courses",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("course_name", String(100), nullable=False),
    Column("department_id", Integer, ForeignKey("departments.id"), nullable=False),
    Column("semester", Integer, nullable=False),
    Column("class", String(50), nullable=False),
    Column("lecture_hours", Integer, nullable=False),
    Column("submitted_by", Integer, ForeignKey("users.id"), nullable=True),
    Column("updated_at", DateTime, server_default=func.now(), onupdate=func.now()),
)

# Attendance Log Table (Connected to Students & Courses)
attendance_log = Table(
    "attendance_log",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("student_id", Integer, ForeignKey("students.id"), nullable=False),
    Column("course_id", Integer, ForeignKey("courses.id"), nullable=False),
    Column("present", Boolean, nullable=False, default=False),
    Column("submitted_by", Integer, ForeignKey("users.id"), nullable=True),
    Column("updated_at", DateTime, server_default=func.now(), onupdate=func.now()),
)
