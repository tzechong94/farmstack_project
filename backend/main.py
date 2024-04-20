from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Todo

#app object
app = FastAPI()

from database import (
    fetch_all_todos,
    fetch_one_todo,
    create_todo,
    update_todo,
    delete_todo
)

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def read_root():
    return {'Ping': "Pong"}

@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos() #return coroutine
    return response

@app.get("/api/todo/{id}", response_model=Todo)
async def get_todo_by_id(title):
    response = fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"there is no TODO item with this title {title}")

@app.post("/api/todo", response_model=Todo)
async def post_todo(todo: Todo):
    response = await create_todo(todo.model_dump())
    if response:
        return response
    raise HTTPException(400, "something went wrong / bad request")

@app.put("/api/todo/{title}", response_model=Todo)
async def put_todo_by(title:str, desc:str):
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(404, f"there is no TODO item with this title {title}")


@app.delete("/api/todo/{title}")
async def delete_todo(title):
    response = await delete_todo(title)
    if response:
        return "Successfully deleted"
    raise HTTPException(404, f"there is no TODO item with this title {title}")


