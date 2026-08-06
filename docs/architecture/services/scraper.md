# Scraper Service

## Purpose

Scraper Service is responsible for collecting vacancy data from external job boards.

The service periodically requests vacancy pages, parses HTML or JSON responses,
normalizes extracted data into a common DTO and publishes messages to Redis.

---

## Responsibilities

- Schedule scraping jobs
- Download vacancy pages
- Parse source-specific data
- Normalize vacancies
- Handle retries
- Publish VacancyDTO to Redis
- Log scraping statistics

---

## Does NOT

- Store data in PostgreSQL
- Perform analytics
- Transform business data

## C3 components

```mermaid
flowchart LR

sites["🌐 Job Sites"]

redis[("🟥 Redis Queue")]

subgraph scraper["🕷️ Scraper Service"]

    direction TB

    scheduler["⏰ Scheduler"]

    coordinator["🎯 Scraper Coordinator"]

    subgraph parsers["📄 Site Parsers"]

        hh["HH Parser"]

        habr["Habr Parser"]

        remote["RemoteOK Parser"]

    end

    normalize["🧩 Normalization Layer"]

end

scheduler --> coordinator

coordinator --> hh
coordinator --> habr
coordinator --> remote

hh -->|"HTTPS"| sites
habr -->|"HTTPS"| sites
remote -->|"HTTPS"| sites

hh --> normalize
habr --> normalize
remote --> normalize

normalize -->|"Publish DTO"| redis

class scheduler,coordinator,hh,habr,remote,normalize service

class redis cache

class sites external
```