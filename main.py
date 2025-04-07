from fastapi import FastAPI
from .database import engine, Base

# Import all route files
from routes import user, student, attendance_log, department, course


# Initialize FastAPI
app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Register all routers
app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(student.router, prefix="/students", tags=["Students"])
app.include_router(attendance_log.router, prefix="/attendance", tags=["Attendance"])
app.include_router(department.router, prefix="/departments", tags=["Departments"])
app.include_router(course.router, prefix="/courses", tags=["Courses"])

# Root Endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the Attendance Management System API"}
