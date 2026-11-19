from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite Database URL
DATABASE_URL = "sqlite:///campushub.db"

# Create Database Engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Create Session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Create Base Class
Base = declarative_base()


# Get Database Session
def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()



# Create Database Tables
def create_tables():
    from app.database import models

    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")
