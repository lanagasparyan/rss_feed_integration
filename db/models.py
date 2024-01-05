# models.py

from pydantic import BaseModel, Field
from typing import Optional
import datetime
import uuid

class Article(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    source_feed: str
    publication_date: str
    content: str
    fetch_date: Optional[str] = datetime.datetime.now().isoformat()
    processed: Optional[bool] = False
