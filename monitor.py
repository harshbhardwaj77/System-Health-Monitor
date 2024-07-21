import psutil
import logging
from datetime import datetime

# Define thresholds
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage
PROCESS_THRESHOLD = 150  # number of processes

# Set up logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_and_alert(message):
    print(message)
    logging.info(message)

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_and_alert(f"High CPU usage detected: {cpu_usage}%")

def check_memory():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        log_and_alert(f"High memory usage detected: {memory_usage}%")

def check_disk():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        log_and_alert(f"Low disk space detected: {disk_usage}% used")

def check_processes():
    process_count = len(psutil.pids())
    if process_count > PROCESS_THRESHOLD:
        log_and_alert(f"High number of processes detected: {process_count} processes")

def monitor_system():
    log_and_alert("Starting system health check")
    check_cpu()
    check_memory()
    check_disk()
    check_processes()
    log_and_alert("System health check completed")

if __name__ == "__main__":
    monitor_system()
