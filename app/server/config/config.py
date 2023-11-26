import os

# Mongo configuration
MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/log_ingestion')

