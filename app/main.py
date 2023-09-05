from datetime import date

import uvicorn
from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/hotels')
def get_hotels(
        location: str,
        date_from: date,
        date_to: date,
        stars: int = Query(None, ge=1, le=5),
        has_spa: bool = None
):
    return location, date_to, date_from, stars, has_spa


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
