
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)

        return cls._instance

    def __init__(self):
        if hasattr(self, "_initialized"):
            return

        self.DATABASE_URL = "sqlite:///campushub.db"

        self.engine = create_engine(
            self.DATABASE_URL,
            connect_args={"check_same_thread": False}
        )

        self.SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine
        )

        self.Base = declarative_base()

        self._initialized = True


# Create the Singleton database instance
database = Database()

# Keep existing names compatible with the project
engine = database.engine
SessionLocal = database.SessionLocal
Base = database.Base


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
