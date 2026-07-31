import boto3

sns = boto3.client("sns", region_name="ap-south-1")

TOPIC_ARN = "arn:aws:sns:ap-south-1:899505639594:CloudMonitorAlerts"


def send_alert(message):

    sns.publish(
        TopicArn=TOPIC_ARN,
        Subject="Cloud Monitor Alert",
        Message=message
    )


    print("Alert email sent.")