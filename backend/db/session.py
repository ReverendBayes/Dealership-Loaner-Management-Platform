# db/session.py
# Configures the SQLAlchemy engine, session, and database connection

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Load database URL from environment or default to local file
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./dealership.db")

# Create the SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
)

# SessionLocal is used to interact with the DB in routes and services
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)