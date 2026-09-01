from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..base import Base
from .associations import search_profile_sources
from .vacancy import Vacancy
from .search_profile import SearchProfile

class Source(Base):
    __tablename__ = "sources"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    base_url: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    vacancies: Mapped[list["Vacancy"]] = relationship(back_populates="source")
    search_profiles: Mapped[list["SearchProfile"]] = relationship(secondary=search_profile_sources, back_populates="sources")
