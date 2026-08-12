from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Optional


class IssueStatus(str, Enum):
    open = "open"
    in_progress = "in_progress"
    closed = "closed"


class IssuePriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class IssueCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str = Field(None, max_length=1000)
    priority: IssuePriority = Field(default=IssuePriority.medium)

class IssueUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, max_length=1000)
    status: Optional[IssueStatus] = None
    priority: Optional[IssuePriority] = None

class IssueOut(BaseModel):
    id: str
    title: str
    description: Optional[str]
    status: IssueStatus
    priority: IssuePriority

    

    


