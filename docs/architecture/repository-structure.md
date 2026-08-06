## Project Structure

```text
job-market-analyzer/
│
├── docs/                     # Documentation
│   ├── architecture/
│   ├── diagrams/
│   ├── database/
│   ├── api/
│   ├── testing/
│   └── adr/
│
├── infrastructure/           # Infrastructure configuration
│   ├── docker/
│   ├── postgres/
│   ├── redis/
│   └── monitoring/
│
├── services/
│   ├── scraper/
│   │   ├── app/
│   │   │   ├── clients/
│   │   │   ├── config/
│   │   │   ├── coordinator/
│   │   │   ├── dto/
│   │   │   ├── parsers/
│   │   │   │   ├── hh/
│   │   │   │   ├── habr/
│   │   │   │   └── remoteok/
│   │   │   ├── publisher/
│   │   │   ├── scheduler/
│   │   │   ├── core/
│   │   │   └── main.py
│   │   │
│   │   ├── tests/
│   │   ├── Dockerfile
│   │   └── pyproject.toml
│   │
│   ├── etl/
│   └── analytics/
│
├── shared/                   # Shared packages
│   ├── dto/
│   ├── utils/
│   ├── database/
│   ├── logging/
│   ├── config/
│   └── exceptions/
│
├── docker-compose.yml
├── .env.example
├── pyproject.toml
└── README.md
```