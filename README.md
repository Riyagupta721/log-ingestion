# LOG INGESTION

## Setting up MongoDB Database

    • Setup MongoDB database using [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) or run it locally.

    • Copy the MongoDB URI.

## Configuring Your App

    • Paste the MongoDB URI in the config file of your application. The config file is usually named `config.py` which is inside the ./app/server/config/.

        ```
        MONGO_URI = "<your_mongo_uri>"
        ```

## Installing Dependencies

    • Install the required Python modules using pip.

        ```bash
        pip install fastapi[all]==0.95.2 loguru==0.7.0 motor==3.2.0 uvicorn==0.23.2
        ```

## Running Your Application

    • Run the application on port 3000 using the following command.

        ```bash
        uvicorn app.main:app --host 0.0.0.0 --port 3000 --reload
        ```

Your FastAPI application should now be running on [http://localhost:3000/docs].

For more information about FastAPI, refer to the [FastAPI documentation](https://fastapi.tiangolo.com/).
