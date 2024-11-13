from __future__ import annotations

from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
from app.enums import UrlType

if TYPE_CHECKING:
  from app.models.article import Article
  

class ArticleContent(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    url: str
    url_type: UrlType

    article_id: int = Field(foreign_key="article.id")
    article: Optional[Article] = Relationship(back_populates="contents")
