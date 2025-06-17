from fastapi import FastAPI, Request
from starlette.responses import JSONResponse

from configs import configs

app = FastAPI()

@app.get("/", tags=["healthcheck"])
async def read_root():
    return {"Hello": "World"}

@app.middleware("http")
async def verify_api_key_middleware(request: Request, call_next):
    if configs.ENV == "prod" and request.url.path not in configs.EXCLUDE_PATHS:
        api_key = request.headers.get(configs.API_KEY_NAME)
        if api_key != configs.API_KEY:
            return JSONResponse(status_code=401, content={"detail": "Unauthorized"})
    response = call_next(request)
    return response
    