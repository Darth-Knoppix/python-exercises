# SNS + SQS Pubsub

Setup SQS to subscribe to SNS so that messages can be published and then queued.

**Execute from http://localhost:8000/docs**

## How does it work?

1. Order coffee

This publishes an event on `coffee-orders` which gets pushed onto the `order-queue` queue.

```sh
curl -X 'POST' \
  'http://localhost:8000/order-coffee' \
  -H 'accept: application/json' \
  -d ''
```

2. Then see the coffee orders and remove them from the queue.

The `order-queue` is read and up to 4 orders are accepted at a time.

```sh
curl -X 'GET' \
  'http://localhost:8000/items/' \
  -H 'accept: application/json'
```

## How?

Run localstack - `docker run --rm -p 4566:4566 -p 4571:4571 -e DEFAULT_REGION=eu-west-1 localstack/localstack` in addition to the app itself `docker-compose build` then `docker-compose up`.

**Both localstack and the app must be running for this to work**
