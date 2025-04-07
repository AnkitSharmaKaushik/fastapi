from fastapi import APIRouter, Depends
from attendance_system.apps import database
from schemas.user import UserCreate
from auth.auth import hash_password

router = APIRouter()

@router.post("/register")
async def create_user(user: UserCreate):
    query = users.insert().values(
        full_name=user.full_name,
        username=user.username,
        email=user.email,
        password=hash_password(user.password),
        submitted_by=1,
        updated_at=datetime.utcnow()
    )
    user_id = await database.execute(query)
    return {"id": user_id, "message": "User created successfully"}
