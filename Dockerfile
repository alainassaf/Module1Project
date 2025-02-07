# Use the latest Python image from the Docker Hub
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the Pillow library
RUN pip install --no-cache-dir pillow

# Command to run when the container starts
CMD ["python"]