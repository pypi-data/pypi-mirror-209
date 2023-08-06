from fastapi import Depends, FastAPI
from fastapi.openapi.utils import get_openapi
from starlette.requests import Request
from starlette.responses import Response
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from api import health_api, rule_api
app = FastAPI()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Rule Engine",
        version="1.0.0",
        description="Rule Engine API's",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


async def catch_global_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "message": f"Error occured while processing request",
                "Error": str(e),
            },
        )


app.middleware("http")(catch_global_exceptions_middleware)
app.openapi = custom_openapi

app.include_router(
    health_api.router,
    prefix="/api/v1",
    tags=["Health"],
)

app.include_router(
    rule_api.router,
    prefix="/api/v1",
    tags=["Rules"],
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def welcome():
    return "Rule_Engine"