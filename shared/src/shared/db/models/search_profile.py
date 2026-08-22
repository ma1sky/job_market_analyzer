from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from shared.db.base import Base


class SearchProfile(Base):
    __tablename__ = "search_profiles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )