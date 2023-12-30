from fastapi import FastAPI

from api.routers import question

app = FastAPI()
app.include_router(question.router)

@app.get("/hello",tags=["root"])
async def hello():
    return {"message": "Hello World"}