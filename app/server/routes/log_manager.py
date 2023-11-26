from typing import Any, Optional

from fastapi import APIRouter, Body, Depends

from app.server.models.logs import LogEntry
from app.server.services import log_manager
import re


router = APIRouter()


@router.post("/ingest-log", summary='Ingest a log')
async def ingest_log(log_entry: LogEntry):
    result = await log_manager.ingest_logs(log_entry.dict())
    return result

@router.get("/search-logs", summary='Search logs')
async def search_logs(
    page: int,
    page_size: int,
    level: Optional[str] = None,
    message: Optional[str] = None,
    resourceId: Optional[str] = None,
    timestamp_start: Optional[str] = None,
    timestamp_end: Optional[str] = None,
    traceId: Optional[str] = None,
    spanId: Optional[str] = None,
    commit: Optional[str] = None,
    parent_resourceId: Optional[str] = None,
):
    
    query = {
        "level": level,
        "message": message,
        "resourceId": resourceId,
        "traceId": traceId,
        "spanId": spanId,
        "commit": commit,
        "metadata.parentResourceId": parent_resourceId,
    }

    # Add timestamp range query if both start and end timestamps are provided
    if timestamp_start and timestamp_end:
        query["timestamp"] = {"$gte": timestamp_start, "$lte": timestamp_end}
    
    elif timestamp_start:
        query["timestamp"] = {"$gte": timestamp_start}

    elif timestamp_end:
        query["timestamp"] = {"$lte": timestamp_start}

    fields_for_case_insensitive_regex = ["level", "message", "resourceId", "traceId", "spanId", "commit", "metadata.parentResourceId"]
    # Remove None values from the query to filter only on provided parameters
    regex_query = {}
    for key, value in query.items():
        if value is not None:
            if key in fields_for_case_insensitive_regex:
                regex_query[key] = {"$regex": re.compile(re.escape(value), re.IGNORECASE)}
            else:
                regex_query[key] = value

    print(regex_query)
    result = await log_manager.get_logs(page, page_size, regex_query)

    return result
    