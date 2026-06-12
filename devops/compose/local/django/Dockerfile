# Base Python image
FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim AS python

# Python build stage
FROM python AS python-build-stage

ARG APP_HOME=/app
WORKDIR ${APP_HOME}

# UV environment variables
ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy UV_PYTHON_DOWNLOADS=0

# Install system packages
RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev \
    gdal-bin \
    gettext \
    proj-bin \
    wait-for-it \
    sudo git bash-completion nano ssh \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files first for caching
COPY pyproject.toml poetry.lock README.md ./

# Install Poetry and dependencies directly into system Python (no venv)
RUN pip install --upgrade pip poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root

# Copy source code last to allow live reload via bind mount
COPY . .

# Create dev-user
RUN groupadd --gid 1000 dev-user \
    && useradd --uid 1000 --gid dev-user --shell /bin/bash --create-home dev-user \
    && echo "dev-user ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/dev-user \
    && chmod 0440 /etc/sudoers.d/dev-user

# Copy entrypoint scripts
COPY ./devops/compose/production/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint && chmod +x /entrypoint

COPY ./devops/compose/local/django/start /start
RUN sed -i 's/\r$//g' /start && chmod +x /start

COPY ./devops/compose/local/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker && chmod +x /start-celeryworker

COPY ./devops/compose/local/django/celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat && chmod +x /start-celerybeat

COPY ./devops/compose/local/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower && chmod +x /start-flower

# Final workdir
WORKDIR /app

# Use the entrypoint
ENTRYPOINT ["/entrypoint"]
