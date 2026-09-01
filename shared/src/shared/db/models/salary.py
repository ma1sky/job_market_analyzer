from decimal import Decimal
from typing import Optional
from .vacancy import Vacancy
from sqlalchemy import (
    Boolean,
    CheckConstraint,
    ForeignKey,
    Integer,
    Numeric,
    String,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from ..base import Base

class Salary(Base):
    __tablename__ = "salaries"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    vacancy_id: Mapped[int] = mapped_column(
        ForeignKey("vacancies.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
    )

    min_amount: Mapped[Optional[Decimal]] = mapped_column(
        Numeric(12, 2),
    )

    max_amount: Mapped[Optional[Decimal]] = mapped_column(
        Numeric(12, 2),
    )

    currency: Mapped[Optional[str]] = mapped_column(
        String(3),
    )

    period: Mapped[Optional[str]] = mapped_column(
        String(20),
    )

    gross: Mapped[Optional[bool]] = mapped_column(
        Boolean,
    )

    vacancy: Mapped["Vacancy"] = relationship(
        back_populates="salary",
    )

    __table_args__ = (
        CheckConstraint(
            """
            min_amount IS NULL
            OR max_amount IS NULL
            OR min_amount <= max_amount
            """,
            name="ck_salary_min_le_max",
        ),

        CheckConstraint(
            """
            min_amount IS NULL
            OR min_amount >= 0
            """,
            name="ck_salary_min_non_negative",
        ),

        CheckConstraint(
            """
            max_amount IS NULL
            OR max_amount >= 0
            """,
            name="ck_salary_max_non_negative",
        ),
    )

