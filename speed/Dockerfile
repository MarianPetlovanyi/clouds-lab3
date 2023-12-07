# Use an official Python runtime as a base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the Python script and requirements file
COPY speed_device.py .

# Install required libraries
RUN pip install requests

# Command to run your simulation
CMD ["python", "speed_device.py"]