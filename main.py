import logging
import asyncio
from fastapi import FastAPI, Request
import uvicorn
from controllers import controller

app = FastAPI()
app.include_router(controller.router)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@app.middleware("http")
async def front_controller(request: Request, call_next):
    print(f"Front Controller processing request: {
          request.method} {request.url.path}")
    response = await call_next(request)
    return response


@app.get("/")
async def app_running():
    print("App Running")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000,
                log_config="log.ini", reload=True)
