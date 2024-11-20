# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Update package manager and install required utilities
RUN apt update && apt install -y \
    cron \
    iputils-ping \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script
COPY writer.py .
COPY .env /.env

# Create a directory for logs
RUN mkdir -p /logs

# Ensure the log file exists and has the correct permissions
RUN touch /logs/cron.log && chmod 0664 /logs/cron.log

# Copy cron job configuration
COPY cronjob /etc/cron.d/my-cron-job

# Set permissions for the cron file
RUN chmod 0644 /etc/cron.d/my-cron-job

# Apply cron job
RUN crontab /etc/cron.d/my-cron-job

# Ensure cron runs in the foreground
CMD ["cron", "-f"]
