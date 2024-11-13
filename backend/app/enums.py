from enum import Enum
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class UrlType(str, Enum):
    ORIGINAL = "original"
    PAYWALL_FREE = "paywall-free"
    CACHED = "cached"
