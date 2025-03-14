# Python Hands-On Tasks

## 1. System Monitoring Script  
📌 **Task:** Use an appropiate Python library to display CPU and memory usage.  
✅ **Instructions:**  
- Install `python lib` using `pip`.  
- Write a script that prints CPU and memory usage every few seconds.  
- Example output:  
CPU Usage: 35% 
Memory Usage: 60%

- **Bonus:** Extend the script to log this data into a file for future analysis.

## Solution

```python
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
```
## Screenshot (Bonus Inclusive):
![Image](https://github.com/user-attachments/assets/a2d0c531-aff7-4231-b8f3-a41320cb092b)


- **Bonus (Log file data):**
![Image](https://github.com/user-attachments/assets/9ed1ec5f-bdf5-4a25-b9fd-056366aedc3b)
---

## 2. API Interaction (Weather Data Fetching)  
📌 **Task:** Write a Python script that fetches weather data from an API and processes the response.  
✅ **Instructions:**  
- Sign up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) and get a free API key.  
- Fetch weather details (temperature, weather condition, humidity) for a given city.  
- Example output:  
Weather in Lagos: 
Temperature: 30°C 
Condition: Clear sky 
Humidity: 75%


- **Bonus:** Modify the script to allow users to enter multiple city names.

## Solution

```python
#!/usr/bin/env python3

import requests

def get_weather(city, api_key):
    # OpenWeatherMap API endpoint
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse the JSON data
        data = response.json()
        # Extract relevant information
        city_name = data['name']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        return city_name, temperature, weather_description, humidity
    else:
        print("Error: Unable to fetch data.")
        return None

def main():
    api_key = "Replace with your API key"  # Replace with your API key

    # Allow user to enter multiple city names, separated by commas
    cities = input("Enter city names (comma-separated): ").split(",")

    # Strip spaces from each city name
    cities = [city.strip() for city in cities]

    for city in cities:
        weather = get_weather(city, api_key)
        if weather:
            city_name, temperature, weather_description, humidity = weather
            print("---------------------------")
            print(f"Weather in {city_name}: ")
            print(f"Temperature: {temperature}°C")
            print(f"Description: {weather_description}")
            print(f"Humidity: {humidity}%")
            print("--------------------------")


if __name__ == "__main__":
    main()
```
## Screenshot (Bonus Inclusive):

![Image](https://github.com/user-attachments/assets/4425f149-85b9-4561-9335-d7c591d765af)


---

## 3. Log File Error Scanner  
📌 **Task:** Write a script that scans a `.log` file and counts occurrences of the word `"ERROR"`.  
✅ **Instructions:**  
- Create a sample `.log` file with different log messages, including `"ERROR"`.  
- Write a Python script that reads the file and counts occurrences of `"ERROR"`.  
- Example output:  
Found 5 occurrences of 'ERROR' in logs.

- **Bonus:** Extend the script to filter logs by date or severity level (INFO, WARNING, ERROR).

## Solution

```python
def scan_log(file_path, severity="ERROR"):
    count = 0
    filtered_logs = []

    with open(file_path, "r") as log_file:
        for line in log_file:
            if severity in line:
                count += 1
                filtered_logs.append(line.strip())

    print(f"Found {count} occurrences of '{severity}' in logs.")

    if filtered_logs:
        print("\nFiltered logs:")
        for log in filtered_logs:
            print(log)

# Run the function
log_file_path = "sample.log"
scan_log(log_file_path, "ERROR")
```

## Screenshot (Bonus Inclusive):

![Image](https://github.com/user-attachments/assets/28073091-9549-4748-bd1d-d499acda6858)


---
