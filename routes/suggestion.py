from fastapi import APIRouter, Depends, Body, Request
from models import suggestion
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from bson import ObjectId
from config.db import MongoClient, get_connection
from schemas.user import SuggestionEntity
from starlette.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from typing import Optional
import datetime

suggestion = APIRouter()

@suggestion.get("/")
async def UserLoginAPIView(conn: MongoClient = Depends(get_connection)) -> JSONResponse:
    
    return JSONResponse(status_code=HTTP_200_OK, content="Lets Start The Suggestion Service!")

