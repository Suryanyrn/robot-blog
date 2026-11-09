FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app/

# Set working directory to the subfolder containing manage.py
WORKDIR /app/blogs

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --noinput

# Run gunicorn
CMD ["gunicorn", "blogs.wsgi:application", "--bind", "0.0.0.0:8000"]
