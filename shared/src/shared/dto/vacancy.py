from datetime import datetime

from pydantic import BaseModel, ConfigDict, HttpUrl


class SalaryDTO(BaseModel):
    model_config = ConfigDict(extra="ignore")

    salary_from: int | None = None
    salary_to: int | None = None
    currency: str | None = None


class VacancyDTO(BaseModel):
    model_config = ConfigDict(extra="ignore")

    source: str
    external_id: str

    title: str
    description: str | None = None

    company: str | None = None

    location: str | None = None
    remote: bool | None = None

    salary: SalaryDTO | None = None

    url: HttpUrl

    published_at: datetime | None = None
    scraped_at: datetime