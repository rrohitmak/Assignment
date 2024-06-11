from .database import engine_1, engine_2
from .self_ship import Base as Base_1
from .client import Base as Base_2
Base_1.metadata.create_all(bind=engine_1)
Base_2.metadata.create_all(bind=engine_2)
