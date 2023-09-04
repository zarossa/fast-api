import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def get_hotels():
    return 'One great hotel'


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
