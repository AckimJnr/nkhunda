from fastapi import FastAPI, APIRouter, Depends, HTTPException
from models.user import User
from config.db_config import collection
from models.schemas import all_users_data
import uuid
"""
Main module
"""


app = FastAPI()
router = APIRouter()


@router.get("/users/")
async def get_users():
    """
    Get all users
    """
    data = collection["user"].find()
    return all_users_data(data)

@router.post("/user/")
async def create_user(user: User):
    """
    Create a new user
    """
    try:
        result = collection["user"].insert_one(dict(user))
        return {"status_code": 200, "id":str(result.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"An error occurred: {e}")

app.include_router(router)
