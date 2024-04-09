import psutil
import time

# Define thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

# Loop continuously
while True:
    # Get system usage stats
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent

    # Check if any of the thresholds are exceeded
    if cpu_percent > CPU_THRESHOLD or memory_percent > MEMORY_THRESHOLD or disk_percent > DISK_THRESHOLD:
        print(f"Alert: CPU usage={cpu_percent}%, Memory usage={memory_percent}%, Disk usage={disk_percent}%")

    # Sleep for 5 seconds before checking again
    time.sleep(5)
    
    with open('alert.log', 'a') as f:
    f.write(f"Alert: CPU usage={cpu_percent}%, Memory usage={memory_percent}%, Disk usage={disk_percent}%\n")