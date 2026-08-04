# C3 - Scraper Service

```mermaid
flowchart LR

    scheduler["Scheduler"]

    orchestrator["Scraper Orchestrator"]

    hh["HH Scraper"]
    habr["Habr Scraper"]
    remote["RemoteOK Scraper"]

    mapper["DTO Mapper"]

    redis[("Redis Queue")]

    sites["Job Sites"]

    scheduler --> orchestrator

    orchestrator --> hh
    orchestrator --> habr
    orchestrator --> remote

    hh --> sites
    habr --> sites
    remote --> sites

    hh --> mapper
    habr --> mapper
    remote --> mapper

    mapper -->|"VacancyDTO"| redis
```

# C3 - ETL Service

```mermaid
flowchart LR

    redis[("Redis Queue")]

    consumer["Queue Consumer"]

    transformer["Transformer"]

    validator["Validator"]

    deduplicator["Deduplicator"]

    repository["Repository"]

    postgres[("PostgreSQL")]

    redis --> consumer

    consumer --> transformer

    transformer --> validator

    validator --> deduplicator

    deduplicator --> repository

    repository --> postgres
```

# C3 - Analytics Service

```mermaid
flowchart LR

    router["FastAPI Router"]

    service["Analytics Service"]

    repository["Repository"]

    cache[("Redis Cache")]

    postgres[("PostgreSQL")]

    router --> service

    service --> cache

    service --> repository

    repository --> postgres
```