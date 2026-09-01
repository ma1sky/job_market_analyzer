from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..base import Base
from .associations import vacancy_skills, search_profile_skills
from .vacancy import Vacancy
from .search_profile import SearchProfile

class Skill(Base):
    __tablename__ = "skills"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    vacancies: Mapped[list["Vacancy"]] = relationship(secondary=vacancy_skills, back_populates="skills")
    search_profiles: Mapped[list["SearchProfile"]] = relationship(secondary=search_profile_skills, back_populates="skills")
