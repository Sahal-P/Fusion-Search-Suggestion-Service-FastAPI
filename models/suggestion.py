from pydantic import BaseModel, Field
from bson import ObjectId
import pydantic, datetime
from bson import ObjectId
from typing import Optional
# pydantic.json.ENCODERS_BY_TYPE[ObjectId]=str

class PyObjectId(ObjectId):
    """ Custom Type for reading MongoDB IDs """
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid object_id")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

# 
class Suggestion(BaseModel):
    _id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")


    class Config:
        allow_population_by_field_name =True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: lambda v:str}
        


