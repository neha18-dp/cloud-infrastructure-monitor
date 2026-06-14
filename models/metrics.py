from dataclasses import dataclass

@dataclass
class SystemMetrics:
    server_id: str
    timestamp: str
    cpu_usage: float
    memory_usage: float
    disk_usage: float
    uptime: str
    service_status: dict

