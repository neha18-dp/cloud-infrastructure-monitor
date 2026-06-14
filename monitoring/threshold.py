CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 85


def check_thresholds(metrics: dict) -> list:
    """
    Check collected metrics against thresholds.

    Returns:
        list: List of alert messages.
    """

    alerts = []

    if metrics["cpu_usage"] > CPU_THRESHOLD:
        alerts.append(
            f"CPU usage exceeded threshold: {metrics['cpu_usage']}%"
        )

    if metrics["memory_usage"] > MEMORY_THRESHOLD:
        alerts.append(
            f"Memory usage exceeded threshold: {metrics['memory_usage']}%"
        )

    if metrics["disk_usage"] > DISK_THRESHOLD:
        alerts.append(
            f"Disk usage exceeded threshold: {metrics['disk_usage']}%"
        )

    return alerts