from pydantic import BaseModel, Field
from pymongo import MsongoClient
from bson import ObjectId
from typing import Optional

client = MongoClient()
db = client.test


class PyObjectId(ObjectId):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')


class Villagers(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    emailid: str
    password: str
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
