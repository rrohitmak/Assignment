import logging
import asyncio
import subprocess
from fastapi import FastAPI, Request
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


async def main():
    command = "uvicorn main:app --host 0.0.0.0 --port 8000"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    asyncio.run(main())
