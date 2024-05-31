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
from jobs.messaging_job import send_message_job
from rq import Queue
from redis import Redis
from rq.job import Job
from routers import message
from routers import user
from routers import organisation
from routers import group
from routers import app
"""
Main module
"""


app = FastAPI()
router = APIRouter()
redis_conn = Redis()


app.include_router(message.router)
app.include_router(user.router)
app.include_router(organisation.router)
app.include_router(group.router)
app.include_router(app.router)

app.include_router(router)
