from .database import engine_1
from .client import Base
Base.metadata.create_all(bind=engine_1)
