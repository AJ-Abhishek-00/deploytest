# Use lightweight Python image
FROM python:3.11-slim

# Create non-root user for security
RUN adduser --disabled-password --gecos "" appuser

# Set working directory
WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create necessary folders
RUN mkdir -p data logs

# Give ownership to non-root user
RUN chown -R appuser /app

# Switch to non-root user
USER appuser

EXPOSE 10000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "10000"]
