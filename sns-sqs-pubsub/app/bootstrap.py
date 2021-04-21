import os
import boto3


TOPIC_NAME = 'coffee-orders'
QUEUE_NAME = 'order-queue'


aws_client_kwargs = {
    'region_name': os.getenv("AWS_REGION_NAME", None),
    'endpoint_url': os.getenv("AWS_ENDPOINT", None),
    'aws_access_key_id': os.getenv("AWS_ACCESS_KEY_ID", None),
    'aws_secret_access_key': os.getenv("AWS_SECRET_ACCESS_KEY", None),
}


def create_topic():
    client = boto3.client('sns', **aws_client_kwargs)
    response = client.create_topic(Name=TOPIC_NAME)
    return response['TopicArn']


def create_queue():
    sqs = boto3.resource('sqs', **aws_client_kwargs)
    sqs.create_queue(QueueName=QUEUE_NAME, Attributes={'DelaySeconds': '5'})
