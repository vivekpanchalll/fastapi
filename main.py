from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

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

@app.get("/api/posts")
def get_posts():
    return posts 