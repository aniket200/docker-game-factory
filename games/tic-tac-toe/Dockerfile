# ============================================================
# Docker Game Factory - Tic-Tac-Toe
# Multi-stage production Dockerfile
# ============================================================


# ============================================================
# STAGE 1 - BUILDER
# ============================================================

FROM python:3.12-slim AS builder

WORKDIR /build


# Copy dependency file

COPY requirements.txt .


# Create isolated Python environment

RUN python -m venv /opt/venv


# Install dependencies

RUN /opt/venv/bin/pip install \
    --no-cache-dir \
    --upgrade pip \
    && \
    /opt/venv/bin/pip install \
    --no-cache-dir \
    -r requirements.txt


# ============================================================
# STAGE 2 - PRODUCTION
# ============================================================

FROM python:3.12-slim


# Application directory

WORKDIR /app


# Create dedicated non-root user

RUN useradd \
    --create-home \
    --shell /bin/bash \
    gameuser


# Copy Python virtual environment
# from builder stage

COPY --from=builder \
    /opt/venv \
    /opt/venv


# Copy application

COPY app.py .

COPY templates ./templates


# Configure Python path

ENV PATH="/opt/venv/bin:$PATH"

ENV PYTHONUNBUFFERED=1

ENV PYTHONDONTWRITEBYTECODE=1


# Run application as non-root user

USER gameuser


# Application port

EXPOSE 5000


# ============================================================
# DOCKER HEALTH CHECK
# ============================================================

HEALTHCHECK \
    --interval=30s \
    --timeout=5s \
    --start-period=10s \
    --retries=3 \
    CMD python -c \
    "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" \
    || exit 1


# ============================================================
# PRODUCTION SERVER
# ============================================================

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--threads", "2", "--timeout", "30", "app:app"]
