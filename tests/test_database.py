
from app.database.db import engine, create_tables
from app.database import models

# Create all database tables
create_tables()

# Test Database Connection
try:
    connection = engine.connect()
    print("Database connected successfully!")
    connection.close()

except Exception as e:
    print("Database connection failed:", e)
