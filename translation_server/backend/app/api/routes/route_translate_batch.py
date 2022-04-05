from fastapi import APIRouter
from typing import List, TypedDict

# from app.db.schemas import NewUser
from app.db import schemas
from app.db.database import ElasticsearchClient

from app.services import service_translate_batch

schemas.TranslationDataRequest

router = APIRouter()
"""
@router.post("/translate_batch/")
async def translate_batch(req_query: schemas.TranslationDataRequest)-> schemas.TranslationDataResponse:
    
    try:
        results = ElasticsearchClient.es.search(index="tmx_data", query={"match": {"src": "mail"}})
    except AssertionError as error:
        return JSONResponse(status_code=200, content=str(error))
    return results
"""

@router.post("/translate_batch/")
async def translate_batch(req_query: schemas.TranslationDataRequest)-> schemas.TranslationDataResponse:
    
    try:
        val = await service_translate_batch.translate_batch(req_query)# await ElasticsearchClient.es.search(index="tmx_data", query={"match": {"src": "mail"}})
        results = val
    except AssertionError as error:
        return JSONResponse(status_code=200, content=str(error))
    return results