from fastapi import APIRouter, Depends, Body, Request
from models import suggestion
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from bson import ObjectId
from schemas.user import SuggestionEntity
from starlette.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_204_NO_CONTENT
from typing import Optional
from fastapi import Query
import datetime
from services.service import SearchSuggestion
# from config.db import collection

suggestion = APIRouter()
data = SearchSuggestion()

@suggestion.get("/")
async def UserLoginAPIView() -> JSONResponse:
    
    for i in range(1000):
        data.insert(f'sahal{i}')
    for i in range(1000):
        data.insert(f'nikhil{i}')
    for i in range(1000):
        data.insert(f'fayas{i}')
    for i in range(1000):
        data.insert(f'nibu{i}')
    for i in range(1000):
        data.insert(f'jaswanth{i}')
    for i in range(50):
        data.insert(f'saj{i}')
    for i in range(50):
        data.insert(f'sae{i}')
    for i in range(50):
        data.insert(f'saoo{i}')
    return JSONResponse(status_code=HTTP_200_OK, content="Lets Start The Suggestion Service!")

@suggestion.get("/search")  
async def UserLoginAPIView(prefix: str = Query(...)) -> JSONResponse:
    try:
        results = data.search(prefix)
    except KeyError:
        return JSONResponse(status_code=HTTP_204_NO_CONTENT, content=[])
    return JSONResponse(status_code=HTTP_200_OK, content=results)
