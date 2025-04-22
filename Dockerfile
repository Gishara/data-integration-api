# Use official FastAPI image (includes Uvicorn and Python)
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire app
COPY . .

# Optional: expose port (default is 80 in base image)
EXPOSE 80
