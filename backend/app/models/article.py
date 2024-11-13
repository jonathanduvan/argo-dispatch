from __future__ import annotations

from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from app.models.article_content import ArticleContent
    from app.models.author import Author

class Article(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    publication_date: Optional[datetime]
    paywall_flag: bool
    validation_score: Optional[float]

    # Relationships
    contents: List[ArticleContent] = Relationship(back_populates="article")
    author: Optional[Author] = Relationship(back_populates="articles")
