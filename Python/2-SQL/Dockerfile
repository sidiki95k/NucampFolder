# Use an official Python runtime as the base image
FROM python:3.12.1-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Install virtualenv
RUN python -m venv venv

# Copy the Flask application code and requirements.txt to the container
COPY week3 /app
COPY week3/requirements.txt /app/requirements.txt

# Activate the virtual environment and install the python packages into it
RUN . /app/venv/bin/activate && pip install -r requirements.txt

# Set the environment variables
ENV FLASK_APP=/app/flask/twitter/wsgi.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

# Expose the port on which the Flask app will run
EXPOSE 5000

# Keep the container running indefinitely for debugging or manual interaction
CMD ["tail", "-f", "/dev/null"]
