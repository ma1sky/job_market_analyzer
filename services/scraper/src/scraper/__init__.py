from datetime import datetime, timezone

from shared.dto.vacancy import VacancyDTO, SalaryDTO
from pydantic import HttpUrl


def main() -> None:
    print(vacancy_mock)


vacancy_mock = VacancyDTO(
    source="hh",
    external_id="12345678",

    title="Python Backend Developer",
    description="Разработка backend-сервисов на Python.",

    company="Yandex",

    location="Moscow",
    remote=True,

    salary=SalaryDTO(
        salary_from=250000,
        salary_to=350000,
        currency="RUR",
    ),

    url=HttpUrl("https://hh.ru/vacancy/12345678"),

    published_at=datetime(
        2026, 8, 10, 12, 0, tzinfo=timezone.utc
    ),

    scraped_at=datetime.now(timezone.utc),
)

if __name__ == '__main__':
    main()
