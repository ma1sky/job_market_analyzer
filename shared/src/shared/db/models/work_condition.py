from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..base import Base
from .associations import vacancy_work_conditions
from .vacancy import Vacancy

class WorkCondition(Base):
    __tablename__ = "work_conditions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    vacancies: Mapped[list["Vacancy"]] = relationship(secondary=vacancy_work_conditions, back_populates="work_conditions")
