from fastapi import FastAPI, status

from .publisher import Publisher
from .orders import Orders
from .bootstrap import create_queue, create_topic


app = FastAPI()

topic_arn = create_topic()
create_queue()
pub = Publisher(topic_arn)


@app.post("/order-coffee", status_code=status.HTTP_201_CREATED)
def order_coffee():
    pub.publish()
    return {"status": "done"}


@app.get("/items/")
def orders():
    return Orders(topic_arn).process()
