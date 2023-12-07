import requests
import os
import json
import time
from random import randint
import argparse
from datetime import datetime

def simulate_iot_device(api_url, interval, speed_range=(10, 15), date_format='%Y-%m-%d %H:%M:%S', location=None):
    while True:
        # Simulate IoT device data
        speed = randint(*speed_range)
        current_time = datetime.now().strftime(date_format)

        data = {'speed': speed, 'timestamp': current_time, 'location': location}

        # Convert data to JSON
        payload = json.dumps(data)

        # Set headers
        headers = {'Content-Type': 'application/json'}

        try:
            # Send POST request to API Gateway
            response = requests.post(api_url, data=payload, headers=headers)

            # Print the response from the server
            print(f"Status Code: {response.status_code}, Response: {response.text}")

            # Wait for the specified interval before sending the next request
            time.sleep(interval/1000)

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Retrieve values from environment variables or use default values
    api_url = os.getenv('API_URL')
    interval = int(os.getenv('INTERVAL', 100))
    speed_range = tuple(map(int, os.getenv('SPEED_RANGE', '10 15').split()))
    date_format = os.getenv('DATE_FORMAT', '%Y-%m-%d %H:%M:%S')
    location = os.getenv('LOCATION')

    simulate_iot_device(api_url, interval, speed_range, date_format, location)