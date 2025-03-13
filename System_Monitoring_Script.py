import psutil
import time
import logging

# Configure logging
logging.basicConfig(
    filename="system_usage.log",
    level=logging.INFO,
    format="%(asctime)s: \n%(message)s\n",
)

def display_and_log_usage():
    """Displays CPU and memory usage every few seconds and logs it to a file."""
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        
        # Correct log format
        log_message = f"CPU Usage: {cpu_usage}%\nMemory Usage: {memory_usage}%"

        # Print to console
        print(log_message)
        print("-" * 30)  # Separator for readability

        # Log to file
        logging.info(log_message)

        time.sleep(4)  # Wait 4 seconds before next update

if __name__ == "__main__":
    print("Monitoring CPU and Memory usage... Press Ctrl+C to stop.")
    print("-" * 30)  # Separator for readability
    
    display_and_log_usage()