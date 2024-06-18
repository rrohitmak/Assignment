import logging
import asyncio
import subprocess
from fastapi import FastAPI
from controllers import controller

app = FastAPI()
app.include_router(controller.router)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


async def main():
    command = "uvicorn main:app --host 0.0.0.0 --port 8000"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    asyncio.run(main())
