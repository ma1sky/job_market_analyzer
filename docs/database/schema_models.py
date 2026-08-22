from sqlalchemy import Column, ForeignKey, Integer, Interval
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


class Vacancy(Base):
    __tablename__ = "vacancy"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(Interval, nullable=True)

    table_2 = relationship("Table2")


class Table2(Base):
    __tablename__ = "table_2"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    vacancy_id = Column(Integer, ForeignKey("vacancy.id"), nullable=True)

    vacancy = relationship("Vacancy")