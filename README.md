# System Health Monitoring

This script monitors the health of your system by checking CPU usage, memory usage, disk space, and the number of running processes. It logs any issues that exceed predefined thresholds and provides alerts both in the console and in a log file.

## Requirements

- Python 3.x
- `psutil` library (`pip install psutil`)

## Configuration

You can configure the thresholds for system health checks by modifying the following variables in the script:
- `CPU_THRESHOLD`: CPU usage percentage threshold to trigger an alert (default: 80%).
- `MEMORY_THRESHOLD`: Memory usage percentage threshold to trigger an alert (default: 80%).
- `DISK_THRESHOLD`: Disk usage percentage threshold to trigger an alert (default: 80%).
- `PROCESS_THRESHOLD`: Number of processes threshold to trigger an alert (default: 150).

## Setup and Usage

1. **Install Dependencies**:
   Install the `psutil` library using pip:
   ```bash
   pip install psutil

2. **Run The Script**
   python monitor.py 