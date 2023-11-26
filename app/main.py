from fastapi import APIRouter, Depends, FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import ORJSONResponse
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from starlette.exceptions import HTTPException
from app.server.routes.log_manager import router as LOG_MANAGER
from app.server.utils import date_utils
from app.server.logger.custom_logger import logger

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None, title='FastAPI Backend', version='1.0.0', swagger_ui_parameters={'defaultModelsExpandDepth': -1}, default_response_class=ORJSONResponse)


# add routes
app.include_router(LOG_MANAGER, tags=['LOG'], prefix='/api/v1')

# add middlewares

app.add_middleware(GZipMiddleware, minimum_size=1000)
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'], allow_headers=['*'])

@app.get('/docs', include_in_schema=False)
async def get_documentation():
    return get_swagger_ui_html(openapi_url='/openapi.json', title=app.title, swagger_ui_parameters=app.swagger_ui_parameters)

@app.get('/openapi.json', include_in_schema=False)
async def openapi():
    return get_openapi(title=app.title, version=app.version, tags=app.openapi_tags, routes=app.routes)

@app.on_event('startup')
async def startup_event():
    logger.debug(f'App startup: {str(date_utils.get_current_date_time())}')
    # Count the number of APIs
    num_apis = len(app.routes)
    print(f'**********************************************\nThere are {num_apis} APIs in this application.\n**********************************************')


@app.on_event('shutdown')
def shutdown_event():
    logger.debug(f'App shutdown: {str(date_utils.get_current_date_time())}')


@app.get('/', tags=['Root'], include_in_schema=False)
async def read_root():
    return {"message": "Welcome to Log Ingestion"}

