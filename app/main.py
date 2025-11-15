# pip install python-dotenv
import os

from fastapi import FastAPI
from dotenv import load_dotenv

from config.mysql_config import engine, Base

load_dotenv()

# pip install fastapi

app = FastAPI()

if __name__ == "__main__":
    # pip install uvicorn
    import uvicorn
    host = os.getenv("APP_HOST")
    port = int(os.getenv("APP_PORT"))
    uvicorn.run(app, host=host, port=port)
    Base.metadata.create_all(bind=engine)
    uvicorn.run(app, host=host, port=port)