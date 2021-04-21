import boto3
from .bootstrap import aws_client_kwargs


class Publisher:
    topic_arn = None

    def __init__(self, topic_arn):
        self.client = boto3.client('sns', **aws_client_kwargs)
        self.topic_arn = topic_arn

    def publish(self):
        if self.topic_arn is None:
            print('No topic to publish events to')
            return

        self.client.publish(
            TopicArn=self.topic_arn,
            Message='1x latte',
            Subject='coffee',
        )
