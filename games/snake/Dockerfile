# ============================================================
# Docker Game Factory - Snake
# ============================================================

FROM python:3.12-slim AS builder

WORKDIR /build

COPY requirements.txt .

RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install \
    --no-cache-dir \
    --upgrade pip && \
    /opt/venv/bin/pip install \
    --no-cache-dir \
    -r requirements.txt


# ============================================================
# Production image
# ============================================================

FROM python:3.12-slim

WORKDIR /app


# Create non-root user

RUN useradd \
    --create-home \
    --shell /bin/bash \
    gameuser


# Copy virtual environment

COPY --from=builder \
    /opt/venv \
    /opt/venv


# Copy application

COPY app.py .

COPY templates ./templates


# Environment

ENV PATH="/opt/venv/bin:$PATH"

ENV PYTHONUNBUFFERED=1

ENV PYTHONDONTWRITEBYTECODE=1


# Non-root execution

USER gameuser


EXPOSE 5000


# Health check

HEALTHCHECK \
    --interval=30s \
    --timeout=5s \
    --start-period=10s \
    --retries=3 \
    CMD python -c \
    "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')" \
    || exit 1


# Production server

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--threads", "2", "--timeout", "30", "app:app"]
