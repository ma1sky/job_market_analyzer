from typing import Optional
from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..base import Base
from .associations import search_profile_locations
from .vacancy import Vacancy
from .search_profile import SearchProfile

class Location(Base):
    __tablename__ = "locations"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    country: Mapped[Optional[str]] = mapped_column(Text)
    city: Mapped[Optional[str]] = mapped_column(Text)
    vacancies: Mapped[list["Vacancy"]] = relationship(back_populates="location")
    search_profiles: Mapped[list["SearchProfile"]] = relationship(secondary=search_profile_locations, back_populates="locations")
