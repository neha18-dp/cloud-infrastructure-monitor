from decimal import Decimal
import boto3

# Connect to DynamoDB using AWS CLI credentials
dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("ServerMetrics")


def save_metrics(system_metric):
    """
    Save monitoring metrics to DynamoDB.
    """

    table.put_item(
        Item={
            "server_id": system_metric.server_id,
            "timestamp": system_metric.timestamp,
            "cpu_usage": Decimal(str(system_metric.cpu_usage)),
            "memory_usage": Decimal(str(system_metric.memory_usage)),
            "disk_usage": Decimal(str(system_metric.disk_usage)),
            "uptime": system_metric.uptime,
            "service_status": system_metric.service_status["status"]
        }
    )


    print(f" Metrics stored for {system_metric.server_id}")