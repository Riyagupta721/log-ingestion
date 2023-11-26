from pydantic import BaseModel
from typing import Any, List, Optional, Union


class LogEntry(BaseModel):
    level: str
    message: str
    resourceId: str
    timestamp: str
    traceId: Optional[str] = None
    spanId: Optional[str] = None
    commit: Optional[str] = None
    metadata: Optional[dict] = {}