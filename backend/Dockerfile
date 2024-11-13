# Base stage: common dependencies
FROM python:3.11-slim AS base

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    apt-get clean

# Install Python dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Development stage
FROM base AS development

# Install dev tools
RUN pip install --no-cache-dir black pylint
RUN apt-get update && apt-get install -y curl nano vim

# Copy application source code
COPY ./app /app/app

# Enable live reload
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# Production stage
FROM base AS production

# Copy application source code
COPY ./app /app/app

# Run the app in production mode
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
