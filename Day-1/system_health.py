import psutil

def get_thresholds():
    cpu_threshold = float(input("Enter CPU usage threshold percentage: "))
    disk_threshold = float(input("Enter Disk usage threshold percentage: "))    
    memory_threshold = float(input("Enter Memory usage threshold percentage: "))
    return cpu_threshold, disk_threshold, memory_threshold

def get_system_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
    disk_usage = psutil.disk_usage('/').percent
    memory_info = psutil.virtual_memory().percent
    return cpu_usage, disk_usage, memory_info

def compare_threshold(resource_name,system_usgae_value, threshold_value):
    if system_usgae_value > threshold_value:
        print(f"Alert {resource_name} usage is high")
    else:
        print(f"{resource_name} usage is Ok..")

def main():
    cpu_th, disk_th, mem_th = get_thresholds()
    cpu_usage, disk_usage, memory_usage = get_system_metrics()
    print("\n---System Metrics---")
    print(f"Current CPU Usage: {cpu_usage}%")
    print(f"Current Disk Usage: {disk_usage}%")
    print(f"Current Memory Usage: {memory_usage}%") 
    
    print("\n--threshould check--")
    compare_threshold("CPU", cpu_usage, cpu_th)
    compare_threshold("Disk", disk_usage, disk_th)
    compare_threshold("Memory", memory_usage, mem_th)
    
if __name__ == "__main__":
    main()    
    
    



    

