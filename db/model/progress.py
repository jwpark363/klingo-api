## scenario, quest progress state table
from datetime import datetime
from typing import Optional, Any
from pydantic import BaseModel
from sqlmodel import Field, SQLModel
from enum import Enum
from sqlalchemy.types import JSON
from sqlalchemy import Column
from scenario import StageType

class ProgressState(Enum):
    START = 1
    DOING = 2
    DONE  = 3

# Models
class Progress(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id : int = Field(foreign_key="user.id")
    scenario_id: int = Field(foreign_key="scenario.id")
    stage_type: StageType
    state_type: ProgressState
    state_info: dict[str,Any] = Field(default={}, sa_column=Column(JSON))
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    
class ProgressResponse(BaseModel):
    id: int
    user_id: int
    scenario_id: int
    stage_type: StageType
    state_type: ProgressState
    state_info: dict[str,Any]
    updated_at: datetime
    
class ProgressCreate(BaseModel):
    user_id: int
    scenario_id: int
    stage_type: StageType
    state_type: ProgressState
    state_info: dict[str,Any]
