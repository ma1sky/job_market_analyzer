from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..base import Base
from .associations import search_profile_keywords
from .search_profile import SearchProfile

class Keyword(Base):
    __tablename__ = "keywords"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    word: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    search_profiles: Mapped[list["SearchProfile"]] = relationship(secondary=search_profile_keywords, back_populates="keywords")
