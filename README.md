# LOG INGESTION

## Setting up MongoDB Database

    • Setup MongoDB database using [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) or run it locally.

    • Copy the MongoDB URI.

## Configuring Your App

    • Paste the MongoDB URI in the config file of your application. The config file is usually named `config.py` which is inside the ./app/server/config/.

        ```
        MONGO_URI = "<your_mongo_uri>"
        ```
        example: your_mongo_uri = "mongodb://localhost:27017/log_ingestion"
        where log_ingestion is the database_name

## Installing Dependencies

    • Install the required Python modules using pip.
        Create a virtual env:
        ```bash
        python -m venv env
        ```

        Install module using pip
        ```bash
        pip install fastapi[all]==0.95.2 loguru==0.7.0 motor==3.2.0 uvicorn==0.23.2 python-dotenv==1.0.0
        ```

## Running Your Application

    • Run the application on port 3000 using the following command.

        ```bash
        uvicorn app.main:app --host 0.0.0.0 --port 3000 --reload
        ```

Your FastAPI application should now be running on [http://localhost:3000/docs].

## Ingesting Logs

### Route: `/ingest-log`

To insert logs into the database, use the `/ingest-log` route with the following payload:

```json
{
  "level": "Error message",
  "message": "Failed to CONNECT to db",
  "resourceId": "server-12345",
  "timestamp": "23-09-17T08:00:00Z",
  "traceId": "abc-xyz-123",
  "spanId": "span-456",
  "commit": "5e4fc2",
  "metadata": {
    "parentResourceId": "server-0987"
  }
```

Response:
{
  "message": "Log ingested successfully",
  "log_id": "655a146eb1aed0dd9b3ade0f"
}

## Searching Logs

### Route: `/search-logs`

To search logs, use the `/search-logs` route with the following filters:

- level
- message
- resourceId
- timestamp_start
- timestamp_end
- traceId
- spanId
- commit

#### Additional Features:

1. *Pagination:*

   Pass `page` (by default=1) and `page_size` (by default=10) to get the next page where there is more data than `page_size`.

   Example:
   ```bash
   /search-logs?page=2&page_size=20
   ```

2. Date Range Search:

   To filter logs between specific date ranges, pass timestamp_start and timestamp_end in the format "YYYY-MM-DDTHH:MM:SSZ".
    Example:
   ```bash
   /search-logs?timestamp_start=2023-09-10T00:00:00Z&timestamp_end=2023-09-15T23:59:59Z
   ```

3. Regular Expression Search:

    Utilize regular expressions for search. For example, searching for level with "error" will match values like ["Error", "eRRor"]. Similarly, in the message field, searching for "connect" or "connect to db" will match messages containing these keywords or expressions.
    Example:
   ```bash
   /search-logs?level=error&message=connect
   ```

along with this we have also included database as mongodb atlas which has following benefits because it has the capability to run in multiple nodes and managed by mongodb which helps in data backup and scalability
- Volume: The ability of your system to ingest massive volumes.
- Speed: Efficiency in returning search results.
- Scalability: Adaptability to increasing volumes of logs/queries.

For more information about FastAPI, refer to the [FastAPI documentation](https://fastapi.tiangolo.com/).