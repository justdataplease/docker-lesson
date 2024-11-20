# Use a lightweight Python image
FROM python:3.9-slim

RUN apt update && apt install -y cron

# Set the working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script
COPY writer.py .

# Copy cron job configuration
COPY cronjob /etc/cron.d/cronjob

# Set permissions for the cron file
RUN chmod 0644 /etc/cron.d/cronjob

# Apply cron job
RUN crontab /etc/cron.d/cronjob

# Ensure the log file exists and has the correct permissions
RUN touch /logs/cron.log && chmod 0664 /logs/cron.log

# Ensure cron runs in the foreground
CMD ["cron", "-f"]
