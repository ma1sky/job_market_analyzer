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
- Produce data to Kafka
- Log scraping statistics

---

## Does NOT

- Store data in PostgreSQL
- Perform analytics
- Transform business data

## C3 components

```mermaid
flowchart TD

sites["🌐 Job Sites"]

kafka@{ shape: das, label: "💬 Apache Kafka" }

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

normalize -->|"Produce"| kafka

%% ============================================================
%%                        STYLES (classDef)
%% ============================================================

classDef actor fill:#21262D,stroke:#8B949E,stroke-width:2px,color:#F0F6FC;

classDef service fill:#1F2937,stroke:#58A6FF,stroke-width:2px,color:#F0F6FC;

classDef database fill:#0E4429,stroke:#3FB950,stroke-width:2px,color:#F0F6FC;

classDef cache fill:#4D3A12,stroke:#F2CC60,stroke-width:2px,color:#F0F6FC;

classDef queue fill:#4D3A12,stroke:#F2CC60,stroke-width:2px,color:#F0F6FC;

classDef dashboard fill:#35264C,stroke:#BC8CFF,stroke-width:2px,color:#F0F6FC;

classDef external fill:#2D1B16,stroke:#FF7B72,stroke-width:2px,color:#F0F6FC;

classDef storage fill:#0E4429,stroke:#2EA043,stroke-width:2px,color:#F0F6FC;

classDef scheduler fill:#3A2F00,stroke:#D29922,stroke-width:2px,color:#F0F6FC;

classDef message fill:#2D333B,stroke:#768390,stroke-width:1px,color:#F0F6FC;

classDef brokerFill fill:#4D3A12,stroke:#F2CC60,stroke-width:2px,color:#F0F6FC;

%% ============================================================
%%                 APPLYING STYLES (class)
%% ===========================================================

class scheduler,coordinator,hh,habr,remote,normalize service

class redis cache

class sites external
class kafka brokerFill
```