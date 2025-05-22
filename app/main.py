from fastapi import FastAPI
import uvicorn
import auth, database, models, schemas
from database import get_db
from sqlalchemy.orm import Session

app = FastAPI()

# Create the database tables
database.Base.metadata.create_all(bind=database.engine)

