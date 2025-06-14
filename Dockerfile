# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy your current directory contents into the container
COPY . .

# Install dependencies (if you have a requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt || true

# Run nginx_monitor.py when the container starts
CMD ["python", "nginx_monitor.py"]
