from pydantic import BaseModel, validator

from pydantic.utils import GetterDict

from typing import Any

from peewee import ModelSelect

class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        
        res = getattr(self._obj, key, default)

        if isinstance(res, ModelSelect):
            return list(res)

        return res    

class UserRequestModel(BaseModel):
    username : str
    password : str

    @validator('username')
    def username_validator(cls, username):
        if len(username) < 3 or len(username) > 50:
            raise ValueError('El nombre de usuario debe tener mas de 3 y menos de 50 caracteres.')

        return username    

class UserResponseModel(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict



    


