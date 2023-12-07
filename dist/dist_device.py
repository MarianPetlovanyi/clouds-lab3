import os
import json
import requests
import time
from random import randint
from datetime import datetime

def simulate_iot_device(api_url, interval, distance_range=(10, 100), date_format='%Y-%m-%d %H:%M:%S', location=None):
    while True:
        # Simulate IoT device data
        distance = randint(*distance_range)
        current_time = datetime.now().strftime(date_format)

        data = {'distance': distance, 'timestamp': current_time, 'location': location}

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
            time.sleep(interval / 1000)

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Retrieve values from environment variables or use default values
    api_url = os.getenv('API_URL')
    interval = int(os.getenv('INTERVAL', 100))
    distance_range = tuple(map(int, os.getenv('DISTANCE_RANGE', '10 100').split()))
    date_format = os.getenv('DATE_FORMAT', '%Y-%m-%d %H:%M:%S')
    location = os.getenv('LOCATION')

    simulate_iot_device(api_url, interval, distance_range, date_format, location)