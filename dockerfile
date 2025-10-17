FROM astral/uv:python3.12-bookworm-slim

# Install system packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        git \
        curl && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /fullstack

# Copy project files
COPY . .

# Configure uv to use a .venv in the workdir and add it to PATH
ENV UV_PROJECT_ENVIRONMENT=.venv \
    PATH="/fullstack/.venv/bin:${PATH}"

# Install Python dependencies from pyproject.toml
RUN uv sync --no-dev

# Expose application port
EXPOSE 8000

CMD ["/bin/bash"]
