from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://youruser:yourpassword@db:5432/yourdb"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)
Base = declarative_base()

# Function to get a session, used as a dependency
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session
        
async def init_db():
    Base.metadata.create_all(bind=engine)
