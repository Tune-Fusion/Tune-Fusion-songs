# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask app to the container
COPY api.py .
COPY schema.sql .

# Expose the port on which the Flask app will run
ENV FLASK_RUN_HOST=0.0.0.0

ENV FLASK_RUN_PORT=8080
EXPOSE 8080

# Start the Flask app
CMD ["python", "api.py"]
