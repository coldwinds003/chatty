FROM python:3.11-slim

WORKDIR /app

# Install system dependencies that might be needed by PyMuPDF and others
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port 8000
EXPOSE 8000

# Start the uvicorn server
CMD ["python", "main.py"]
