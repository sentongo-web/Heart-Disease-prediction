FROM python:3.10-slim

# Keep Python output unbuffered
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install runtime dependencies first
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . /app

# Add a non-root user for security
RUN useradd --create-home appuser || true
RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 80

# Use Gunicorn with Uvicorn workers for production
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "src.app.main:app", "--bind", "0.0.0.0:80", "--workers", "2", "--log-level", "info"]
