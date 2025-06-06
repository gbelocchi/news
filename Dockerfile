# Base image
FROM python:3.11-slim

# Working directory
WORKDIR /app

# Copy files
COPY main.py .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port for Flask
EXPOSE 8080

# Run the app
CMD ["python", "main.py"]
