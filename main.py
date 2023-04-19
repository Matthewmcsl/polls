from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

"""
username
email
created_at
updated_at
"""


class User(BaseModel):
    username: str
    email: str


"""
title
typeChoiceField (e.g, text or img)
created_by
create_at
updated_at
is_add_choices_active
is_voting_active
"""


class Poll(BaseModel):
    title: str
    type: str
    is_add_choices_active: bool
    is_voting_active: bool


@app.get("/")
def read_root():
    return {"Hello": "World"}


# setting up end points
@app.get("/polls")
def read_root():
    return {"Hello": "Homies"}


@app.get("/users")
def read_root():
    return {"Hello": "Users"}


@app.post("/users/")
async def create_user(user: User):
    return user
