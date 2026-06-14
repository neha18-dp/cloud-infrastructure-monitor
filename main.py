from monitoring.collector import collect_metrics
from monitoring.service_checker import get_service_status
from models.metrics import SystemMetrics
from datetime import datetime
from monitoring.logger import setup_logger
from monitoring.threshold import check_thresholds


metrics = collect_metrics()
service_status = get_service_status("python.exe")

timestamp = datetime.now()

system_metric = SystemMetrics(
    server_id="local-machine",
    timestamp=timestamp.isoformat(),
    cpu_usage=metrics["cpu_usage"],
    memory_usage=metrics["memory_usage"],
    disk_usage=metrics["disk_usage"],
    uptime=metrics["uptime"],
    service_status=service_status
)

logger = setup_logger()

logger.info("Monitoring snapshot collected")

print(system_metric)

alerts = check_thresholds(metrics)

if alerts:
    for alert in alerts:
        logger.warning(alert)
        print(alert)