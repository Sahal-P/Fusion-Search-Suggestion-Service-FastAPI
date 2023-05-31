from fastapi import FastAPI
from routes.suggestion import suggestion
from config.suggestion_db_utils import connect_to_mongo, close_mongo_connection
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(suggestion)

app.add_event_handler("startup",connect_to_mongo)
app.add_event_handler("shutdown",close_mongo_connection)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)