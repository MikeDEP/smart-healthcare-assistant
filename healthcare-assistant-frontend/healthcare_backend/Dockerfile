# Use a Python base image (adjust the version as needed)
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt into the container
COPY requirements.txt .

# Install system dependencies for building Django and its dependencies
RUN apt-get update && apt-get install -y libpq-dev

# Install Python dependencies from the requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project files into the container
COPY . .

# Set environment variables if needed (for example, to enable Django's development mode)
ENV DJANGO_SETTINGS_MODULE=healthcare_backend.settings

# Expose the port the Django app will run on (default is 8000)
EXPOSE 8000

# Set the command to start Django (using Gunicorn as the WSGI server)
CMD ["gunicorn", "healthcare_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
