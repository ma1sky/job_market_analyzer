from datetime import datetime
from typing import Optional
from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.dialects.postgresql import INT4RANGE, Range
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..base import Base
from .associations import search_profile_keywords, search_profile_skills, search_profile_locations, search_profile_sources
from .keyword import Keyword
from .location import Location
from .skill import Skill
from .source import Source

class SearchProfile(Base):
    __tablename__ = "search_profiles"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, server_default="true")
    experience_range: Mapped[Optional[Range[int]]] = mapped_column(INT4RANGE)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now(), onupdate=func.now())
    keywords: Mapped[list["Keyword"]] = relationship(secondary=search_profile_keywords, back_populates="search_profiles")
    skills: Mapped[list["Skill"]] = relationship(secondary=search_profile_skills, back_populates="search_profiles")
    locations: Mapped[list["Location"]] = relationship(secondary=search_profile_locations, back_populates="search_profiles")
    sources: Mapped[list["Source"]] = relationship(secondary=search_profile_sources, back_populates="search_profiles")
