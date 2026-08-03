```mermaid
flowchart LR

User([User])
Admin([Administrator])

System["Job Market Analyzer"]

Sites["Job Sites<br/>HH, Habr, RemoteOK"]
Dashboard["Dashboard"]

User -->|View dashboards| Dashboard
Dashboard -->|REST API| System
Admin -->|Configure scraping| System
System -->|HTTPS| Sites
User -->|REST API| System
```