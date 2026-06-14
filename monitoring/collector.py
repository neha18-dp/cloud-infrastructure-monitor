import psutil

def get_cpu_usage() -> float:

    """
    Retrieve the current CPU utilization percentage.

    Returns:
        Float: CPU usage percentage.

    """
    return round(psutil.cpu_percent(interval=1), 2)

def get_memory_usage() -> float:
    """
    Retrieve the current memory utilization percentage.

    Returns:
        Float: Memory usage percentage.

    """
    return round(psutil.virtual_memory().percent, 2)

def get_disk_usage() -> float:

    """
    Retrieve the current disk utilization percentage.

    Returns:
        Float: Disk usage percentage.

    """
    return round(psutil.disk_usage("C:\\").percent, 2)

import time

def get_uptime() -> str:
    """
    Retrieve the system uptime.

    Returns:
        str: System uptime in days, hours and minutes.

    """
    uptime_seconds = int(time.time() - psutil.boot_time())

    days = int(uptime_seconds // 86400)

    hours = int((uptime_seconds % 86400) // 3600)

    minutes = int((uptime_seconds % 3600) // 60)

    return f"{days} days, {hours} hours, {minutes} minutes"

def collect_metrics() -> dict:
    return{
        "cpu_usage": get_cpu_usage(),
        "memory_usage": get_memory_usage(),
        "disk_usage": get_disk_usage(),
        "uptime": get_uptime()
    }




if __name__ == "__main__":


    print(collect_metrics())