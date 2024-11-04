from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/quizzes/{quizz_id}")
async def get_quizz(quizz_id: int, q: str):
    return {"quizz_id": quizz_id, "q": q}
