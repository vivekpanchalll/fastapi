from fastapi import FastAPI, Request, HTTPException,status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from schemas import PostCreate, PostResponse
from datetime import datetime

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {
        "id": 1,
        "author": "John Doe",
        "title": "First Post",
        "content": "This is the first post",
        "created_at": "2026-01-01"
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Second Post",
        "content": "This is the second post",
        "created_at": "2026-01-02"
    },
    {
        "id": 3,
        "author": "John Doe",
        "title": "Third Post",
        "content": "This is the third post",
        "created_at": "2026-01-03"
    }
]

@app.get("/", include_in_schema=False, name="home")
@app.get("/posts", include_in_schema=False)
def home(request: Request):
    return templates.TemplateResponse(
            request,"home.html",
            {"posts":posts,
            "title":"Home"
            }
        ) 
 
@app.get("/api/posts",response_model=list[PostResponse])
def get_posts():
    return posts 

@app.post(
    "/api/posts",
    response_model=PostResponse,
    status_code=status.HTTP_201_CREATED
)
def create_post(post: PostCreate):
    
    new_post = {
        "id": len(posts) + 1,
        "title": post.title,
        "content": post.content,
        "author": post.author,
        "created_at": datetime.now().isoformat()
    }
    posts.append(new_post)
    return new_post

@app.get("/api/posts/{post_id}",response_model=PostResponse)
def get_posts(post_id: int):
    for post in posts:
        if post.get("id") == post_id:
            return post
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")