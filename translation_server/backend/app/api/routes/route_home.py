from fastapi import APIRouter
from typing import List, TypedDict
from app.db.database import ElasticsearchClient

router = APIRouter()

@router.get("/")
async def home_route() -> str:
    welcome_msg = {"message":"Welcome to Lengoo Translation Server"}
    return await ElasticsearchClient.es.cluster.health()
