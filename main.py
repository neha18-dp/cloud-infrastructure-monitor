from monitoring.collector import collect_metrics
from monitoring.service_checker import get_service_status
from models.metrics import SystemMetrics
from datetime import datetime
from monitoring.logger import setup_logger
from monitoring.threshold import check_thresholds
from config.config import SERVERS
from aws.dynamodb import save_metrics
from aws.sns import send_alert


logger = setup_logger()

metrics = collect_metrics()
service_status = get_service_status("python.exe")

# Add service status to metrics for SNS email
metrics["service_status"] = service_status

timestamp = datetime.now()

all_alerts = []

for server in SERVERS:

    system_metric = SystemMetrics(
        server_id=server,
        timestamp=timestamp.isoformat(),
        cpu_usage=metrics["cpu_usage"],
        memory_usage=metrics["memory_usage"],
        disk_usage=metrics["disk_usage"],
        uptime=metrics["uptime"],
        service_status=service_status
    )

    save_metrics(system_metric)

    logger.info("Monitoring snapshot collected")
    logger.info(f"CPU Usage: {system_metric.cpu_usage}%")
    logger.info(f"Memory Usage: {system_metric.memory_usage}%")
    logger.info(f"Disk Usage: {system_metric.disk_usage}%")

    logger.info(
        f"Service {service_status['service']}: "
        f"{service_status['status']}"
    )

    print(system_metric)

    alerts = check_thresholds(metrics)

    for alert in alerts:
        logger.warning(alert)
        print(alert)

        # Collect alert instead of sending immediately
        all_alerts.append((server, alert))


# Send ONE SNS email for the entire monitoring run
if all_alerts:
    send_alert(
        all_alerts,
        metrics,
        timestamp.isoformat()
    )