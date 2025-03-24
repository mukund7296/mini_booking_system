# Use official Python image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the entire project
COPY . .

# Run the entrypoint script
ENTRYPOINT ["/app/docker/entrypoint.sh"]
