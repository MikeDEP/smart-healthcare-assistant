# Use official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory into the container's working directory
COPY . .

# Install dependencies (Flask, etc.)
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your app will run on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]

