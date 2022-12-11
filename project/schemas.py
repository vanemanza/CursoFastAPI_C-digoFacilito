from pydantic import BaseModel, validator

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

    


