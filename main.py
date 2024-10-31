from random import randrange
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [
    {
        "title": "title of post 1",
        "content": "content of post 1",
        "id": 1
    },{
        "title": "title of post 1",
        "content": "content of post 2",
        "id": 2
    }
]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

@app.get("/")
async def root():
    return {"test-message": "Hello World"}

@app.get("/posts")
async def get_posts():
    return {"data": my_posts}


@app.post("/posts")
async def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"message": post_dict}

@app.get("/posts/{id}")
async def get_post(id):
    post = find_post(int(id))
    return {
        "message": "You selected post {id}",
        "post-detail": post
    }