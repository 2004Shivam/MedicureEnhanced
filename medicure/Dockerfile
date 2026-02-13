# Use official Python runtime
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Copy project
COPY . /app/

# Collect static files for WhiteNoise
RUN pip install setuptools==69.5.1
RUN python manage.py collectstatic --noinput

# Expose port (not strictly necessary but good practice)
EXPOSE 8000

# Default command (Production ready)
CMD ["sh", "-c", "python manage.py migrate && python manage.py populate_doctors && gunicorn medicure.wsgi:application --bind 0.0.0.0:8000"]
