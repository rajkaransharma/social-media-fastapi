from fastapi import FastAPI
from . import models, auth
from .database import engine
from .routers import user, post, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

# No longer needed since alembic is creating tables.
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(CORSMiddleware, allow_origins=origins,
                allow_credentials=True, allow_methods=["*"], allow_headers=["*"],)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get('/')
def home():
    return {'message': 'Please check /docs for more details.'}







