from typing import Optional
from datetime import datetime
import json

import redis

from fastapi import FastAPI
from pydantic import BaseModel

from .tasks import add


class AddResult(BaseModel):
    status: str
    result: int
    task_id: str
    date_done: datetime


app = FastAPI()
store = redis.Redis(host="redis", db=0)


@app.get("/")
def read_root():
    result = add.delay(2, 8)
    return {"result": result.id}


@app.get("/results/{result_id}", response_model=Optional[AddResult])
def get_result(result_id: str):
    result = store.get("celery-task-meta-" + result_id)

    if result is None:
        return None

    return json.loads(result)
