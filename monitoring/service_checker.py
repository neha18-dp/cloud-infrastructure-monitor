import psutil

def is_process_running(process_name: str) -> bool:
    for process in psutil.process_iter(['name']):
        if process.info["name"] and process.info["name"].lower() == process_name.lower():
            return True
    return False

def get_service_status(process_name: str) -> dict:
    status = "running" if is_process_running(process_name) else "stopped"
    return {
        "service": process_name,
        "status": status
    }


if __name__ == "__main__":
    


    print(is_process_running("python.exe"))
    print(get_service_status("python.exe"))