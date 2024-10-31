from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")
async def root():
    return {"test-message": "Hello World"}

@app.get("/posts")
async def get_posts():
    return {"data": "This is your post"}


@app.post("/create-posts")
async def create_posts(new_post: Post):
    print(new_post)
    return {"message": new_post.dict()}