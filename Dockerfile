FROM python:3.8-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install --upgrade pip && \
    pip install poetry==1.6.1

# Copy only requirements to cache them in docker layer
COPY poetry.lock pyproject.toml /app/

# Install dependencies
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root

# Copy the rest of the application
COPY . /app

# Install the package in development mode
RUN poetry install --no-interaction --no-ansi

# Expose the default Modbus TCP port
EXPOSE 5020

# Health check script
RUN echo '#!/bin/sh\n\
# Check if modbus server is running\nif ! pgrep -f "modbusim tcp" > /dev/null; then\n  exit 1\nfi\n\n# Check if we can connect to the Modbus server\nif ! nc -z localhost 5020; then\n  exit 1\nfi\n\n# Check if we can read from the device (if using RTU)\nif [ "$MODBUS_MODE" = "rtu" ] && [ -e "$MODBUS_PORT" ]; then\n  if ! stty -F "$MODBUS_PORT" -a > /dev/null 2>&1; then\n    exit 1\n  fi\nfi\n\nexit 0\n' > /healthcheck.sh && \
    chmod +x /healthcheck.sh

# Set the health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD /healthcheck.sh

# Set the default command to run the Modbus TCP simulator
CMD ["poetry", "run", "modbusim", "tcp", "--host", "0.0.0.0", "--port", "5020"]
