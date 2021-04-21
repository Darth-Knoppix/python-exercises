import boto3

from .bootstrap import QUEUE_NAME, aws_client_kwargs


class Orders:
    queue = None

    def __init__(self, topic_arn):
        sqs = boto3.resource("sqs", **aws_client_kwargs)
        self.queue = sqs.get_queue_by_name(QueueName=QUEUE_NAME)

        client = boto3.client("sns", **aws_client_kwargs)
        client.subscribe(
            TopicArn=topic_arn,
            Protocol="sqs",
            Endpoint=self.queue.attributes["QueueArn"],
        )

    def process(self):
        messages = []
        for message in self.queue.receive_messages(MaxNumberOfMessages=4):
            messages.append(message.body)
            message.delete()

        return messages
