
from sqlalchemy import inspect
from app.database.db import engine, create_tables

create_tables()

inspector = inspect(engine)

print("\nDatabase Tables:")

for table in inspector.get_table_names():
    print(table)
