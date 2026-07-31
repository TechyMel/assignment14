FROM python:3.10-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies, including the runtime libs Playwright's
# Chromium needs for the E2E test suite
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        gcc python3-dev libssl-dev curl \
        libglib2.0-0 libnss3 libnspr4 libdbus-1-3 libatk1.0-0 \
        libatk-bridge2.0-0 libcups2 libx11-6 libxcomposite1 libxdamage1 \
        libxext6 libxfixes3 libxrandr2 libgbm1 libxcb1 libxkbcommon0 \
        libpango-1.0-0 libcairo2 libasound2 libatspi2.0-0 && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip and essential Python tools
RUN python -m pip install --upgrade pip setuptools>=70.0.0 wheel

# Create non-root user with a home directory (Playwright caches its browser there)
RUN groupadd -r appgroup && \
    useradd -r -m -d /home/appuser -g appgroup appuser

# Copy dependencies and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Ensure correct ownership
RUN chown -R appuser:appgroup /app

# Switch to non-root user
USER appuser

# Download the Playwright Chromium browser used by the E2E test suite
RUN python -m playwright install chromium

# Health check for the service
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run database initialization before starting the app
CMD python -m app.database_init && \
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
