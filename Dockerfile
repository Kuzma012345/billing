FROM python:3.10-slim AS base-image

# --- BEGIN BASE IMAGE ---
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    VENV_PATH=/opt/venv
ENV PATH="$VENV_PATH/bin:$PATH"

# Install packages
RUN apt-get update && \
    \
    apt-get install -y \
        gcc \
        curl \
        bash \
        libpq-dev \
    && \
    \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /usr/share/man/

# Setup venv
RUN python -m venv $VENV_PATH
# --- END BASE IMAGE ---

# --- BEGIN POETRY ---
ENV POETRY_HOME=/opt/poetry \
    POETRY_VERSION=1.1.13
ENV PATH="$POETRY_HOME/bin:$PATH"

# Install poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python - && \
    poetry --version && \
    \
    poetry config virtualenvs.create false
# --- END POETRY ---



FROM base-image AS dependency-image

WORKDIR /build

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-interaction --no-dev --no-root -vvv




FROM base-image AS runtime-image

WORKDIR /app

COPY --from=dependency-image $VENV_PATH $VENV_PATH
COPY ./ ./

COPY  docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /app/docker-entrypoint.sh
CMD [ "sh", "/app/docker-entrypoint.sh" ]
