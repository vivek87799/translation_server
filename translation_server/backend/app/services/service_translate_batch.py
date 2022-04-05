from fastapi import status, HTTPException
from concurrent.futures import ProcessPoolExecutor
import asyncio
from elasticsearch import AsyncElasticsearch
from typing import List

from app.models import model_user
from app.db.schemas import Token
from app.api.dependencies import create_access_token

from app.db import schemas

from app.db.database import ElasticsearchClient

async def task(src: str, es):
    query_body =  {
            "match": {
                "src": src
            }
        }
    
    val = await ElasticsearchClient.es.search(
        index = "tmx_data", # Parameters.ES_INDEX,
        query= query_body
    )
    
    # val = await es.search(index="tmx_data", query={"match": {"src": "mail"}})
    val = val ['hits']['hits']
    results = []
    try:
        for k in val:
            results.append(k['_source'])
    except Exception as error:
        return str(error)
    
    
    return results # str(len(val['hits']['hits']))

async def run_manager(str_query: List[str]):
    results = []
    try:
        """
        with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
            futures = {executor.submit(worker_process, i): i for i in range(10)}
            futures = {executor.submit(task, src_sent, AsyncElasticsearch('http://gs-search:9200/')): src_sent for src_sent in str_query}
            for future in concurent.futures.as_completed(futures):
                i = futures[future]
                results.append(future.result())
                # print(f'{future.result()}')
                # process the result
            results  = "works"
        """
        for src_sent in str_query:
            results.append(asyncio.create_task(task(src_sent, ElasticsearchClient.es)))
    
    except Exception as error:
        return str(error)
    return await asyncio.gather(*results)

async def translate_batch(data: schemas.TranslationDataRequest)-> schemas.TranslationDataResponse:
    try:
        """
        
        """
        str_query = [d.src_sent for d in data.__root__]
        # val = await ElasticsearchClient.es.search(index="tmx_data", query={"match": {"src": "mail"}})
        return await run_manager(str_query)
        
    except Exception as error:
        return error