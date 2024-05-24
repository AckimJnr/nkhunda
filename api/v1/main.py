from fastapi import FastAPI, APIRouter, Depends, HTTPException
from models.user import User
from models.app import App
from models.organisation import Organisation as Org
from models.message import Message
from models.group import Group
from config.db_config import collection
from models.schemas import *
from bson.objectid import ObjectId
from datetime import datetime
"""
Main module
"""


app = FastAPI()
router = APIRouter()

# user routers
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


#organisaton routes
@router.get("/orgs/")
async def get_orgs():
    """
    Get all organisations
    """
    data = collection["org"].find()
    return all_orgs_data(data)

@router.post("/org/")
async def create_org(org: Org):
    """
    Create a new organisation
    """
    try:
        result = collection["org"].insert_one(dict(org))
        return {"status_code": 201, "id":str(result.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"An error occurred: {e}")

@router.put("/org/{org_id}")
async def update_org(org_id: str, updated_org: Org):
    """
    Update an organisation
    """
    try:
        org_id = ObjectId(org_id)
        existing_org = collection["org"].find_one({"_id": org_id})

        if not existing_org:
            return HTTPException(status_code=404, detail=f"Organisation not found")
        
        update_org.updated_at = datetime.timestamp(datetime.now())
        result = collection["org"].update_one({"_id": org_id}, {"$set":dict(updated_org)})
        return {"status_code": 200, "message":"Organisation Updated Successfully"}

    except Exception as e:
        return HTTPException(status_code=500, detail=f"An error occured {e}")

@router.delete("/org/{org_id}")
async def delete_org(org_id: str):
    """
    Delete a single organisation
    """
    try:
        org_id = ObjectId(org_id)
        existing_org = collection["org"].find_one({"_id": org_id})

        if not existing_org:
            return HTTPException(status_code=404, detail=f"Organisation not found")
        
        update_org.updated_at = datetime.timestamp(datetime.now())
        result = collection["org"].delete_one({"_id": org_id})
        return {"status_code": 200, "message":"Organisation Deleted Successfully"}

    except Exception as e:
        return HTTPException(status_code=500, detail=f"An error occured {e}")
    
#app routes
@router.get("/apps/")
async def get_apps():
    """
    Get all apps
    """
    data = collection["app"].find()
    return all_apps_data(data)

@router.post("/app/")
async def create_app(app: App):
    """
    Create a new app
    """
    try:
        result = collection["app"].insert_one(dict(app))
        return {"status_code": 201, "id":str(result.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"An error occurred: {e}")
    
@router.put("/app/{app_id}")
async def update_app(app_id: str, updated_app: App):
    """
    Update an app
    """
    try:
        app_id = ObjectId(app_id)
        existing_app = collection["app"].find_one({"_id": app_id})

        if not existing_app:
            return HTTPException(status_code=404, detail=f"App not found")
        
        update_app.updated_at = datetime.timestamp(datetime.now())
        result = collection["app"].update_one({"_id": app_id}, {"$set":dict(updated_app)})
        return {"status_code": 200, "message":"App Updated Successfully"}

    except Exception as e:
        return HTTPException(status_code=500, detail=f"An error occured {e}")

@router.delete("/app/{app_id}")
async def delete_app(app_id: str):
    """
    Delete a single app
    """
    try:
        app_id = ObjectId(app_id)
        existing_app = collection["app"].find_one({"_id": app_id})

        if not existing_app:
            return HTTPException(status_code=404, detail=f"App not found")
        
        update_app.updated_at = datetime.timestamp(datetime.now())
        result = collection["app"].delete_one({"_id": app_id})
        return {"status_code": 200, "message":"App Deleted Successfully"}

    except Exception as e:
        return HTTPException(status_code=500, detail=f"An error occured {e}")

#messages routes
@router.get("/messages/")
async def get_messages():
    """
    Get all messages
    """
    data = collection["message"].find()
    return all_messages_data(data)

@router.post("/message/")
async def create_message(message: Message):
    """
    Create a new message
    """
    try:
        result = collection["message"].insert_one(dict(message))
        return {"status_code": 201, "id":str(result.inserted_id)}
    except Exception as e:
        return HTTPException(status_code=500, detail=f"An error occurred: {e}")

@router.put("/message/{message_id}")
async def update_message(message_id: str, updated_message: Message):
    """
    Update a message
    """
    try:
        message_id = ObjectId(message_id)
        existing_message = collection["message"].find_one({"_id": message_id})

        if not existing_message:
            return HTTPException(status_code=404, detail=f"Message not found")
        
        update_message.updated_at = datetime.timestamp(datetime.now())
        result = collection["message"].update_one({"_id": message_id}, {"$set":dict(updated_message)})
        return {"status_code": 200, "message":"Message Updated Successfully"}

    except Exception as e:
        return HTTPException(status_code=500, detail=f"An error occured {e}")

@router.delete("/message/{message_id}")
async def delete_message(message_id: str):
    """
    Delete a single message
    """
    try:
        message_id = ObjectId(message_id)
        existing_message = collection["message"].find_one({"_id": message_id})

        if not existing_message:
            return HTTPException(status_code=404, detail=f"Message not found")
        
        update_message.updated_at = datetime.timestamp(datetime.now())
        result = collection["message"].delete_one({"_id": message_id})
        return {"status_code": 200, "message":"Message Deleted Successfully"}

    except Exception as e:
        return HTTPException(status_code=500, detail=f"An error occured {e}")
    
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


app.include_router(router)
