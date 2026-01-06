import psutil


def get_system_metrics():
    """
      This API gets the system meterics(CPU, Memory, Disk Usage) and checks if the CPU usage is above a certain threshold.
      Returns:
          dict: A dictionary containing CPU, Memory, Disk usage percentages and status based on CPU threshold
    """
    cpu_percentage = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage("/").percent
    
    cpu_threshold = 20
    status = "High CPU Usage" if cpu_percentage > cpu_threshold else "Normal CPU Usage"
    # or
    # if cpu_percentage > cpu_threshold:
    #     cpu_status = "High CPU Usage"
    # else:
    #     cpu_status = "Normal CPU Usage"
    return {
        "cpu_usage_percent": cpu_percentage,
        "memory_usage_percent": memory_percent,
        "disk_usage_percent": disk_percent,
        "cpu_threshold": cpu_threshold,
        "status": status
    }