from fastapi import APIRouter, Depends
from app.models import Article
from app.db import get_session
from typing import List

router = APIRouter()

@router.get("/articles/", response_model=List[Article])
def get_articles(session=Depends(get_session)):
    return session.query(Article).all()

@router.post("/articles/", response_model=Article)
def create_article(article: Article, session=Depends(get_session)):
    session.add(article)
    session.commit()
    session.refresh(article)
    return article