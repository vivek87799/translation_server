from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer

from app.api.routes import router as api_router
from app.db.database import ElasticsearchClient

title = "Lengo Translation Server"
description = "Lengo batch translation server" 
version = 2.1

def get_application() -> FastAPI():
    app = FastAPI(title=title, description=description, version=version)
    app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
    )
    app.include_router(api_router, prefix="/api")
    return app

app = get_application()

@app.on_event("shutdown")
async def app_shutdown():
    await es.close()
"""
app = FastAPI()

@app.get("/")
async def index():
    return await ElasticsearchClient.es.cluster.health()
"""