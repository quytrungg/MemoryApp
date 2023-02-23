# Start with a base image that has Python and Django pre-installed
FROM python:3.10.6-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory to /app
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code to the container
COPY . /app/

# Collect static files
# RUN python manage.py collectstatic --no-input

# Expose port 8000
EXPOSE 8000

# Start the server
# CMD ["python", "manage.py", "runserver", "localhost:8000"]
