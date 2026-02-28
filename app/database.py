from sqlalchemy import create_engine
feature/ci-setup
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import sessionmaker, declarative_base
develop

DATABASE_URL = "sqlite:///./campus.db"

engine = create_engine(
feature/ci-setup
    DATABASE_URL, connect_args={"check_same_thread": False}

    DATABASE_URL,
    connect_args={"check_same_thread": False}
 develop
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

 feature/ci-setup
Base = declarative_base()

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
 develop
