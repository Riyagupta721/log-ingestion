import asyncio
from datetime import timedelta
from typing import Any, Optional

from fastapi import HTTPException, status

from app.server.database.db import client, mongo

async def ingest_logs(data: dict):
    collection = mongo.get_collection('logs')
    result = await collection.insert_one(data)
    return {"message": "Log ingested successfully", "log_id": str(result.inserted_id)}

async def get_logs(page, page_size, query):
    collection = mongo.get_collection('logs')
    result = await collection.find(query).sort("timestamp", -1).skip((page - 1) * page_size).limit(page_size).to_list(page_size)
    for data in result:
        data["_id"] = str(data["_id"])
    return result 
