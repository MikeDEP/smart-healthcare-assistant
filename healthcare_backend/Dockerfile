# Use official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
# Set the working directory
WORKDIR /app

# Copy requirements.txt into the container
COPY requirements.txt /app/

# Install the dependencies
RUN ls -al /app/
RUN pip install --no-cache-dir -r /app/requirements.txt --verbose


# Expose the port your app will run on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]



