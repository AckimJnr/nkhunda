from fastapi import APIRouter, HTTPException
from bson.objectid import ObjectId
from datetime import datetime
from models.group import Group
from config.db_config import collection
from models.schemas import all_groups_data

router = APIRouter(
    prefix="/api/v1",
    tags=["Group"],
    responses={404: {"description": "Not found"}},
)


#group routes
@router.get("/groups/")
async def get_groups():
    """
    Get all groups
    """
    data = collection["group"].find()
    return all_groups_data(data)

@router.post("/group/")
async def create_group(group: Group):
    """
    Create a new group
    """
    try:
        result = collection["group"].insert_one(dict(group))
        return {"status_code": 201, "id":str(result.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"An error occurred: {e}")

@router.put("/group/{group_id}")
async def update_group(group_id: str, updated_group: Group):
    """
    Update a group
    """
    try:
        group_id = ObjectId(group_id)
        existing_group = collection["group"].find_one({"_id": group_id})

        if not existing_group:
            return HTTPException(status_code=404, detail=f"Group not found")
        
        update_group.updated_at = datetime.timestamp(datetime.now())
        result = collection["group"].update_one({"_id": group_id}, {"$set":dict(updated_group)})
        return {"status_code": 200, "message":"Group Updated Successfully"}

    except Exception as e:
        return HTTPException(status_code=500, detail=f"An error occured {e}")

@router.delete("/group/{group_id}")
async def delete_group(group_id: str):
    """
    Delete a single group
    """
    try:
        group_id = ObjectId(group_id)
        existing_group = collection["group"].find_one({"_id": group_id})

        if not existing_group:
            return HTTPException(status_code=404, detail=f"Group not found")
        
        update_group.updated_at = datetime.timestamp(datetime.now())
        result = collection["group"].delete_one({"_id": group_id})
        return {"status_code": 200, "message":"Group Deleted Successfully"}

    except Exception as e:
        return HTTPException(status_code=500, detail=f"An error occured {e}")