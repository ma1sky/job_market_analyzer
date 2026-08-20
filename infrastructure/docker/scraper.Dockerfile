FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY pyproject.toml uv.lock ./

COPY services/scraper/pyproject.toml services/scraper/pyproject.toml
COPY shared/pyproject.toml shared/pyproject.toml

COPY services/scraper/src services/scraper/src
COPY shared/src shared/src

RUN uv sync --frozen --package scraper --no-dev

CMD ["uv", "run", "--package", "scraper", "scraper"]