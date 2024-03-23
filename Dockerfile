# Use an official Python runtime as a parent image
FROM python:3.10.11

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 to allow communication to/from server
EXPOSE 5000

# Define environment variable
ENV FLASK_APP run.py
ENV DATABASE_URL sqlite:///light_db.db

# Migration
RUN flask db init
RUN flask db migrate
RUN flask db upgrade

# Run app.py when the container launches
RUN flask run --host=0.0.0.0
