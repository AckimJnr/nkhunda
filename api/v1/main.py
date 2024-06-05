from fastapi import FastAPI, APIRouter, Depends, HTTPException
from routers import message
from routers import user
from routers import organisation
from routers import group
from routers import organisation_app
"""
Main module
"""
app = FastAPI()
router = APIRouter()

app.include_router(message.router)
app.include_router(user.router)
app.include_router(organisation.router)
app.include_router(group.router)
app.include_router(organisation_app.router)

#root route
@app.get("/", tags=['Root'])
def read_root():
    return {"Success": "Server is running"}

app.include_router(router)
