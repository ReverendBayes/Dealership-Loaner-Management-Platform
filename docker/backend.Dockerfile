# docker/backend.Dockerfile
# FastAPI backend Docker image

FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libpangocairo-1.0-0 \
    libpangoft2-1.0-0 \
    libjpeg-dev \
    libffi-dev \
    libxml2 \
    libxslt1.1 \
    libpq-dev \
    curl && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend app
COPY backend/ ./

# Expose port and run
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
