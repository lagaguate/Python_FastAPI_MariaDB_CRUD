from fastapi import APIRouter, Response
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from schema.user_schema import UserSchema, UserLogin
from config.db import engine
from model.user import users
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List

user = APIRouter()


@user.get("/")
def root():
    return {"message": "Router with FastAPI"}


@user.get("/api/user", response_model=List[UserSchema])
def get_users():
    with engine.connect() as conn:
        result = conn.execute(users.select()).fetchall()

        return result


@user.get("/api/user/{user_id}", response_model=UserSchema)
def get_user(user_id: str):
    with engine.connect() as conn:
        result = conn.execute(users.select().where(
            users.c.id == user_id)).first()

        return result


@user.post("/api/user", status_code=HTTP_201_CREATED)
def create_user(data_user: UserSchema):
    with engine.connect() as conn:
        new_user = data_user.dict()
        new_user["user_passw"] = generate_password_hash(
            data_user.user_passw, "pbkdf2:sha256:30", 30)
        # print(data_user)
        print(new_user)
        conn.execute(users.insert().values(new_user))
        return Response(status_code=HTTP_201_CREATED)


@user.put("/api/user/{user_id}", response_model=UserSchema)
def update_user(data_user: UserSchema, user_id: str):
    with engine.connect() as conn:
        encryp_passw = generate_password_hash(
            data_user.user_passw, "pbkdf2:sha256:30", 30)
        conn.execute(users.update().values(name=data_user.name,
                     username=data_user.username, user_passw=encryp_passw).where(users.c.id == user_id))
        result =conn.execute(users.select().where(users.c.id == user_id)).first()

        return result
    
@user.delete("/api/user/{user_id}",status_code=HTTP_204_NO_CONTENT)
def delete_user(user_id:str):
    with engine.connect() as conn:
        conn.execute(users.delete().where(users.c.id==user_id))    

        return Response(status_code=HTTP_204_NO_CONTENT)    

 #
 #  Valida que sea el password correcto que se ingreso
 #     
@user.post("/api/user/login")
def user_login(data_login: UserLogin):
    with engine.connect() as conn:
        result = conn.execute(users.select().where(users.c.username == data_login.username)).first()    

        if result != None:
            check_passw = check_password_hash(result[3],data_login.user_passw)
            print (check_passw)

            if check_passw:
                return {
                    "status":200,
                    "message":"Access success"
                }     
               
        return {
                    "status":401,
                    "message":"Access denied"
                }     