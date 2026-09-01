from sqlalchemy import Column, ForeignKey, Table
from ..base import Base

vacancy_skills = Table("vacancy_skills", Base.metadata,
    Column("vacancy_id", ForeignKey("vacancies.id", ondelete="CASCADE"), primary_key=True),
    Column("skill_id", ForeignKey("skills.id", ondelete="CASCADE"), primary_key=True))
vacancy_work_conditions = Table("vacancy_work_conditions", Base.metadata,
    Column("vacancy_id", ForeignKey("vacancies.id", ondelete="CASCADE"), primary_key=True),
    Column("work_condition_id", ForeignKey("work_conditions.id", ondelete="CASCADE"), primary_key=True))
search_profile_keywords = Table("search_profile_keywords", Base.metadata,
    Column("search_profile_id", ForeignKey("search_profiles.id", ondelete="CASCADE"), primary_key=True),
    Column("keyword_id", ForeignKey("keywords.id", ondelete="CASCADE"), primary_key=True))
search_profile_skills = Table("search_profile_skills", Base.metadata,
    Column("search_profile_id", ForeignKey("search_profiles.id", ondelete="CASCADE"), primary_key=True),
    Column("skill_id", ForeignKey("skills.id", ondelete="CASCADE"), primary_key=True))
search_profile_locations = Table("search_profile_locations", Base.metadata,
    Column("search_profile_id", ForeignKey("search_profiles.id", ondelete="CASCADE"), primary_key=True),
    Column("location_id", ForeignKey("locations.id", ondelete="CASCADE"), primary_key=True))
search_profile_sources = Table("search_profile_sources", Base.metadata,
    Column("search_profile_id", ForeignKey("search_profiles.id", ondelete="CASCADE"), primary_key=True),
    Column("source_id", ForeignKey("sources.id", ondelete="CASCADE"), primary_key=True))
