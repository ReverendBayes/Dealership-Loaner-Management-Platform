# db/base.py
# SQLAlchemy declarative base used by all ORM models

from sqlalchemy.ext.declarative import declarative_base

# This base class allows us to define mapped classes
# that SQLAlchemy uses to create and manage database tables
Base = declarative_base()