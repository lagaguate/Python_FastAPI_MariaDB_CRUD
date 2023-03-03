from typing import Optional
from pydantic import BaseModel


class UserSchema(BaseModel):
    id: Optional[str]
    name: str
    username: str
    user_passw: str

class UserLogin(BaseModel):
    username: str
    user_passw: str  

    