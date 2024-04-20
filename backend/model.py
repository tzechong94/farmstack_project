from pydantic import BaseModel

# pydantic helps to auto crate JSON schemas from model
# works like object relational mapper

class Todo(BaseModel):
    title: str
    description: str