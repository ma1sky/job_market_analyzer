FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:0.12.3 /uv /uvx /bin/
COPY pyproject.toml uv.lock ./

COPY services/scraper/pyproject.toml services/scraper/pyproject.toml
COPY shared/pyproject.toml shared/pyproject.toml

COPY services/scraper/src services/scraper/src
COPY shared/src shared/src

RUN uv sync --frozen --package scraper --no-dev

CMD ["uv", "run", "--frozen", "--no-sync", "--package", "scraper", "python", "-m", "scraper"]
