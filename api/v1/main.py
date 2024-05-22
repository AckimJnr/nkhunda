from fastapi import FastAPI, APIRouter, Depends, HTTPException
from models.user import User
from config.db_config import collection
from models.schemas import all_users_data
from bson.objectid import ObjectId
from datetime import datetime
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
        return {"status_code": 201, "id":str(result.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"An error occurred: {e}")

@router.put("/user/{user_id}")
async def update_user(user_id: str, updated_user: User):
    """
    Update a user
    """
    try:
        user_id = ObjectId(user_id)
        existing_user = collection["user"].find_one({"_id": user_id})

        if not existing_user:
            return HTTPException(status_code=404, detail=f"User not found")
        
        update_user.updated_at = datetime.timestamp(datetime.now())
        result = collection["user"].update_one({"_id": user_id}, {"$set":dict(updated_user)})
        return {"status_code": 200, "message":"User Updated Successfully"}

    except Exception as e:
        return HTTPException(status_code=500, detail=f"An error occured {e}")


@router.delete("/user/{user_id}")
async def delete_user(user_id: str):
    """
    Delete a single user
    """
    try:
        user_id = ObjectId(user_id)
        existing_user = collection["user"].find_one({"_id": user_id})

        if not existing_user:
            return HTTPException(status_code=404, detail=f"User not found")
        
        update_user.updated_at = datetime.timestamp(datetime.now())
        result = collection["user"].delete_one({"_id": user_id})
        return {"status_code": 200, "message":"User Deleted Successfully"}

    except Exception as e:
        return HTTPException(status_code=500, detail=f"An error occured {e}")
    
app.include_router(router)
