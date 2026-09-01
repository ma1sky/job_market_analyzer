from ..base import Base
from .associations import vacancy_skills, vacancy_work_conditions
from .salary import Salary
from datetime import datetime
from typing import Optional
from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    Text,
    UniqueConstraint,
    func,
)
from sqlalchemy.dialects.postgresql import INT4RANGE, Range
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)


from .company import Company
from .location import Location
from .salary import Salary
from .skill import Skill
from .source import Source
from .work_condition import WorkCondition

class Vacancy(Base):
    __tablename__ = "vacancies"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    external_id: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    company_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("companies.id"),
    )

    location_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("locations.id"),
    )

    source_id: Mapped[int] = mapped_column(
        ForeignKey("sources.id"),
        nullable=False,
    )

    relocation: Mapped[Optional[bool]] = mapped_column(
        Boolean,
    )

    experience_range: Mapped[Optional[Range[int]]] = mapped_column(
        INT4RANGE,
    )

    grade: Mapped[Optional[str]] = mapped_column(
        Text,
    )

    link: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    description: Mapped[Optional[str]] = mapped_column(
        Text,
    )

    publication_date: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
    )

    parsing_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    company: Mapped[Optional["Company"]] = relationship(
        back_populates="vacancies",
    )

    location: Mapped[Optional["Location"]] = relationship(
        back_populates="vacancies",
    )

    source: Mapped["Source"] = relationship(
        back_populates="vacancies",
    )

    salary: Mapped[Optional["Salary"]] = relationship(
        back_populates="vacancy",
        uselist=False,
        cascade="all, delete-orphan",
    )

    skills: Mapped[list["Skill"]] = relationship(
        secondary=vacancy_skills,
        back_populates="vacancies",
    )

    work_conditions: Mapped[list["WorkCondition"]] = relationship(
        secondary=vacancy_work_conditions,
        back_populates="vacancies",
    )

    __table_args__ = (
        UniqueConstraint(
            "source_id",
            "external_id",
            name="uq_vacancy_source_external_id",
        ),
    )
