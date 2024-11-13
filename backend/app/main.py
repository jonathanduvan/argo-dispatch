from fastapi import FastAPI

from app.routers import articles

app = FastAPI()


app.include_router(router=articles.router, prefix="/api/v1", tags=["Articles"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to Argo Dispatch"}


