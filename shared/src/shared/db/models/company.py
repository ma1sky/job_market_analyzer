from typing import Optional
from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..base import Base
from .vacancy import Vacancy

class Company(Base):
    __tablename__ = "companies"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    phone_number: Mapped[Optional[str]] = mapped_column(Text)
    email: Mapped[Optional[str]] = mapped_column(Text)
    description: Mapped[Optional[str]] = mapped_column(Text)
    link: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    vacancies: Mapped[list["Vacancy"]] = relationship(back_populates="company")
