import boto3

sns = boto3.client("sns", region_name="ap-south-1")

TOPIC_ARN = "arn:aws:sns:ap-south-1:899505639594:CloudMonitorAlerts"


def send_alert(alerts, metrics, timestamp):
    message = f"""CLOUD INFRASTRUCTURE ALERT

Timestamp: {timestamp}

ALERTS DETECTED:
"""

    for server_id, alert in alerts:
        message += f"""
- {server_id}: {alert}
"""

    message += f"""
CURRENT SYSTEM HEALTH:

CPU Usage: {metrics["cpu_usage"]}%
Memory Usage: {metrics["memory_usage"]}%
Disk Usage: {metrics["disk_usage"]}%
Uptime: {metrics["uptime"]}

Service:
{metrics["service_status"]["service"]} - {metrics["service_status"]["status"]}

Please investigate the server condition.
"""

    sns.publish(
        TopicArn=TOPIC_ARN,
        Subject="Cloud Monitor Alert - Infrastructure",
        Message=message
    )

    print("Alert email sent.")