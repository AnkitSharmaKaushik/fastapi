from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from databases import Database

DATABASE_URL = "sqlite:////home/ankit/Desktop/Framework/FastApi/attendance_system/app/database/database.db"

# Create an engine (Synchronous for table creation)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Async Database connection for FastAPI
database = Database(DATABASE_URL)

# Metadata to store schema information
metadata = MetaData()

# Base for ORM Models
Base = declarative_base()
